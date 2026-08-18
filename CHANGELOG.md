# Changelog

Corrections and additions recorded against the published record. v0 was minted
2026-07-12, concept DOI `10.5281/zenodo.21325372`, version `21325373`.

⛔ Nothing in the v0 bundle is overwritten. v0.1 files carry their own names and the
2026-07-12 artefacts stand as deposited.

## v0.1, in preparation, 2026-08-13

### C-01 ⛔ WITHDRAWN: the OpenAI source date

v0 recorded `source_date` 2026-01 for the Brockman claim, and `SOURCES.md` carried the note
"Exact event date to firm before mint (Sequoia AI Ascent 2026)". **The flag was never
resolved and v0 shipped with the unfirmed date.**

The talk was published as a Sequoia *Training Data* episode on 1 May 2026, and Sequoia's
AI Ascent runs in spring. 2026-01 is therefore probably wrong by around four months.

✅ **CLOSED 2026-08-13.** Sequoia's own AI Ascent 2026 page, hand-fetched and hashed
(`5ff8a499…f94325ba`), states: "On April 20, we hosted our fourth annual AI Ascent in San
Francisco", and names Brockman among the speakers. The page was published 2026-05-08 and the
podcast released 2026-05-01, both after the event.

⇒ `source_date` corrected from 2026-01 to **2026-04-20**. v0's date was wrong by roughly three
and a half months.

⚠️ Still outstanding on this row: the **quote wording is secondary**. "We went from these agentic
coding tools writing 20% of your code to writing 80% of your code" and the "within December"
detail both come from reporting, not from the talk. The transcript is not held. The December
detail carries weight in the row's scope note and should be verified or dropped.

### C-02 ⛔ WITHDRAWN: "0 of 8 define a rigorous denominator" was already false at mint

v0 carried one Anthropic row conflating Amodei's March 2025 prediction, a spokesperson
range and Krieger's "effectively 100%". The Anthropic Institute paper "When AI builds
itself" states a denominator, and it was **published 4 June 2026, five weeks before v0 was
minted on 12 July 2026.** It was not a later development. It was missed.

⇒ v0's Layer 1 headline, that no claim in the set defines a rigorous denominator, was
incorrect on the day of deposit. The count should have been 1 of 9. This is a correction
against the published record, not a refresh. See C-08.

Verbatim: "As of May 2026, more than 80% of the code we merge into Anthropic's codebase
was authored by Claude." The measured object is lines merged into the production codebase,
which is the metric Redwood Research argued was the right one. The lab states the direction
of its own measurement bias: "our attribution pipeline has gaps, and the lines not attributed
to Claude include auto-generated code and other artifacts that were not hand-written by
humans either."

It also reports "the typical engineer was merging 8x as much code per day as they were in
2024" for Q2 2026, with its own caveat that "Lines of code is an imperfect measure, as it
measures quantity over quality" and that the figure is "almost certainly an overstatement
of the true productivity gain".

⇒ The 2025 prediction is retained as its own row. A new measurement row is added.
`denominator_defined` moves N to Y for the new row. `measured_vs_anecdote` is
`internal_metric`, which under the v0 scoring rule does not score, because it is
self-reported telemetry and no raw data is released.

⚑ This is the largest single improvement in the set and it belongs to the lab that makes
the assisting model. It was checked against the primary and stated conservatively: the row
still fails audit and reproducibility, and better disclosure is consistent with the tier-1
motive already recorded for this lab, which is to sell capability **and** to appear the
responsible party. Improved disclosure quality is not evidence against that motive.

### C-03 ⛔ WITHDRAWN: "0 of 8 isolate the research loop" was also false at mint

v0's reported-not-scored finding was that no claim in the set isolates the research loop.
Two of eleven now do, but **one of those two, OpenAI's Codex post, is dated 5 February 2026,
five months before the mint.** Only the TIME row of 7 August 2026 post-dates it.

⇒ The correct v0 statement was 1 of 9, not 0 of 8. See C-08.

