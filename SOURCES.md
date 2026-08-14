# Sources - AI Research-Automation Scorecard

Version 0.1, 13 August 2026. How to read `source_register.csv`, which replaces the prose
source list this file carried at version 0.

AI disclosure: the research is the author's; this text was drafted with AI assistance and
reviewed by the author. The model, and the conflict it creates, are named in the Conflict
of interest and scope section.

## Why the register rather than a list

At version 0 this file was the source record, written out by hand per claim. It drifted
from the data it described, and nothing could detect that. The record is now
`source_register.csv`, which `reproduce_v0.1.py` reads and fails on, so a claim that cites
a source the register does not hold stops the script rather than sitting unnoticed in
prose.

## The columns

    source_id          the token a claim row cites in claims_v0.1.csv
    party              whose document it is
    document           its title
    source_role        primary, subject's own claim, second source, or context
    motive_tier        1 to 5, see below
    url                where it lives
    local_path         where the author's copy sits, not shipped
    sha256             hash of that copy
    retrieval_status   retrieved, or not
    accessed_date      when
    quote_anchor       for the six transcripts, the timestamp of the quoted words
    notes              what the source settles, and what it does not

## Motive tier

1 is the least incentive for a number to look high, 5 the strongest, matching the house
source-incentive scale. An executive speaking about their own company's capability on
stage is a 5. An institutional post or a formal paper from the same company is a 3.
Independent or adversarial measurement is a 1, and those are second sources, never the
claim itself.

Version 0's key ran the other way, 1 for the strongest incentive. Any tier read from the
v0 deposit must be inverted before it is compared with this one.

## The six transcripts

Five were produced locally with Whisper large-v3 from publicly posted video; one is an
auto-generated transcript taken from a video page. None is redistributed here, so each row
carries the address of the recording and the timestamp at which the words occur.
`reproduce_v0.1.py` prints that list. A reader checks a transcript-anchored claim at the
recording rather than against the author's transcript of it, which needs no file from this
deposit.

Machine transcription is not neutral on detail. The register notes where it renders SQL as
"sequel" and Llama as "Lama", so a reader comparing a quotation with the audio is not
surprised by it.

## Second sources

Redwood Research put company-wide merged lines at Anthropic nearer 50 than 90 per cent and
found the answer swings on definition. METR's July 2025 randomised controlled trial found
experienced developers 19 per cent slower with frontier tools while believing themselves 20
per cent faster. A 2025 study in Science puts AI-written US GitHub Python functions at
roughly 29 per cent. All three come from those parties' own published accounts and none was
re-derived here.

METR's entity-based pilot of February to April 2026 sits on the boundary between an audit
and a second source and is scored as neither. It obtained non-public information from four
frontier developers, but it collected what those firms reported about their own internal use
rather than examining the data behind any graded figure. It is recorded in Layer 2.

*Verification: every row in `source_register.csv` was retrieved by the author and hashed on
the date the row records. Twelve of the eighteen are official text or the subject's own
writing; six are transcripts, labelled as machine or auto transcripts in the register. The
motive tier is the author's judgement against the house scale, not a measurement, and is
identified as such rather than presented as one. The second-source findings above are quoted
from those parties' published accounts and were not re-derived here.*

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
