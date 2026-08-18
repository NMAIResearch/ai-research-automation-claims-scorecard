# The AI Automation Claims Scorecard

Version 0.1.1, 18 August 2026. NM AI Research.

A motive-neutral referee for the claims frontier AI labs and large adopters make about
how much of their code an AI now writes, and for the recursion red-lines those labs set
in their own safety frameworks. It grades the claims, not the capability.

AI disclosure: the research is the author's; this text was drafted with AI assistance and
reviewed by the author. The model, and the conflict it creates, are named in the Conflict
of interest and scope section.

## What ships

    AI_Research_Automation_Scorecard_v0.1_2026-08-13.pdf   the paper
    claims_v0.1.csv                                        Layer 1, twelve graded claims
    triggers_v0.1.csv                                      Layer 2, twelve register rows
    source_register.csv                                    eighteen sources, hashed
    reproduce_v0.1.py                                      regenerates every table
    SOURCES.md                                             how to read the register
    CORRECTIONS_v0_to_v0.1.md                              what changed since version 0
    README.md                                              this file

## Run

    python3 reproduce_v0.1.py

Python 3 standard library only, no dependencies, no network. It verifies every held source
against its recorded SHA-256, checks that each claim citing a primary has one in the
register, regenerates every table and count in the paper, and exits non-zero on any
integrity failure. Run from this deposit, where the source files are absent by design, it
says why, skips the hash check and still regenerates every table.

## The two objects, kept apart

Coding automation is AI writing product code. It is broad, it is measured externally well
below the labs' own figures, and it is a labour-productivity story.

Recursion in the research loop is AI writing the training and evaluation apparatus that
grows the next model. It is narrow, concentrated, and it is the object the labs' own
frontier-safety frameworks are written about.

"AI writes the code" is not "AI writes the model". Weights are grown by an optimiser over
data rather than authored, the recursion bites on the training apparatus rather than on
the weights, and there is no continuous self across versions. A prior model builds the
tooling that trains the next.

## What the four columns grade

Each is a yes-or-no test that applies to any public statistic. The score is an unweighted
sum out of four, a convenience index rather than a validated metric; the counts are the
finding.

- `denominator_defined` - is it stated what the percentage is of? Y for an exact base such
  as lines merged, partial for a bounded class such as "new code", N for no stated base.
- `measured_vs_anecdote` - `audited` scores; `internal_metric`, `exec_estimate` and
  `prediction` do not.
- `reproducible` - could an outsider re-derive it from disclosed data?
- `second_source` - has a named party with no stake in the number corroborated that firm's
  specific figure?

Recorded and not scored: `research_loop_isolated`, because a public statement about
general coding automation has no duty to break out an internal research-loop share and
grading it against that would be a category error. Also `claim_type`, `risk_object` and
`motive_tier`, which runs from 1 for the least incentive to 5 for the strongest.

## The finding

Across the twelve claims: 1 defines a rigorous denominator with a further 6 partial, 0 are
externally audited, 0 are externally reproducible, and 2 carry an independent check of the
specific figure. Two are targets or predictions rather than current measurements. The
unweighted index averages 0.50 out of 4, and it is the same 0.50 for the ten current claims
and the two forward-looking ones taken separately, so the mixture is not what produces it.

Separately, and not scored, 3 of the 12 isolate the research-loop subset. Version 0
reported that column as empty across the board; on the held evidence it was never empty.

Headline percentages run from roughly a fifth to all of it. Checkability does not follow
them. Four claims read differently in their primary source than in general circulation,
and in each case the source is narrower.

## Layer 2, the register

Twelve rows: four red lines, two observed events, one independent assessment, one
self-assessment, one policy instrument and three timeline claims. No lab reports its
recursion red-line crossed. The register now carries an independent cross-lab instrument,
METR's entity-based pilot of February to April 2026, and its one bounded observed event
remains AlphaEvolve.

## Limitations

The paper's Limitations section is the full list, with the reasoning for each. The four that
change what a reader can do with this deposit:

- **It grades claims, not ground truth.** Every input is self-reported and no lab shares raw
  telemetry. Disclosure quality is the object being measured, not a reduced version of one.
- **The denominators are incompatible**, so the spread is reported rather than resolved into a
  single comparable number. Lines merged and new code approved by engineers are not one measure.
- **The set is a convenience sample against stated criteria**, twelve claims from ten
  organisations. A claim absent from it is not a claim that does not exist.
- **The source files are not deposited and the hashes do not all reproduce.** Stable files such
  as the arXiv papers will; browser captures will not, because a capture embeds session data and
  timestamps. For those the hash shows the held copy is unaltered rather than offering a value a
  reader can re-derive, and the register carries an address and a date so a source is fetched
  directly.

*Verification: all twelve claims are traced to a primary document held locally and
hash-verified, listed with address, retrieval date and SHA-256 in `source_register.csv`,
and, for the six transcripts, with the timestamp range at which the quoted words occur.
`reproduce_v0.1.py` fails if a claim cites a primary the register does not hold. Twelve of
the eighteen sources are official text or the subject's own writing; five are transcripts
generated locally with Whisper large-v3 from publicly posted video; one is an auto-generated
transcript taken from a video page. The four column scores are derived from `claims_v0.1.csv`
by the stated rule and are not reported by any source; the index out of four is an unweighted
sum offered as a convenience measure and is identified as such rather than presented as a
measurement. The comparisons attributed to Redwood Research, to METR's July 2025 trial and to
the 2025 Science study come from those parties' own published accounts and were not re-derived
here. No figure in this deposit is a measurement of automation: every percentage is a claim
made by the named party.*

## Conflict of interest and scope

The research design, method, sourcing decisions and analytical judgements are
the author's. Models from Anthropic and Google assisted with data retrieval, calculation,
literature search and drafting, so this text was artificially generated and was reviewed by
the author before publication. The assisting model is not always a neutral party
to the subject matter, and here all three vendors are relevant: Anthropic holds the
highest-scoring row in the set and is named by Snap as the vendor behind its own figure,
Google holds a row of its own, and OpenAI is a graded party whose model assisted with
this pre-publication red-team review. The OpenAI review is therefore not independent on
OpenAI rows.

Guarantee: every measured claim is traced to the primary document named in the
Verification note, and reproduce_v0.1.py regenerates every table from claims_v0.1.csv and
triggers_v0.1.csv. Modelled or estimated inputs are identified as such in the Verification
note rather than presented as measurements. A reader can check this without trusting
either party.

What the author cannot guarantee: a language model's output can be wrong in ways
that survive review. In prose the error is locally plausible and consistent in
tone with what surrounds it; in code it simply runs, and a wrong constant or a
mis-set filter still returns a clean number. Several methods have been deployed to
mitigate this, including explicit instructions, internal red-teaming and
cross-lab blindspot checks, but the author does not claim the review is
exhaustive. Corrections are logged against the DOI when surfaced.

No warranty is offered beyond the terms of the CC BY 4.0 licence. Independent
analysis and open-science documentation only, not investment advice.

## Version history

**v0.1, 13 August 2026.** The set grows from eight claims to twelve. Every claim is
anchored to a held, hash-verified primary, which is new. Timeline claims are added to
Layer 2. Three counts that were wrong at the version 0 deposit are corrected. Full
register in `CORRECTIONS_v0_to_v0.1.md`.

**v0, 12 July 2026.** First deposit. Eight claims, the Layer 2 register, no source hashing.