**OpenAI, 5 February 2026**, held locally and hashed. Verbatim: "GPT-5.3-Codex is our first
model that was instrumental in creating itself. The Codex team used early versions to debug
its own training, manage its own deployment, and diagnose test results and evaluations." A
dedicated section, "How we used Codex to train and deploy GPT-5.3-Codex", names monitoring
and debugging the training run, tracking patterns across training, proposing fixes, adapting
the harness, root-causing cache hit rates and scaling GPU clusters during launch.

⭐ **In the same document, the words "self-improvement" and "recursive" appear zero times**
across 20,773 characters of extracted text, while the model is classified as "the first model
we classify as High capability for cybersecurity-related tasks under our Preparedness
Framework". Observation: the lab graded this model against its own framework for one
capability and made a research-loop claim in the same post without grading it against the
framework's self-improvement category.

⛔ Secondary reporting that the model "does not reach High capability on AI self-improvement"
is **not in the primary** and is not carried.

**OpenAI, 7 August 2026**, via TIME: experiments per researcher doubled by July. Research
throughput rather than code share. Base is per-researcher, "experiment" is undefined, no
absolute count given, so `denominator_defined` is partial.

Neither new row scores well. That is the point: the safety-relevant object is now being
asserted without a denominator, an audit or a second source.

### C-04 Google's trajectory extended

v0 recorded ">25% Oct'24 -> >30% Apr'25 -> ~75% later". The 75% figure is now dated to April
2026, up from 50% in late 2025. Scope note added: the human-approval step makes this a
different measure from Microsoft's repository share, so part of the 75-versus-30 gap is
definitional rather than a difference in adoption.

### C-05 Rechecked and unchanged

Microsoft has not refreshed 20-30% since April 2025, though Nadella has said the share climbs
each quarter and some internal repos exceed 50% without giving a new headline figure. Meta
remains a target with no measured figure, and Zuckerberg said he did not know Meta's share
when asked directly. No updated Salesforce figure was located. Amazon and Snap unchanged.

### C-06 Layer 2 additions, pending entry to `triggers.csv`

- **METR, Frontier Risk Report (February to March 2026)**, published 19 May 2026. An
  entity-based pilot assessing risks from internal AI use at Anthropic, Google, Meta and
  OpenAI, with access to internal models, raw chains of thought and non-public information on
  how AI is used internally. ⭐ This is the first independent cross-lab instrument touching the
  research loop, which v0 correctly recorded as not existing at the time. Reported finding:
  companies did not report evidence of dramatic speed-ups attributable to AI R&D automation,
  and Anthropic argued it had not seen a 2x increase in pace as of April 2026.
- **FRONTIER Act**, introduced July 2026: would require periodic confidential reports to the
  Department of Commerce on catastrophic risks from internal use of frontier models, and
  incident reporting within 72 hours including whether an incident involved internal use.
- **Anthropic, "When AI builds itself"**: states "We are not there yet" on recursive
  self-improvement and asks for the option to slow or pause frontier development.

⚠️ Dated sequence worth preserving rather than collapsing: METR reports no dramatic speed-up
as of February to April 2026; OpenAI reports doubled experiments per researcher by July 2026.
Those are compatible in time order. Neither is an audit of the other.

### C-07 The COI statement needs rewriting, not extending

v0's COI names Anthropic as the top number and the maker of the assisting model. v0.1 adds an
OpenAI research-loop row, and the work is now produced with two assistants from two labs, both
of which are graded subjects in the set.

⛔ The disclosure is about **tool provenance**, not co-authorship. The author governs both
models, sets the research question and method, and makes every sourcing and analytical
judgement. The models say nothing; the author does. The existing house line already states
this and it stands: "The research question, method, sourcing decisions and analytical
judgements are the author's. The assisting model is not always a neutral party to the subject
matter."

### C-08 ⛔ The v0 search was not complete at the date of deposit

Dated check, 2026-08-13. Of the three claims added in v0.1, **two were public before v0 was
minted**:

| Claim | Date | v0 minted 2026-07-12 |
|---|---|---|
| OpenAI, "instrumental in creating itself" | 2026-02-05 | 5 months before |
| Anthropic Institute, >80% merged code | 2026-06-04 | 5 weeks before |
| OpenAI, experiments per researcher doubled | 2026-08-07 | after |

