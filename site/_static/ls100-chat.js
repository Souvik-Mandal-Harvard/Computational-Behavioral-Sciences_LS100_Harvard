/**
 * LS100 course search - semantic search over the course materials, running
 * entirely in the reader's browser. No server, no API key, no cost.
 *
 * A query is embedded locally with all-MiniLM-L6-v2 and compared against a
 * vector index built at deploy time from the site's own pages. Results are
 * passages the course actually contains, linked to the section they came from;
 * nothing is generated, so it cannot invent an answer.
 *
 * dtype is pinned to 'q8' to match the build step. Transformers.js would
 * otherwise default differently in Node and the browser, quietly querying the
 * index in a different quantisation than it was built with.
 */
(function () {
  'use strict';

  if (window.__ls100ChatLoaded) return;   // survives client-side navigation
  window.__ls100ChatLoaded = true;

  // The `/dist/transformers.min.js` build, not jsdelivr's `+esm` wrapper, and
  // pinned: an unpinned CDN import would let a future release change behaviour
  // under the site without warning.
  var TRANSFORMERS = 'https://cdn.jsdelivr.net/npm/@huggingface/transformers@4.2.0/dist/transformers.min.js';
  var MODEL = 'Xenova/all-MiniLM-L6-v2';
  var DTYPE = 'q8';
  var MAX_RESULTS = 6;
  var MIN_SCORE = 0.25;   // below this the passage is unrelated; say so instead

  // The script lives at <siteRoot>/ls100-chat/ls100-chat.js, so the site root is
  // recoverable from its own URL. This keeps the widget working whether the site
  // is served from / or from /teaching-learning/ls100.
  var self = document.currentScript && document.currentScript.src;
  var siteRoot = self ? self.replace(/\/ls100-chat\/ls100-chat\.js.*$/, '') : '';
  var assets = siteRoot + '/ls100-chat/';

  var state = { open: false, ready: false, pending: null, index: null, embed: null };

  // ---------------------------------------------------------------- markup
  var root = document.createElement('div');
  root.className = 'ls100-chat';
  root.innerHTML = [
    '<button class="ls100-chat__fab" type="button" aria-expanded="false"',
    '        aria-controls="ls100-chat-panel" title="Search the course">',
    '  <svg viewBox="0 0 24 24" aria-hidden="true" width="22" height="22">',
    '    <circle cx="11" cy="11" r="7" fill="none" stroke="currentColor" stroke-width="2"/>',
    '    <path d="M16.5 16.5 L21 21" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>',
    '  </svg>',
    '  <span>Ask the course</span>',
    '</button>',
    '<section class="ls100-chat__panel" id="ls100-chat-panel" role="dialog"',
    '         aria-label="Search the course materials" hidden>',
    '  <header class="ls100-chat__head">',
    '    <div>',
    '      <strong>Ask the course</strong>',
    '      <span class="ls100-chat__sub">Finds passages from the LS100 materials</span>',
    '    </div>',
    '    <button class="ls100-chat__close" type="button" aria-label="Close">&times;</button>',
    '  </header>',
    '  <form class="ls100-chat__form">',
    '    <input class="ls100-chat__input" type="search" autocomplete="off"',
    '           placeholder="e.g. how do I extract body keypoints?" aria-label="Your question">',
    '    <button class="ls100-chat__go" type="submit">Search</button>',
    '  </form>',
    '  <div class="ls100-chat__body" role="status" aria-live="polite"></div>',
    '  <footer class="ls100-chat__foot">Runs in your browser &middot; your question is never sent anywhere</footer>',
    '</section>'
  ].join('\n');
  document.body.appendChild(root);

  var fab = root.querySelector('.ls100-chat__fab');
  var panel = root.querySelector('.ls100-chat__panel');
  var form = root.querySelector('.ls100-chat__form');
  var input = root.querySelector('.ls100-chat__input');
  var body = root.querySelector('.ls100-chat__body');
  var closeBtn = root.querySelector('.ls100-chat__close');

  function say(html, cls) {
    body.innerHTML = '<div class="ls100-chat__msg ' + (cls || '') + '">' + html + '</div>';
  }

  function escapeHtml(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }

  // ------------------------------------------------------------- loading
  // Opening the panel starts the load, and submitting a query needs the same
  // load. Both callers await one shared promise; returning early for the second
  // one would abort the search while the model was still on its way.
  function ensureReady() {
    if (state.ready) return Promise.resolve(true);
    if (!state.pending) {
      state.pending = load().then(function (ok) {
        if (!ok) state.pending = null;   // allow a retry after a failure
        return ok;
      });
    }
    return state.pending;
  }

  async function load() {
    try {
      say('Loading the search model&hellip;<br><small>About 23&nbsp;MB the first time, then cached for future visits.</small>');

      var mod = await import(TRANSFORMERS);
      var pipeline = mod.pipeline;

      // The model weights come from the Hugging Face CDN (free, and cached by
      // the browser after the first visit). Self-hosting them alongside this
      // script was the original plan and is intentionally not used: in
      // transformers.js 4.2.0 the browser build never loads a tokenizer from
      // env.localModelPath - it fails before making any request, leaving a
      // pipeline whose tokenizer is not callable. Remote loading works, so the
      // index and the widget ship from this site and only the weights do not.

      var idxReq = fetch(assets + 'index.json').then(function (r) {
        if (!r.ok) throw new Error('index ' + r.status);
        return r.json();
      });

      var extractor = await pipeline('feature-extraction', MODEL, {
        dtype: DTYPE,
        progress_callback: function (p) {
          if (p && p.status === 'progress' && p.progress) {
            say('Loading the search model&hellip; ' + Math.round(p.progress) + '%' +
                '<br><small>First visit only - it is cached afterwards.</small>');
          }
        }
      });

      var index = await idxReq;

      // Unpack the int8 vectors written by embed_chat_index.mjs.
      var raw = atob(index.vectors);
      var bytes = new Int8Array(raw.length);
      for (var i = 0; i < raw.length; i++) bytes[i] = (raw.charCodeAt(i) << 24) >> 24;
      index.vecs = bytes;

      state.index = index;
      state.embed = extractor;
      state.ready = true;
      return true;
    } catch (err) {
      say('Search could not load.<br><small>' + escapeHtml(err.message || String(err)) +
          '</small>', 'ls100-chat__msg--error');
      return false;
    }
  }

  // -------------------------------------------------------------- search
  async function search(query) {
    if (!(await ensureReady())) return;
    say('Searching&hellip;');

    var out = await state.embed([query], { pooling: 'mean', normalize: true });
    var q = out.data;
    var idx = state.index;
    var D = idx.dim;
    var vecs = idx.vecs;

    var scored = [];
    for (var i = 0; i < idx.count; i++) {
      var dot = 0;
      var base = i * D;
      for (var c = 0; c < D; c++) dot += q[c] * (vecs[base + c] / 127);
      scored.push([dot, i]);
    }
    scored.sort(function (a, b) { return b[0] - a[0]; });

    // Adjacent chunks overlap, so the same section can fill the list. Keep only
    // the best-scoring passage per destination.
    var seen = {};
    var hits = [];
    for (var s = 0; s < scored.length && hits.length < MAX_RESULTS; s++) {
      if (scored[s][0] < MIN_SCORE) break;
      var chunk = idx.chunks[scored[s][1]];
      if (seen[chunk.u]) continue;
      seen[chunk.u] = true;
      hits.push({ score: scored[s][0], c: chunk });
    }

    if (!hits.length) {
      say('Nothing in the course materials matches that closely.' +
          '<br><small>Try naming a tool or concept - "MediaPipe", "mixed-effects model", "spectrogram".</small>');
      return;
    }

    body.innerHTML = hits.map(function (h) {
      var c = h.c;
      var where = escapeHtml(c.t) + (c.s ? ' <span class="ls100-chat__crumb">› ' + escapeHtml(c.s) + '</span>' : '');
      var snippet = c.x.length > 260 ? c.x.slice(0, 260).trim() + '…' : c.x;
      return '<a class="ls100-chat__hit" href="' + siteRoot + escapeHtml(c.u) + '">' +
             '<span class="ls100-chat__kind ls100-chat__kind--' + escapeHtml(c.k) + '">' + escapeHtml(c.k) + '</span>' +
             '<span class="ls100-chat__where">' + where + '</span>' +
             '<span class="ls100-chat__snip">' + escapeHtml(snippet) + '</span>' +
             '</a>';
    }).join('');
  }

  // --------------------------------------------------------------- events
  function open() {
    state.open = true;
    panel.hidden = false;
    fab.setAttribute('aria-expanded', 'true');
    root.classList.add('is-open');
    input.focus();
    ensureReady();   // warm up while the reader is typing
  }
  function close() {
    state.open = false;
    panel.hidden = true;
    fab.setAttribute('aria-expanded', 'false');
    root.classList.remove('is-open');
    fab.focus();
  }

  fab.addEventListener('click', function () { state.open ? close() : open(); });
  closeBtn.addEventListener('click', close);
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var q = input.value.trim();
    if (q) search(q).catch(function (err) {
      say('Something went wrong.<br><small>' + escapeHtml(err.message || String(err)) + '</small>',
          'ls100-chat__msg--error');
    });
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && state.open) close();
  });

  say('Ask a question about the course materials.<br><small>Results are passages from the guides, notebooks, and course documents.</small>');
})();
