---
subtitle: 'LS100 — Module 00A · Research Plans & Proposals'
title: 'Research Methodologies: Converting the Problem to a Research Framework'
short_title: 'Guide 00: Research Framework'
exports:
  - format: pdf
    template: lapreprint-typst
    output: exports/LS100_module-00A_Research_content-00_Guide-00_Converting-the-Problem-to-a-Research-Framework_LastUpdated-20260920.pdf
    id: rg00-pdf
downloads:
  - id: rg00-pdf
    title: Download the article (PDF)
---
*Authored by* **Souvik Mandal, Ph.D.**

*Project Leader & Instructor, Computational Behavioral Sciences, LS100, FAS, Harvard University* | LinkedIn ID: [souvik-mandal-phd](https://www.linkedin.com/in/souvik-mandal-phd)

---

Most research projects do not fail at the analysis stage. They fail much earlier, in the weeks when everything still feels like a good idea — when the question is interesting but not yet answerable, when the behaviour of interest has not been defined precisely enough to be counted, and when nobody has asked what a single row of the final dataset will contain. By the time those problems surface, the data have usually already been collected, and they are often the wrong data.

This guide covers the thinking that happens before you write a proposal or present a plan. It takes you from a vague interest to a **research framework**: a question that can be answered, a behaviour that can be measured, a data model that can be built, and an analysis that can be run. The two companion guides in this module then turn that framework into documents — *Presenting Research Plans and Proposals* covers the talk you give at the start of the semester, and *Writing Research Plans and Proposals* covers the written plan. Neither will help you much until the framework underneath them is sound.

Work through this guide with one candidate project in hand. At each step you will be asked to write something down; by the end you should have a complete, if rough, framework that you can defend, revise, and eventually abandon parts of. Research is iterative, and expect to loop back through these steps more than once — that revision *is* the work, not a sign that you started badly.

## 1. From an interest to a research problem

Every project begins as an interest: dance, birdsong, sleep, crowd behaviour, a sport you play. An interest is a region of the world you find compelling. It is not yet a problem, and the distinction matters more than it first appears.

A **topic** is a region. A **problem** is a tension inside that region — something that does not add up, is not known, cannot currently be measured, or matters practically but has no answer. "Movement in classical dance" is a topic. "Trained and untrained dancers are said to differ in movement efficiency, but efficiency is usually judged by expert eye rather than measured" is a problem. The second one tells you what to do next; the first does not.

Problems usually come from one of a few places. There may be an **anomaly** — something observed that existing explanations do not cover. There may be a **disagreement** between studies, or between what practitioners believe and what has been tested. There may be a **missing measurement**: everyone talks about a phenomenon, but nobody has quantified it. There may be a **missing tool**, where the measurement is possible in principle but nothing exists to do it at scale. Or there may be a **practical need** — a coach, a clinician, or a conservation team who would act differently if they had a number they currently lack.

That fourth and fifth category deserve emphasis in this course. Behavioural science has historically been limited less by ideas than by the difficulty of measuring behaviour rigorously and at scale, and the argument for computational approaches is precisely that automated, vision-based quantification can make behavioural description objective and high-throughput rather than subjective and slow ([@anderson2014]). Building the measurement can be the contribution. You do not always need a novel theory; sometimes you need a number nobody has been able to collect.

:::{tip} Critical Evaluation:
State your problem in one sentence containing the word "but". If the sentence still works with "but" removed, you have a topic, not a problem. "Runners are coached to maintain form when tired, **but** whether form actually degrades measurably over a race has rarely been quantified outside a lab" is a problem.
:::

:::{dropdown} Worksheet Checklist

- [ ] Write your interest in one line, then write the tension inside it in one "but" sentence.

- [ ] Name which kind of problem it is: anomaly, disagreement, missing measurement, missing tool, or practical need.

- [ ] Write one sentence answering "who, other than me, would change what they do if this were answered?"

:::

## 2. From a problem to a researchable question

A problem becomes researchable when it is narrow enough that a specific set of observations could settle it. This is the step where most projects are either saved or quietly doomed, because a question that sounds impressive but cannot come out two ways will consume an entire semester and produce nothing.

The first test is whether the answer is already guaranteed. **Avoid tautological questions** — questions whose answer follows from the definitions involved. (The presentation guide returns to this when you build the talk.) "Does arm kinematics differ across different types of baseball or golf swings?" must be true; the swings are defined by differing in kinematics. No amount of data will produce a different result, so no data are worth collecting. The useful version asks about an empirical unknown: which specific joint angle differs, by how much, and whether that difference predicts something else you care about, like ball speed or injury risk.

The second test is whether the question names its terms concretely enough to be measured. Compare "Does fatigue affect running form?" with "Does sagittal-plane knee flexion at footstrike change between the first and last kilometre of a 5 km run?" The first is a direction of curiosity; the second tells you what to record, what to compute, and what comparison to make. You will rarely arrive at the second version immediately, and you should not try to — write the loose version, then interrogate each word in it until it becomes specific.

A useful discipline for the third test comes from clinical research training, where candidate questions are screened against five criteria captured by the mnemonic **FINER** — feasible, interesting, novel, ethical, and relevant ([@browner2022]). It is a teaching device rather than a validated instrument, but it catches the two most common failures early: questions that are fascinating but impossible with the resources at hand, and questions that are perfectly answerable but whose answer nobody needs. Feasibility in particular is worth testing before you invest effort, not after.

It also helps to know what *kind* of question you are asking, because each kind implies a different design and a different analysis:

| Question type | Form | What it needs |
|---|---|---|
| Descriptive | What does X look like, and how much does it vary? | A defined measure and representative sampling |
| Comparative | Does X differ between groups or conditions? | Defined groups, controlled comparison |
| Relational | Does X vary with Y? | Both measured on the same units |
| Predictive | Can X forecast Y on new data? | Held-out data, an error metric |
| Causal | Does changing X change Y? | Manipulation, or a strong design for confounds |
| Tool-building | Can X be measured reliably at all? | A validation target and a reliability estimate |

Most LS100 projects are descriptive, comparative, relational, or tool-building, and that is entirely appropriate. Causal claims require designs that are usually out of reach in a semester — the common failure is not choosing a modest question, it is choosing a modest design and then writing causal language over it.

:::{tip} Critical Evaluation:
Ask of your question: what result would make the answer "no"? If you cannot describe a plausible dataset that produces a negative or surprising answer, the question is not empirical yet. Then ask the mirror question: if the answer is "yes", does anyone learn anything?
:::

:::{note} **LS100 Task:**
Draft **two primary questions and one backup**, each in the specific form. The backup exists because data collection fails in ways you cannot predict — a camera angle turns out unusable, a model tracks poorly, a site becomes inaccessible — and a project with only one question has no way to absorb that.
:::

:::{dropdown} Worksheet Checklist

- [ ] Write the loose version of your question, then the specific version naming the measure, the comparison, and the population.

- [ ] Classify it using the table above, and note what that type will require of your design.

- [ ] Confirm it is not tautological: describe, in one sentence, the world in which the answer comes out "no".

- [ ] Draft one backup question that uses the same data but survives if your primary measurement fails.

:::

## 3. Defining the behaviour you will actually measure

This is the step that separates a behavioural study from an opinion about behaviour, and it is where this course's central premise does its work. For the purposes of quantification, behaviour is treated as a **temporal sequence of discrete actions** — movements, vocalizations, or other measurable signals — occurring in a given context. Before you can count anything, you have to decide what counts.

The difficulty is that the things we naturally find interesting are almost never directly observable. "Stress", "skill", "engagement", "fatigue", "confidence", and "welfare" are **constructs**: theoretical entities that we infer from things we *can* see. No camera records fatigue. A camera records a body, from which you compute an angle, from which you derive a variability index, which you then argue reflects fatigue. Each of those arrows is a claim, and the chain is only as strong as the argument connecting its ends.

An **operational definition** is the rule that converts the construct into something countable. It must be explicit enough that two people, given the same footage and the same rule, produce the same labels. "The runner looks tired" is not an operational definition. "Knee flexion angle at the instant of footstrike, measured in the sagittal plane, where footstrike is the first frame in which the foot's vertical velocity crosses zero" is. Notice that the second version is testable, mechanical, and — crucially — arguable. Someone can disagree with it on principled grounds, which is exactly what you want.

When your behaviour has multiple categories rather than a single continuous measure, the tool for this is an **ethogram**: a catalogue of defined, mutually exclusive behavioural acts, with the criteria that distinguish each from the others ([@lehner1996]). Good published ethograms decompose what looks like one event into a sequence of discrete observable acts — a wolf's predatory sequence becomes search, approach, watch, attack-group, attack-individual, and so on, each with its own start and end criteria ([@macnulty2007]). There is also a strong argument for borrowing an existing standardized ethogram where one exists for your system, since idiosyncratic per-study catalogues make it impossible to compare your results with anyone else's ([@stanton2015]).

Defining the categories is only half of it. You must also decide **when you look**, and this choice is not a technicality — different sampling rules answer different questions and are not interchangeable. The classic treatment distinguishes recording every occurrence continuously from sampling instantaneously at fixed intervals, and following one focal individual from scanning a whole group ([@altmann1974]). Each yields unbiased estimates only for particular classes of variables: instantaneous scan sampling estimates the *proportion of time* spent in a state reasonably well, but systematically misses brief events, while continuous focal sampling captures event *frequencies* at the cost of how many individuals you can follow.

> **This applies directly to video.** Your frame rate is an instantaneous sampling rule, whether or not you think of it that way. Recording at 30 fps means you are sampling behaviour every 33 ms, and any event shorter than that is invisible to you no matter how good your model is. Choosing a frame rate is therefore a methodological decision made in the framing stage, not a camera setting chosen on the day.

Finally, an operational definition is a claim that must be checked rather than asserted. Two forms of checking matter. **Reliability** asks whether the rule produces the same answer in different hands: have a second person code a subset independently and report agreement, corrected for the agreement you would expect by chance ([@cohen1960]). Be careful interpreting that correction when your behaviour is rare — with heavily skewed base rates, kappa can collapse to near zero even when two coders agree on almost every frame, a paradox worth understanding before you panic at a low value ([@feinstein1990]). With more than two coders, or with ordinal categories, a measure designed to handle those cases is more appropriate ([@hayes2007]). **Validity** asks the harder question of whether the measure means what you say it means; because no single criterion defines a construct, its validity rests on the network of relationships the measure has with other variables, which is why validating a measure and testing a theory are never fully separable ([@cronbach1955]).

If you cannot measure your construct directly, name the **proxy** explicitly, state in one sentence why it is a reasonable stand-in, and state one specific way it could be wrong. A click count standing in for "engagement" fails for the reader who is engrossed and therefore clicking less. Saying so in advance is a strength, not an admission.

:::{tip} Critical Evaluation:
Hand your operational definition to a classmate along with sixty seconds of your footage and no verbal explanation. If their labels differ from yours, the definition is underspecified — and finding that out now costs an afternoon, while finding it out after collection costs the project.
:::

:::{note} **LS100 Task:**
Write your operational definition, then code a two-minute sample twice: once yourself, once by a partner. Report the agreement. If it is poor, revise the definition rather than the labels. The standard practical manual for this whole process is worth consulting as you go ([@bateson2021]).
:::

:::{dropdown} Worksheet Checklist

- [ ] Name your construct, and list every observable thing you are using to infer it.

- [ ] Write an operational definition precise enough for a stranger to apply, including start and end criteria.

- [ ] If you have categories, draft an ethogram table: act name, definition, what distinguishes it from the adjacent act.

- [ ] State your sampling rule — continuous or instantaneous, focal or scan — and justify it from the question.

- [ ] State your frame rate or sampling rate, and the shortest event you therefore *cannot* detect.

- [ ] Plan a reliability check: who double-codes, how much, and what agreement statistic you will report.

- [ ] If using a proxy, write one sentence on why it is reasonable and one on how it could fail.

:::

## 4. From a question to a testable hypothesis

A hypothesis is a specific, falsifiable expectation about what you will observe. A template that works well — and that the presentation guide uses again when you come to build the talk — is **"if [X], then [Y], because [mechanism or logic]"**. The "because" is not decoration — it is what distinguishes a hypothesis from a guess, and it is what tells you which result would be genuinely surprising.

The decisive property is falsifiability. A theory earns scientific standing by forbidding certain outcomes and surviving sincere attempts to refute it, not by accumulating confirmations ([@popper1959]) — so a hypothesis that no possible observation could contradict is not doing scientific work, however plausible it sounds. Write down, before you collect anything, the result that would make you abandon the hypothesis. If you cannot name one, return to Section 2; the problem is upstream, in the question.

It is equally important to name the **rival explanations** early. If knee flexion changes over a 5 km run, fatigue is one explanation; so are pacing strategy, a change in gradient, the runner noticing the camera, or the pose model degrading as lighting changes toward the end of the session. Fields advance fastest when researchers routinely enumerate several competing hypotheses and design observations that *exclude* some of them, rather than gathering more and more support for a single favoured idea ([@platt1964]). A hypothesis is far more informative when it is framed as a choice between explanations that predict different observations.

Two failure modes are worth naming explicitly, because both feel entirely reasonable in the moment. The first is deciding what you were testing after seeing the results and then presenting it as though it had been predicted all along — common, widely disapproved of, and corrosive to the evidential value of the test you report ([@kerr1998]). The second is subtler: the accumulation of small analytic choices — which trials to exclude, where to set a confidence threshold, which of several derived indices to report — each defensible on its own, which together push the false-positive rate far above the nominal five percent and make it possible to find something "significant" in almost any dataset ([@simmons2011]). The protection against both is writing the analysis down before you look, and reporting what you planned alongside what you found. Formally recording those decisions in advance — preregistration — exists precisely to preserve the line between prediction and postdiction ([@nosek2018]).

None of this forbids exploration. Looking at your data, noticing something unexpected, and chasing it is a legitimate and valuable mode of research — much of computational ethology works this way. What matters is labelling honestly which parts of your report were **confirmatory** (planned in advance, tested as planned) and which were **exploratory** (discovered in the data, and therefore a hypothesis for a future study rather than a finding from this one). Reporting exploratory results in confirmatory language is what invalidates the statistics, not the exploration itself ([@wagenmakers2012]).

:::{tip} Critical Evaluation:
For each hypothesis, complete this sentence: "I would conclude I was wrong if I observed ______." If the blank is hard to fill, the hypothesis is not yet testable. If it is easy but the observation is impossible to obtain with your design, the hypothesis is not yet *yours* to test.
:::

:::{dropdown} Worksheet Checklist

- [ ] Write each hypothesis in "if / then / because" form.

- [ ] For each, write the observation that would falsify it.

- [ ] List at least two rival explanations for your predicted result, and note what would distinguish them.

- [ ] Mark each planned analysis as confirmatory or exploratory, and commit to reporting that label.

:::

## 5. Constructing the data model

If you skip one section of this guide, do not let it be this one. The data model is the bridge between a question and a dataset, and it is the step students most often discover they needed only after collecting several hundred gigabytes that cannot answer anything.

The core question is deceptively simple: **what is one row?**

A video of a runner produces tens of thousands of frames. Each frame yields a set of keypoints. From consecutive frames you can derive strides; from strides, per-stride knee angles; from a series of strides, a variability index per kilometre; from those, one summary per runner. Every one of these is a legitimate table, and they are not interchangeable. Your question determines which one is the **unit of analysis** — not your file format, and not whichever table happens to be easiest to produce.

This maps directly onto the progression used throughout this course. **Primary data** are what the sensor recorded: the video file, the audio file, the raw log. **Secondary data** are what a model or transformation extracts: keypoint coordinates per frame, onset times, spectral features. **Tertiary data** are the analysis-ready variables you actually reason about: joint angles, derived indices, per-runner summaries. Knowing which of these your question lives in tells you what to collect, what to compute, and what to keep.

Once you know what a row is, specify the columns. Every variable should have a declared **role** — what you manipulate or compare across (independent), what you measure as the outcome (dependent), what you must account for but do not care about directly (covariate), and what identifies the entity a row belongs to (grouping or ID). That last category is the one most often forgotten and the most costly to omit: without a runner ID and a segment ID on every row, you cannot later account for the fact that rows from the same runner are not independent.

Each variable also has a **measurement scale** — nominal, ordinal, interval, or ratio — and the scale constrains what arithmetic is meaningful ([@stevens1946]). Treat that framework as a useful prompt rather than a law. The classification depends on the question being asked of the data as much as on the data themselves, and the strict prohibitions often taught alongside it (never average ordinal data, for instance) block analyses that are perfectly defensible in context ([@velleman1993]). Know the categories, then think rather than obey.

Aim for a **tidy** structure, where each variable is a column, each observation is a row, and each type of observational unit gets its own table ([@wickham2014]). This is not an aesthetic preference. Tidy tables are what make the rest of your toolchain composable: plotting, grouping, joining, and modelling all assume this shape, and time spent reshaping untidy data is the most common hidden cost in a student project.

> **The error that quietly invalidates behavioural analyses.** Suppose you record eight runners, extract 30,000 frames, and run a test comparing early-race and late-race knee angles with n = 30,000. That number is fiction. You have eight independent units; the frames within a runner are highly correlated with each other, and treating them as independent replicates inflates your degrees of freedom and manufactures significance out of nothing. The classic statement of this problem comes from experimental ecology ([@hurlbert1984]), and although your case is observational rather than experimental, the logic transfers directly — and the false-positive inflation from analyzing clustered data as though it were independent has been quantified explicitly for neuroscience-style datasets ([@aarts2014]). The remedy is not to throw data away: it is to model the nesting, which is exactly what the mixed-effects models in Module 02 are for.

The most useful thing you can do at this stage takes fifteen minutes. **Draw the final table before you collect anything.** Write the column headers. Invent one plausible row and fill in every cell with a fake but realistic value. If you cannot fill a cell, you have found either a variable you forgot to plan for or a measurement you have no way to make — and you have found it while it is still free to fix.

Conventions for naming, versioning, and documenting those files matter too, and the *Writing Research Plans and Proposals* guide covers them in its Data Management section. Two things are worth deciding here rather than there: that your data should end up findable and reusable by someone who is not you ([@wilkinson2016]), and that a written data management plan is treated by major funders as a precondition of the work rather than paperwork produced afterward ([@nih2020]).

:::{tip} Critical Evaluation:
Point at your planned table and ask: "how many independent units does this represent?" If the answer is smaller than the number of rows — and in behavioural data it almost always is — you have nesting, and your analysis must account for it.
:::

:::{note} **LS100 Task:**
Produce a one-page **data model sketch** containing: the unit of analysis in one sentence, the column headers of the final table with each variable's role and scale, one fully invented example row, and a note on which columns are primary, secondary, and tertiary. Bring it to your work-plan presentation; it is usually the slide that generates the most useful feedback.
:::

:::{dropdown} Worksheet Checklist

- [ ] State the unit of analysis in one sentence: "one row is one ______."

- [ ] List every column with its role (independent / dependent / covariate / ID) and its measurement scale.

- [ ] Confirm every row carries the IDs needed to identify the individual, session, and segment it came from.

- [ ] Write one complete invented row with realistic values in every cell.

- [ ] Count your genuinely independent units, and write that number down next to your expected row count.

- [ ] Note which tables are primary, secondary, and tertiary, and what transformation connects each to the next.

:::

## 6. Matching the measurement to the modality

By this point you know what you want to measure. The question now is whether the modality you have chosen can actually capture it, and at what cost in accuracy.

**Video** gives you spatial configuration over time. Markerless pose estimation makes it practical to extract body keypoints from ordinary footage without physical markers, using transfer learning so that a few hundred labelled frames can reach near-human accuracy on user-defined body parts ([@mathis2018]), with newer systems extending this to multiple interacting individuals while maintaining identity ([@pereira2022]). What video gives you well are postures, joint angles, trajectories, distances, and interactions. What it gives you poorly are anything occluded, anything defined by force rather than position, and anything happening faster than your frame rate.

**Audio** gives you the acoustic signal over time — timing, pitch, amplitude, spectral structure. It excels at onsets and rhythm, at vocal or instrumental quality, and at events that are sonically distinct but visually invisible. It struggles in noise, with overlapping sources, and with anything whose meaning depends on spatial context the microphone cannot hear.

**Digital traces** — logs, web activity, platform records, wearable exports — give you large samples cheaply, at the cost of measuring what the platform chose to record rather than what you would have chosen to measure. Here the construct-validity question from Section 3 becomes acute, because the variable arrives pre-defined by someone with different purposes.

Whichever you choose, hold onto one idea: **your model's error becomes your measurement error**. A pose estimator that jitters by a few pixels, drops confidence under occlusion, or swaps left and right limbs is not a neutral instrument. That noise propagates into every angle, every derived index, and every test you run downstream. Plan to quantify it — hold out a small set of hand-labelled frames and report how far the model's keypoints fall from yours — and plan what you will do with low-confidence frames, because deciding that after seeing the results is one of the forking paths described in Section 4. The broader literature on turning raw recordings into behavioural variables is worth reading for exactly this reason: every stage of the pipeline embeds a representational choice ([@pereira2020]), and the field's own call to action is largely about taking these measurement standards seriously ([@datta2019]).

One further argument for video deserves mention: because the raw recording persists, it can be re-coded under a revised definition, re-analysed by someone else, or reused to answer a question you have not thought of yet — which makes it an unusually durable research asset when consent and storage are handled properly ([@gilmore2017]).

The practical mechanics of each pipeline live in the data modules: Module 01A for video, pose estimation, and kinematics; Module 01B for digital audio and acoustic features. Read the relevant introduction before you finalize your framework, because a constraint you discover there — a frame rate, a microphone placement, a model that does not handle your species or setting — may send you back to Section 3.

:::{tip} Critical Evaluation:
Write down the shortest and smallest thing you need to detect: the briefest event, the smallest angle change that would matter. Then check your sampling rate and your model's error against those two numbers. If either is the same order of magnitude as the effect you are hunting, you cannot detect it, and no statistical test will rescue you.
:::

:::{dropdown} Worksheet Checklist

- [ ] Name your modality and state what it captures well and poorly for *your* construct.

- [ ] Record your sampling rate and the shortest detectable event it implies.

- [ ] Plan how you will quantify model error against hand-labelled ground truth.

- [ ] Pre-specify your handling of low-confidence, occluded, or missing measurements.

- [ ] Read the relevant Module 01A or 01B introduction and note any constraint that changes your plan.

:::

## 7. Choosing the analysis before you collect

Deciding how you will analyse the data after collecting it feels efficient and is not. The analysis determines what the data must look like, so choosing it last means discovering, too late, that your design cannot support the comparison you wanted.

Start with a drawing rather than a test. **Sketch the figure that would answer your question** — draw the axes, label them with your actual variables and units, and draw the shape you expect if your hypothesis is right. Then draw the same axes with the shape you would see if it is wrong. Two sketches on paper will tell you more about whether your design works than an hour of reading about statistical tests, and they immediately expose problems: axes you cannot populate, a comparison with only one group on it, an outcome with no variation to explain.

From the sketch, the analysis usually follows. What comparison does the figure imply — two groups, a trend across a continuous predictor, a change across repeated measurements of the same individuals? The *Navigational Guide to Statistical Methods* in Module 02, together with its decision-tree poster, exists to take you from that description to an appropriate test. Note that the answer will very often involve a model that accounts for repeated measurements within individuals, for exactly the nesting reasons set out in Section 5.

This is also the point to think honestly about **how much data you need**, which in behavioural work is usually a question about how many individuals rather than how many frames. Underpowered studies do not merely fail to detect real effects; they also systematically exaggerate the effects they do detect, because only the largest and luckiest estimates clear the significance threshold, which makes the published record less reliable rather than merely sparser ([@button2013]). If a realistic estimate of your available sample cannot plausibly detect an effect of the size you expect, it is better to know that now — and to reframe the project as descriptive or tool-building, which are honest and useful contributions, than to run a comparison doomed to be uninterpretable.

Finally, pre-specify your **decision rules**. What will you do if an assumption is violated, if a runner's footage is partly unusable, if reliability comes out lower than you hoped? Writing these down converts them from judgement calls made under pressure, with the results visible, into methodology. The written form of this belongs in your methodology section, and the *Writing Research Plans and Proposals* guide describes how to present it.

:::{tip} Critical Evaluation:
Show your two sketches — the "hypothesis true" and "hypothesis false" figures — to someone unfamiliar with the project. If they cannot tell you which is which, the figure is not answering the question, and a reader of your final report will be equally lost.
:::

:::{note} **LS100 Task:**
Produce an **analysis map**: a short table with one row per research question, and columns for the measure, the comparison, the planned test or model, the unit of analysis, and the planned figure. Every question should reach a figure; any question that does not is not yet answerable.
:::

:::{dropdown} Worksheet Checklist

- [ ] Draw the planned figure with real axis labels and units, in both the "true" and "false" versions.

- [ ] Write the comparison in words before naming any test.

- [ ] Use the Module 02 guide and decision tree to select a candidate test or model, and note its assumptions.

- [ ] Estimate your realistic number of independent units, and state whether it can detect the effect you expect.

- [ ] Write decision rules for assumption violations, unusable data, and low reliability.

:::

## 8. Scope, feasibility, and what you will not do

A framework that cannot be executed in the time available is not a framework; it is a wish. Scope is therefore part of the methodology, not an administrative afterthought.

Budget realistically. As a rule of thumb, **plan for about a third of your available time to go to data collection**, and expect the first attempt at collection to be partly wasted — the first session usually teaches you that the camera angle was wrong, the lighting fails at the critical moment, or the microphone picks up a fan you never noticed. That pilot is not lost time; it is the only reliable way to discover these things, which is why the course schedules preliminary collection early and expects you to redesign afterward.

Then account for the things that take calendar time rather than working time: gaining access to a site or population, obtaining consent, borrowing equipment, waiting for an ethics determination, and — if you are training a model — labelling data, which almost always takes longer than students estimate.

Choose **one achievable aim** and make it genuinely achievable. A project with one well-executed question and a clean dataset is a better outcome, and a better piece of work to present, than three half-collected ones. If a later aim depends entirely on an earlier one succeeding, say so explicitly and name it as a risk.

Finally, write down what you are **not** doing. Explicit exclusions protect you twice: they keep the project from expanding as interesting tangents appear, and they answer the reviewer or audience member who asks why you did not also measure something else. "We deliberately restricted this to sagittal-plane kinematics because our single-camera setup cannot resolve rotation" is a strong answer. Silence is not.

:::{dropdown} Worksheet Checklist

- [ ] Draw a timeline with collection occupying roughly a third of it, including a pilot session.

- [ ] List every calendar-time dependency: access, consent, equipment, labelling, approvals.

- [ ] Name your one primary aim, and mark any aim that depends on another succeeding.

- [ ] Write three sentences beginning "This study will not…", each with a one-line justification.

:::

## 9. Ethics at the framing stage

Ethics appears late in most project plans and should appear early in your thinking, for a practical reason: framing decisions foreclose ethical options. The moment you decide that answering your question requires recording identifiable faces in a public space, you have committed to a consent and review pathway, a storage regime, and a set of constraints on what you can publish or share. Deciding that at the framing stage is cheap. Discovering it after collection can end a project.

The underlying principles are stable and worth knowing rather than looking up: respect for persons, expressed through informed consent; beneficence, expressed through a real weighing of risks against benefits; and justice, expressed through who bears the burden of the research and who benefits from it ([@belmont1979]).

Two specifics catch students out. The first is the assumption that recording in a public place is automatically exempt from review. The relevant federal provision does cover observation of public behaviour including visual and auditory recording — but the exemption depends on conditions, principally that the identity of the subjects cannot readily be ascertained, or that disclosure would not place them at risk, or that limited review is obtained ([@cfr46104]). Video of identifiable faces frequently fails the first condition, which is precisely why it matters at framing time.

The second is the belief that obscuring eyes anonymizes a person. It does not, and the standard guidance on publishing identifiable material is explicit that identifying information should not be published unless it is scientifically essential and the participant has given written consent for publication ([@icmje]). Plan for consent that covers not just participation but any later sharing or publication of the recordings, because retrofitting that permission is usually impossible.

There is a constructive move available here, and it belongs in the framework rather than the ethics paperwork: **ask whether you can answer the question with less identifying data**. Very often you can. If your analysis operates on joint angles, you may not need to retain the video at all once keypoints are extracted — and a stored table of coordinates carries dramatically less risk than a stored face. Designing the pipeline so that identifiable data has the shortest possible life is both better ethics and less to safeguard.

The full treatment of consent language, review categories, storage, anonymization, access control, and responsible-AI considerations belongs in the *Writing Research Plans and Proposals* guide, which covers it in detail. What belongs here is the decision that shapes everything downstream: what you will record, of whom, and for how long you will keep it.

:::{tip} Critical Evaluation:
Ask: "what is the least identifiable form of data that still answers my question?" If your plan collects something more identifiable than that answer, justify the gap explicitly or close it.
:::

:::{dropdown} Worksheet Checklist

- [ ] State who or what is recorded, whether they are identifiable, and in what setting.

- [ ] Determine what review your project requires, and start that process before collection.

- [ ] Draft consent covering participation, retention, and any later sharing or publication.

- [ ] Write the minimum-identifiability version of your pipeline and note what it would cost you scientifically.

- [ ] Decide the retention period and deletion point for raw identifiable data.

:::

## 10. A worked example, end to end

The steps above are easier to follow when watched working on a single question. Here is one carried through the whole framework.

| Step | Applied to the example |
|---|---|
| **Interest** | Distance running |
| **Problem** | Runners are coached to "hold form" when tired, but whether form measurably degrades over a race has rarely been quantified outside a laboratory |
| **Question** | Does sagittal-plane knee flexion at footstrike change between the first and final kilometre of a self-paced 5 km run in recreational runners? |
| **Construct** | "Running form", narrowed to one component: knee flexion at footstrike |
| **Operational definition** | Knee angle in the sagittal plane at the first frame in which the foot's vertical velocity crosses zero, computed from hip, knee, and ankle keypoints |
| **Hypothesis** | If accumulated fatigue degrades control, then mean knee flexion at footstrike will increase from kilometre 1 to kilometre 5, because reduced eccentric strength lets the knee collapse further under load |
| **Falsifier** | No change, or a decrease, in mean flexion across segments |
| **Rivals** | Pacing strategy; gradient changes; camera-awareness early on; pose-model degradation as light changes |
| **Modality** | Video at 60 fps, fixed tripod, sagittal view; keypoints via a pose estimator |
| **Unit of analysis** | One row per runner per kilometre segment (not per frame, and not per stride) |
| **Data model** | Primary: video. Secondary: per-frame keypoints. Tertiary: per-stride knee angle → mean and variability per runner per segment |
| **Independent units** | Number of runners — not number of strides, and certainly not number of frames |
| **Analysis** | Mixed-effects model with segment as a fixed effect and runner as a random effect; figure shows per-runner trajectories across segments |
| **Scope limits** | Sagittal plane only; single camera; no force or metabolic measurement; recreational runners only |
| **Ethics** | Runners consent to recording; video deleted after keypoint extraction; only coordinate tables retained |

Notice that the interesting decisions are concentrated in the middle rows. The question is ordinary; the analysis is standard. What makes the study workable is the operational definition and the choice of unit — and both were decided before a single frame was recorded.

## 11. The framework worksheet

Before moving on to the presentation or the written plan, you should be able to complete every line below. If a line is blank, that is where your project currently is, and that is what to work on next.

:::{dropdown} Research Framework Worksheet

**The problem**

- [ ] Interest, in one line
- [ ] Problem, in one "but" sentence
- [ ] Who would act differently if this were answered

**The question**

- [ ] Primary question 1, in specific form
- [ ] Primary question 2, in specific form
- [ ] Backup question
- [ ] Question type, and what it demands of the design
- [ ] The world in which the answer is "no"

**The behaviour**

- [ ] Construct named
- [ ] Operational definition, applicable by a stranger
- [ ] Ethogram table, if categorical
- [ ] Sampling rule and justification
- [ ] Sampling rate, and the shortest undetectable event
- [ ] Reliability plan
- [ ] Proxy justification and failure mode, if applicable

**The hypothesis**

- [ ] "If / then / because" for each question
- [ ] Falsifying observation for each
- [ ] Two rival explanations and what distinguishes them
- [ ] Confirmatory vs exploratory labels

**The data model**

- [ ] "One row is one ______"
- [ ] Column list with roles and scales
- [ ] ID columns for individual, session, segment
- [ ] One invented example row
- [ ] Count of independent units
- [ ] Primary → secondary → tertiary chain

**The measurement**

- [ ] Modality, with strengths and limits for this construct
- [ ] Model-error quantification plan
- [ ] Missing and low-confidence data rules

**The analysis**

- [ ] Planned figure, both "true" and "false" versions
- [ ] Comparison in words
- [ ] Candidate test or model, with assumptions
- [ ] Whether the sample can detect the expected effect
- [ ] Decision rules for violations and data loss

**Scope and ethics**

- [ ] Timeline with a pilot and a collection third
- [ ] Calendar-time dependencies
- [ ] Three explicit exclusions
- [ ] Identifiability assessment and review pathway
- [ ] Minimum-identifiability pipeline and retention plan

:::

Once this worksheet is filled, you have a research framework. The next two guides in this module will help you communicate it — first as a short talk that invites feedback while the plan can still change, then as a written proposal. Both of those are easier to write than they look, provided the thinking in this guide has already been done.