⇒ This is a completeness failure in v0, not movement in the field. Two of v0's four headline
counts were wrong at deposit, and both errors ran in the same direction: they made the set
look less checkable than it was. ⚠️ A scorecard that grades others on sourcing discipline
carries a higher duty here, so the correction is recorded in full rather than absorbed into
a refresh.

**Standing method fix:** v0 verified each claim against its primary but never ran a dated
sweep for claims it did not already hold. Both misses were findable by searching the subject
labs for the period between the previous check and the deposit date. ⇒ Any future version
runs a date-bounded sweep per subject immediately before mint, and records the sweep window
in `SOURCES.md` so a reader can see what period was searched.

### C-09 ⭐ The Anthropic Institute piece states its 8x figure two different ways

Found on reading the held primary, 2026-08-13. The same multiplier is attached to two different
units and two different baselines in one document:

> "In the second quarter of 2026, the typical engineer was merging 8x as much code **per day** as
> they were in **2024**."

> "today, Anthropic engineers on average ship 8x as much code **per quarter** as they did from
> **2021-2025**."

Observation: per day against 2024, and per quarter against a 2021-2025 period, cannot both be the
same measurement. Inference: one is a restatement that lost its unit, probably in the summary
framing, but which one is authoritative is not resolvable from the document.

⇒ Quote the first form, which sits with the chart and the footnote. Record the second as an internal
inconsistency. ⚠️ This does not change the row's score, because the 8x figure is context rather than
the graded claim, and the graded claim is the >80% merged-code figure.

⭐ Method note: this is the kind of defect the scorecard exists to find, and it was only visible
because the primary is held locally rather than summarised. It was not present in any secondary
account read earlier.

### C-10 Motive-tier key flipped to the house canonical direction

Coherence debt logged at v0: the scorecard ran tier 1 = strongest incentive, while the canonical
Source Incentive Map runs tier 1 = LEAST incentive. Internally consistent, but inverted against the
rest of the portfolio. AnchorAI had already realigned.

⇒ Flipped in `claims_v0.1.csv` and `sources/source_register.csv`: 1 to 5, 2 to 4, 3 unchanged.
⭐ **Tier 1 now means least incentive.** Independent measurement (METR, the four arXiv papers) sits
at 1; a chief executive on their own company's capability sits at 5.

⚠️ One row is imperfect and is left visible rather than fudged. `sequoia_brockman_ascent` now reads
tier 5, inherited from the claim it supports. The held document is Sequoia's own event page, whose
incentive relates to promoting the conference, and what it supplies is a date rather than a figure.
The tier describes the claim, not the document.

### C-11 Layer 2 rebuilt as `triggers_v0.1.csv`, 5 rows carried forward, 4 added

⛔ `triggers.csv` is unchanged and remains the deposited v0 file.

Added: the METR Frontier Risk Report as an `independent_assessment`; Anthropic's own "We are not
there yet" as a `self_assessment`; OpenAI's Codex claim as an `observed_event` with the explicit
note that it is **not** a red-line crossing; and the FRONTIER Act as a `policy_instrument`, status
only, recorded because it would convert METR's voluntary internal-use disclosure into a duty.

⭐ The register previously held one observed event, AlphaEvolve. It now holds two, and gains its
first independent cross-lab instrument. v0's statement that no such instrument existed was correct
for its evidence at the time and is superseded rather than withdrawn.

### C-12 COI rewritten, `COI_v0.1.md`

⛔ The v0 statement named one lab. Two of the graded parties now supply tools used to make the work.

The correction is one of framing, made by the author on 2026-08-13: the disclosure concerns **tool
provenance**, not co-authorship. The author governs both models, sets the question and method, and
makes every sourcing and analytical judgement. The models hold no view.

The two-assistant cross-read is stated as what it is: a cross-check inside one author's process that
demonstrably finds errors the single reader missed, and ⛔ not independent review, since both
companies are graded here and the author directs both.

