/**
 * Embed the LS100 chat chunks into a vector index the browser can search.
 *
 * Run AFTER build_chat_index.py. Reads <build>/ls100-chat/chunks.json and writes
 * <build>/ls100-chat/index.json, then copies the model files into the build so
 * the browser loads them from this site rather than a third party.
 *
 * dtype is pinned to 'q8' here and in the widget on purpose. Transformers.js
 * defaults to fp32 in Node but q8 in the browser, so leaving it unset would
 * build the index with one quantisation and query it with another - the scores
 * still look plausible, which is what makes it easy to miss.
 *
 * Vectors are unit-length, so cosine similarity is a plain dot product. They are
 * stored as int8 (a ~4x smaller file than JSON floats); the widget divides by
 * 127 to recover them, which costs about 0.4% of precision and changes no
 * rankings.
 *
 * Usage:  node scripts/embed_chat_index.mjs [build_dir]     (default _build/html)
 *         (the widget loads the model itself from the Hugging Face CDN)
 */
import { pipeline, env } from '@huggingface/transformers';
import fs from 'node:fs';
import path from 'node:path';

const MODEL = 'Xenova/all-MiniLM-L6-v2';
const DTYPE = 'q8';
const BATCH = 64;

const buildDir = process.argv[2] || '_build/html';
const outDir = path.join(buildDir, 'ls100-chat');
const chunksPath = path.join(outDir, 'chunks.json');

if (!fs.existsSync(chunksPath)) {
  console.error(`missing ${chunksPath} - run scripts/build_chat_index.py first`);
  process.exit(1);
}

const cacheDir = path.join(outDir, '.model-cache');
env.cacheDir = cacheDir;

const { chunks } = JSON.parse(fs.readFileSync(chunksPath, 'utf8'));
console.log(`embedding ${chunks.length} chunks with ${MODEL} (${DTYPE})`);

const extractor = await pipeline('feature-extraction', MODEL, { dtype: DTYPE });

// Prepending the page title and section gives each chunk the context a bare
// paragraph lacks ("Step 3" means little without "Pose Estimation").
const asInput = (c) => [c.title, c.section, c.text].filter(Boolean).join(' › ');

const vectors = [];
let dim = 0;
for (let i = 0; i < chunks.length; i += BATCH) {
  const batch = chunks.slice(i, i + BATCH);
  const out = await extractor(batch.map(asInput), { pooling: 'mean', normalize: true });
  dim = out.dims[1];
  for (let r = 0; r < out.dims[0]; r++) {
    vectors.push(out.data.subarray(r * dim, (r + 1) * dim));
  }
  process.stdout.write(`\r  ${Math.min(i + BATCH, chunks.length)}/${chunks.length}`);
}
process.stdout.write('\n');

// int8 quantisation: values are in [-1, 1] because the vectors are normalised.
const quantized = Buffer.alloc(vectors.length * dim);
vectors.forEach((vec, r) => {
  for (let c = 0; c < dim; c++) {
    const v = Math.round(vec[c] * 127);
    quantized[r * dim + c] = Math.max(-127, Math.min(127, v)) & 0xff;
  }
});

const index = {
  model: MODEL,
  dtype: DTYPE,
  dim,
  count: chunks.length,
  generated: new Date().toISOString(),
  vectors: quantized.toString('base64'),
  chunks: chunks.map((c) => ({
    u: c.url,
    t: c.title,
    s: c.section,
    k: c.kind,
    x: c.text,
  })),
};

const indexPath = path.join(outDir, 'index.json');
fs.writeFileSync(indexPath, JSON.stringify(index));
const mb = (fs.statSync(indexPath).size / 1e6).toFixed(2);
console.log(`wrote ${indexPath}  (${chunks.length} x ${dim}, ${mb} MB)`);

// The model weights are deliberately NOT published with the site. The browser
// build of transformers.js 4.2.0 does not load a tokenizer from
// env.localModelPath - it returns a pipeline whose tokenizer is not callable,
// without ever issuing a request - so the widget loads the weights from the
// Hugging Face CDN instead. Publishing an unused 23 MB copy would only add
// weight to every deploy.
fs.rmSync(cacheDir, { recursive: true, force: true });
fs.rmSync(path.join(outDir, 'models'), { recursive: true, force: true });
fs.rmSync(chunksPath, { force: true });   // intermediate; not needed at runtime