### C-13 ⛔ WITHDRAWN: the OpenAI row was never a claim about OpenAI's code

Transcribed locally from the video, faster-whisper large-v3, transcript held and hashed
(`6a52fff6…ecf626ae`). Timestamp 07:32 to 07:41.

The claim is made in answer to how founders should build. Brockman advises them to lean in, then
says agentic tools went from writing 20% of **your** code to writing 80% of **your** code over the
course of December. The subject is the customer's codebase. ⛔ **No figure for OpenAI's own internal
code appears anywhere in the 28-minute talk.**

⇒ v0 grouped this with the "X% of OUR code" self-disclosures from Anthropic, Microsoft, Google and
Meta. It is a different object: a capability claim about a product, addressed to potential users.
`risk_object` corrected to `tool_capability_claim`.

⚠️ v0's paraphrase also firmed up the wording. The actual sentence carries three hedges before the
figure. Quoting the cleaned version would have made the speaker sound more certain than he was.

✅ The "over the course of December" detail is CONFIRMED and can stay.

### C-14 ⭐⭐ Same company, same month, three different figures

New row added: Boris Cherny, Anthropic, at the same event, transcript held and hashed
(`3ec78405…8e77b614ba`).

Within one talk he states, at 05:38 to 06:22, that the Claude Code codebase is at a hundred percent
and that the model reached that point around October or November 2025; and at 18:29 that there is no
more manually written code anywhere at the company, with all the SQL written by models.

⚠️ **Thirty-one seconds before that**, at 17:58, he says they use Opus 4.7 to write **most** of their
code. Most and none-manual are not the same claim.

⭐ **Set against the Anthropic Institute paper, the same organisation has published three different
levels in roughly six weeks:** more than 80% of merged code (formal disclosure, 4 June 2026, stated
denominator), most of our code (20 April 2026), and no manually written code anywhere (20 April
2026, same passage).

Observation: all three are defensible under different definitions of "code" and different scopes.
Inference: that is the scorecard's thesis demonstrated inside a single organisation rather than
across the industry, and it is the strongest evidence in the set that the headline percentages are
definition-dependent rather than measurements of one thing.

⚠️ He also says the model writes a hundred percent of his code while he personally writes a few
dozen pull requests a day, so authorship of a PR and authorship of code are being used differently
in one sentence. Recorded, not resolved.

⛔ This is NOT scored as a second source for the Anthropic Institute row. It is the same party.
Same-party inconsistency is a finding about disclosure quality, not independent verification.

### C-15 Transcripts held

Three AI Ascent 2026 talks transcribed locally on GPU (faster-whisper large-v3, `vad_filter`), no
audio or video uploaded anywhere. Durations match the published runtimes to within nine seconds in
each case, which is what identifies the videos.

⚠️ Machine transcription. Timestamps and wording are good enough to locate and quote a passage, but
any sentence that ends up in the published piece should be checked against the audio, and speaker
attribution is by context since Whisper does not label speakers.

Hassabis is held but unused. It contains a dated AGI-year prediction that would suit the AGI-claims
arm noted in `PROJECT_INDEX.md`, and no automation disclosure.

### C-16 ⭐⭐ The Salesforce figure changes meaning inside the interview

Held transcript, 12:17 to 12:30. The sequence matters and the circulated version collapses it.

Benioff first states a **productivity level**: they are looking at productivity of 30 to 50% this
year in key functions like engineering, coding and support. The interviewer then restates that as
AI **doing** 30 to 50% of the work. Benioff adopts the restatement in his next sentence, giving the
line that has circulated ever since.

Observation: a productivity level and a share of work performed are different quantities. A team
30% more productive has not handed 30% of its work to anything.

Inference: the widely quoted Salesforce claim originated as an interviewer's paraphrase, agreed to
by the speaker rather than asserted by him. ⛔ The row is not rescored, because the speaker did
adopt it and it is his to own. But the scope note now records where the number came from.

⭐ This is the clearest single example in the set of a headline figure whose meaning shifted in
transit, and it was invisible until the primary was held. Every secondary account carries only the
second version.

### C-17 Anchoring: claims are now linked to sources by ID, and the gap is measured

⛔ A structural defect found on 2026-08-13 when the author asked whether all claims were anchored.
They were not, and the paper draft asserted that they were.

v0 and the first v0.1 draft cited sources as free text, so nothing machine-checked whether a graded
claim rested on a document actually held. `reproduce_v0.1.py` verified that each row had a source
*string*, which passes even when the source is a news write-up.

⇒ `claims_v0.1.csv` gains `source_id` and `anchor_status`. `reproduce_v0.1.py` now fails if a row
declares `held_primary` without a matching retrieved row in the register, and prints the anchored
count. **At the point the check was added: 5 of 12.**

Anchored since, all hand-fetched by the author and hash-verified:

| Claim | Primary now held |
|---|---|
| Anthropic 2025 prediction | CFR full official transcript. ⭐ Also recovers the qualifier that secondary reporting drops: the programmer still specifies the conditions, the overall app and the design decisions. |
| Google | Pichai's Cloud Next post, 2026-04-22. ⛔ v0 attributed this to the Q1 2025 earnings call; that was wrong. |
| Amazon | Jassy's own post. All four figures confirmed verbatim. |
| Salesforce | Video transcript. See C-16. |

**Now 9 of 12.** Microsoft, Meta and Snap remain `secondary_reported` pending transcription of the
LlamaCon fireside and the Spiegel interview.

⚠️ Two held sources are auto-generated transcripts rather than official ones, and are marked as such
in the register. They locate and date a claim; they do not settle exact wording.

### C-18 Sources are held but ⛔ NOT deposited, and the script now handles that

⛔ The `sources/` directory does not go to Zenodo. Two independent reasons:

1. Standing rule: a deposit carries the reproducible artefact, not the working trail.
2. Most held sources are third-party copyright (an official transcript, a broadcast interview, a
   news article, a social post, publisher pages, video audio). Bundling them under CC BY 4.0 would
   relicense material the author does not own.

What ships instead: `claims_v0.1.csv`, `triggers_v0.1.csv`, `reproduce_v0.1.py`, the paper, this
changelog, and `sources/source_register.csv`. The register carries a URL, a retrieval date and a
SHA-256 per source, so a reader fetches a source themselves rather than receiving a copy.

**Bug found and fixed the same day.** `reproduce_v0.1.py` exited 1 when source files were absent,
so anyone downloading the deposit would have got an integrity failure caused by the deposit working
as designed. It now detects deposit mode, explains why the files are not present, skips the hash
check and still regenerates every table. Both modes tested: exit 0 with sources present and all 16
verified, exit 0 without them.

⚠️ **Stated limit on the hashes, to be carried in the paper.** Stable files such as the arXiv PDFs
will reproduce their recorded hash for anyone. Browser captures will not, because a capture embeds
session data and timestamps, so saving the same URL tomorrow yields a different value. For those the
hash anchors the author's own chain of custody and proves the held copy is unaltered. ⛔ It is not a
value a reader can independently re-derive, and the piece must not imply that it is.

### C-19 ⭐⭐ The LlamaCon fireside rescopes both rows it anchors. 12 of 12 now anchored.

One held transcript closes the last two unanchored rows, and neither claim survives contact with the
primary unchanged.

**Microsoft: the figure is scoped to "some of our projects".** At 15:29 Nadella puts 20 to 30 percent
of the code inside their repositories, in **some of their projects**, as written by software. ⛔ Every
secondary account drops that qualifier, and so did v0's own scope note, which read as though it
covered all repositories. He also separates a second metric he tracks, an acceptance rate he puts at
"30, 40" and rising, so two different Microsoft numbers are in circulation and only one is the
repository share.

**Meta: the target is about the research loop, not product code.** At 16:15 to 16:31 the bet is stated
in terms of building an AI and machine learning engineer to advance **Llama development itself**,
before the "maybe half the development" line. That is the training and evaluation apparatus.

⇒ `research_loop_isolated` moves N to Y for Meta. **The count goes from 2 of 12 to 3 of 12.** v0
reported this column as empty across the board; on the held evidence it was never empty, and the
third case was sitting in an April 2025 transcript.

⚠️ Meta remains a target rather than a measurement and the original is heavily hedged. At 15:39
Zuckerberg says he does not have the number to hand.

⭐ **The most useful line in the transcript is his own assessment of the metric family this scorecard
grades.** He says a lot of the statistics people cite are effectively of the autocomplete variety.
That is a principal at one of the graded firms describing the genre of number as weakly defined,
which is the scorecard's thesis stated from inside the set.

**Anchoring is now 12 of 12.** Eighteen sources held and hash-verified. ⚠️ Five are machine
transcripts and are marked as such; they locate, date and scope a claim but do not settle exact
wording without a check against audio.

## Outstanding before mint

- Hand-fetch and hash: the Anthropic Institute piece, the METR report PDF, the TIME article.
  Five of six register rows are `registered_not_retrieved`.
- Firm or retire the AI Ascent 2026 event date (C-01).
- Resolve the Anthropic Institute publication date: reporting says 4 June 2026, the fetcher
  returned May 2026, which may be the data date rather than the publication date.
- Enter C-06 into `triggers.csv`.
- Add the second sources: arXiv 2607.07663, ResearchArena, ResearchGym, AIRA_2, the 2606.07462
  suite. AIRA_2 was flagged for this project in the 2026-07-08 paper triage and never folded in.
- Flip the motive-tier key to the house canonical direction (logged coherence debt from v0).
- Concept DOI into `PORTFOLIO.md` and the landing page; the piece still has no repo.
- ⚠️ `SOURCES.md` is still v0-era: it says eight claims, is marked web-verified 2026-07-12, and its
  motive-tier key runs the opposite way to the paper and to `claims_v0.1.csv` (it reads 1 = strongest
  incentive). Rewrite or retire it before mint; it currently contradicts the piece it accompanies.
- ⚠️ The Benioff register row still points at `bloomberg.com`. The held transcript came from the
  video posting, not from Bloomberg's own page, and the address should be the one it was taken from.
- ⚠️ Several items in this list are already done (sources hand-fetched and hashed, the Ascent date
  firmed at C-01). Reconcile the list against the file before mint rather than reading it as current.

### C-20 ⛔ WITHDRAWN same day: the Meta research-loop assertion

C-19 recorded `research_loop_isolated` = Y for Meta, moving the count to 3 of 12. **Withdrawn on
2026-08-13, hours later, at the author's challenge.**

The assertion rested on reading "the development" in "maybe half the development is going to be done
by AI" as carrying over from the preceding clause about Llama development. That reading is available.
So is the reading in which it means Meta's development generally, with the Llama sentence as context
rather than scope. ⛔ Both survive the same recording, so the audio-verification step written for it
was itself misconceived: it asked whether the two were separate, which the transcript already settles
by joining them with "because".

⇒ `research_loop_isolated` = `ambiguous`. The count returns to **2 of 12**, with 1 ambiguous, and the
verifier now reports the ambiguous class separately. Resolving it requires a second Meta source, not a
second listen.

⭐ The general lesson, and it is the same one the jurisdiction pipeline reached independently: when a
claim turns on which of two readings a phrase carries, the correct output is a flag, not a value.
Claude asserted a value here because the reading was plausible and made the finding stronger, which
is the direction its errors run.

### C-21 ⇒ REINSTATED, and the final position: the Meta research-loop row is Y

Third and last move on this row, 2026-08-13. C-19 set it Y, C-20 withdrew it to `ambiguous`, and the
author's reading restores **Y**. His argument is textual and it is stronger than the one it replaces:
the two clauses are joined by "because", and a generic reading of "the development" leaves the
Llama-specific AI and machine learning engineer in the preceding clause unexplained.

⇒ Final position: `research_loop_isolated` = **Y**, count **3 of 12**, with the competing reading
kept in the `scope` field of the claims file and named in the paper, so a reader who takes the phrase
as generic can see exactly which row moves and by how much.

⭐ Worth keeping visible that this row moved three times in one day. The value is defensible; the
stability is not, and that is a property of a claim whose scope its own speaker did not fix.

### C-22 Second-model review, Gemini 3.6, 2026-08-13: what was accepted and what was not

Eight flags. Four accepted, one declined, three already answered in the file. Every flag was checked
against the file itself before being acted on, per the standing rule from the earlier red-team sweeps.

**Accepted.**

⭐ **Inclusion criteria were missing.** The paper disclosed that twelve claims from ten organisations
is not a census but never said how a claim got in. Criteria are now stated at the head of Layer 1.
⛔ The reviewer's proposed wording was not usable: it asked for a declared systematic collection over
a bounded window, which would assert a sweep that was not run. What is stated instead is the truth,
a convenience sample against explicit criteria, with the hash-verified primary as the binding one.

⭐ **The register could not locate a quoted passage.** The three AI Ascent rows shared a single
playlist URL and carried no timestamps, so a reader was handed a playlist and a runtime check. The
register now carries a `quote_anchor` column for all six transcripts and per-video URLs. While fixing
it, two further weak addresses were repaired from the held captures themselves: the Jassy row pointed
at `x.com/ajassy` and now carries the status URL, and the Google row pointed at `blog.google` and now
carries the canonical article URL.

⭐ **The audited and second-source tests were questions, not criteria.** Both now state what earns a
yes, and the live boundary case is named in the paper rather than left implicit: METR's entity pilot
obtained non-public information from four developers, but it collected their own reports rather than
examining the data behind any graded figure, so it makes no row audited and corroborates no specific
percentage. It stays in Layer 2.

⚠️ **The aggregation objection did not survive computation, which is why it is answered rather than
conceded.** The reviewer argued that averaging measurements with targets and predictions makes the
index meaningless and that a forward-looking claim cannot fairly be marked unaudited. Segregating the
table gives 0.50 for the ten current claims and 0.50 for the two forward-looking ones, identical to
the set, and both forward-looking horizons have already elapsed, so the unfair-to-pending-predictions
case has no instance in the data. `reproduce_v0.1.py` now prints both subsets so the invariance is
reproduced rather than asserted.

**Declined.** Splitting Layer 1 into product-code and research-loop sub-tables. The four-tests section
states that grading a general coding claim against a research-loop expectation is a category error;
separate sub-tables would imply the instrument does exactly that. The distinction is already carried
by `risk_object` in the claims file, by the reported-not-scored count, and by its own section.

**Already in the file, no change.** The hash-instability limitation, which the paper states in almost
the reviewer's own words; the transcript-provenance limitation, including the note that attribution
was confirmed against audio where a finding turned on it; and the Anthropic case study, which already
has its own section. ⚠️ The review was written against an earlier draft, which is the ordinary hazard
of a second-model read and a reason to check each flag rather than act on the list.

**Carried to v0.2.** Deterministic web capture, WARC or SingleFile with timestamps stripped, so that
the recorded hashes become values a reader can re-derive rather than integrity checks on a held copy.

⇒ **COI consequence.** The second model on this version is Gemini 3.6, not the OpenAI assistant used
on other projects in this workspace. `COI_v0.1.md` and the paper now name **Alphabet** as the supplier
of the reviewing model, and OpenAI as a graded party holding three rows that supplied no tool here.
The two tool-supplying companies are still both graded subjects, so the disclosure's shape is
unchanged; only the names are corrected.

### C-23 The verification note becomes a section, and a checked slot

His call, 2026-08-13, on noticing the last few pieces all carried one. The note was already slot 8
of Skeleton A but was specified as an unheaded italic paragraph and was checked by nothing.

Measured across the corpus the same day: 12 files carry it as a heading against 6 in the italic form,
and the recent deposits use the heading. ⇒ `## Verification` is now the standard, is required in both
skeletons, and `headingcheck.py` reports the italic form as convertible rather than missing so older
pieces surface without failing. This paper's note is converted in place; its text is unchanged.

⭐ The general point, and it is the third instance today: an element that no tool checks is an element
the next restructure loses. The spec said the note was required and the piece nearly shipped without
the spec ever being able to say so.

### C-24 ⛔ An unbacked claim about other parties' terms, and a paragraph said twice

His catch, 2026-08-13, on the sentence "none is redistributable".

⛔ Nobody read YouTube's or Bloomberg's terms. The piece cannot assert what those parties permit.
What is backed is a statement about this deposit: no redistribution permission was sought, and a
CC BY licence covers the author's own work rather than a third party's, so no copy travels. The
Limitations bullet and both places in `reproduce_v0.1.py` now say that instead.

⭐ **`House style/dupcheck.py` added and wired into `prepublish_check.py` as check 11.** It fires on
a paragraph echo, 65% of the shorter paragraph already present in another or any verbatim run of 15
words, and reports repeated phrases without failing. Thresholds tuned against five deposits: at 12
words it fired on an abstract previewing its own section, which is legitimate.

⇒ It found, in this paper, that the closing paragraph of the method section restated the verification
section with a 15-word run verbatim. That paragraph is now one sentence pointing at the section that
owns the material. Phrase echoes went from 28 to 4, and the 4 that remain are a count restated with
its numbers, a named cross-reference, and the disclosure wording that `coi_template.md` requires in
both places.

⚠️ The same check fires on the published Article 50 snapshot, a 31-word run repeated between its
method and a later section. ⛔ Not a re-mint on its own; it rides the next substantive change.

⚠️ `zenodo_metadata.json` still lists the v0 file set, so the deposit gate never saw this paper.
Update `_files` to the v0.1 artefacts before the mint.

### C-25 The disclosure names Google, drops OpenAI, and the ownership clause becomes `research design`

His calls, 2026-08-13/14, during the final read.

⭐ **Google, not Alphabet.** Every other party in the piece is named as the operating company, so
Alphabet would be the only holding company in the set. The graded row is Google's own claim from
Cloud Next, published on blog.google; Gemini comes from Google DeepMind; the house vendor list keys
on Google. ⚠️ The deposit had briefly carried both names, the paper saying Alphabet and the three
companion files saying Google.

⛔ **OpenAI is out of the disclosure entirely.** It supplied no tool used in this version, so it is
not a conflict. It holds three graded rows, which the tables carry and the COI does not.

⭐ **`research design` replaces `research question` in the ownership clause, and is now the house
standard**, recorded in `coi_template.md` with `apply_coi.py` writing it by default. His reasoning:
the work is produced through an agent stack, and what he authors across it is the design, which
agents run against which sources under which gates. `prepublish_check.py` accepts either word, since
twenty published deposits carry the old one. ⛔ Do not bulk-apply to those.

⇒ PDF re-rendered twice. 8 pages, no literal asterisks, `reproduce_v0.1.py` exits 0,
`prepublish_check.py` passes.

### C-26 The cross-read arrangement comes out of the disclosure entirely

His call, 2026-08-14, on reading `COI_v0.1.md`.

⛔ **The yield paragraph was internal workflow.** Which reader found which correction, and that C-08
surfaced from his own challenge rather than from either model, is process. A public deposit carries
the artefact, not the trail. It stays in this changelog, which does not ship.

⛔ **The "it is not independent review" paragraph is withdrawn too, on his objection**, and the
objection is the stronger of the two: the paragraph asserted a quality control without saying what
control was claimed, and disclaimed an obligation without saying who owed it to whom. It answered a
charge nobody had made.

⇒ Removed from `COI_v0.1.md` (both paragraphs) and from the paper's COI (the "cross-check within one
author's process, not external review" sentence). The "cross-lab blindspot checks" clause is out of
`README.md`, `SOURCES.md` and `CORRECTIONS_v0_to_v0.1.md`, leaving "explicit instructions and
internal red-teaming". ⚠️ That clause is in the canonical Variant A in `coi_template.md`; it is not
one of the eight patterns `prepublish_check.py` requires, so removing it passes, but this deposit now
differs from the template on that line.

⚠️ The METR "independent cross-lab instrument" rows in Layer 2 are a different subject and stay.

⇒ Re-rendered. 8 pages, no literal asterisks, reproduce exits 0, prepublish passes.
