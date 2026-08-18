# The AI Automation Claims Scorecard

*A motive-neutral referee for self-reported vendor figures and stated safety red-lines. Version 0.1.1. NM AI Research, 18 August 2026.*

AI disclosure: the research is the author's; this text was drafted with AI assistance and reviewed by the author. The model, and the conflict it creates, are named in the Conflict of interest and scope section.

## Summary

Frontier AI labs and large adopters increasingly put a number on how much of their code an AI now writes, from roughly a fifth to all of it. This note does not dispute the numbers. It grades their checkability. Twelve public claims are scored on four evidentiary tests that apply to any public statistic: whether the denominator is defined, whether the figure is externally audited, whether an outsider could reproduce it, and whether an independent source has checked it. Across the twelve, one defines a rigorous denominator, none is externally audited, none is externally reproducible, and two carry an independent check of the specific figure. Every claim is traced to a primary document held and hash-verified. Read from source, several of the circulating figures prove narrower than the versions in general use, such as one that changes meaning inside the interview it comes from, one scoped to some projects rather than all repositories, one about the listener's codebase rather than the speaker's company. A separate observation, deliberately not scored, is that three of the twelve isolate the research-loop subset, the training and evaluation apparatus that safety frameworks are written about. A second layer records the labs' own stated red-lines and, new in this version, their stated arrival dates. No lab reports its red-line crossed. The contribution is the referee, not a new benchmark.

## Two objects

The headline claims fuse two things that carry very different weight.

The first is coding automation: AI writing product code. This is broad, measured externally well below the labs' own figures, and it is a labour-productivity story.

The second is recursion in the research loop: AI writing the training and evaluation apparatus that grows the next model. This is narrow, concentrated, and it is the object the labs' own frontier-safety frameworks are written about.

The distinction to hold: "AI writes the code" is not "AI writes the model." Weights are grown by an optimiser over data, not authored. The recursion bites on the training apparatus, not on the weights, and there is no continuous self across versions. A prior model builds the tooling that trains the next.

## The four tests

Each claim is scored on the same four tests. The score is an unweighted sum out of four and is a convenience summary only. The individual yes-or-no counts are the output that carries the argument, and a reader can check each one.

- **Denominator defined.** Does the number state what it is a percentage of? Lines merged, commits authored, characters typed and "any code that was at all useful" are not the same measure. A claim earns yes for an exact base, partial for a bounded class such as "new code" or "code reviews," and no for no stated base.
- **Externally audited.** Has a party outside the firm examined the data behind the figure and published a finding on it? A formal attestation, or a third-party report against a stated verification standard, earns yes. An executive estimate, an internal telemetry figure or an anecdote earns no, however precise the number.
- **Reproducible.** Could an outsider re-derive it from disclosed data?
- **Second source.** Has a named party with no stake in the number corroborated that firm's specific figure? Corroboration of the figure itself earns yes. A parallel estimate of the same quantity at a different scope, or a general finding about industry practice, does not, and is reported in the text instead.

One case sits on the boundary between those last two and is scored as neither. METR's entity-based pilot obtained non-public information from four frontier developers, including access to internal models, which is more access than any outside party has had. It collected what those firms reported about their own internal use rather than examining the data behind any figure graded here, so it makes no row audited, and it corroborates no specific percentage, so it makes no row second-sourced. It is recorded in Layer 2.

A fifth property, whether the claim isolates the research-loop subset, is recorded but deliberately not scored. A public statement about general coding automation has no obligation to break out an internal research-loop share, so grading it against that would be a category error. It is reported as context and as the bridge to Layer 2.

Two further fields are recorded and not scored. Claim type separates a measurement from an assertion, a target and a prediction. Motive tier runs from 1 for the least incentive to 5 for the strongest, aligned with the house source-incentive scale.

Each claim carries the identifier of its primary, and the Verification section states what that anchoring guarantees.

## Layer 1: the twelve claims

A claim enters the set if it is public and on the record, if it comes from a named executive or an official company document, if it puts a number on the share of code or of research work done by AI at a named organisation, and if a primary document can be obtained and hash-verified. The last condition is the binding one. The set was assembled by targeted search rather than by census, so it is a convenience sample against stated criteria and not a sweep of the field. Where an organisation has said several things, one row is scored per distinct claim, and superseded statements are recorded in the scope field of the claims file. Each subject was searched again before this version was cut, which is what surfaced two claims that were already public when version 0 was deposited.

| Lab | Date | Type | Tier | Score | Claim |
|---|---|---|---|---|---|
| Anthropic | 2026-06-04 | measurement | 3 | 2.0 | More than 80% of merged code authored by Claude |
| Anthropic | 2025-03-10 | prediction | 5 | 1.0 | AI writes ≈90% of code, essentially all within a year |
| Microsoft | 2025-04-29 | measurement | 4 | 0.5 | 20 to 30% of repository code, in some projects |
| Google | 2026-04-22 | measurement | 4 | 0.5 | 75% of new code, approved by engineers |
| Amazon | 2024-08-22 | measurement | 5 | 0.5 | 79% of AI code reviews shipped unchanged |
| Snap | 2026-04 | measurement | 5 | 0.5 | More than two thirds of new code |
| Anthropic | 2026-04-20 | assertion | 5 | 0.5 | 100% of the Claude Code codebase |
| OpenAI | 2026-08-07 | measurement | 5 | 0.5 | Experiments per researcher doubled |
| OpenAI | 2026-02-05 | assertion | 3 | 0.0 | Model instrumental in creating itself |
| OpenAI | 2026-04-20 | assertion | 5 | 0.0 | Agentic tools went from 20% to 80% of your code |
| Meta | 2025-04-29 | target | 5 | 0.0 | Target: about half of Llama development |
| Salesforce | 2025-06-26 | assertion | 5 | 0.0 | AI does 30 to 50% of the work |

The aggregate, reproduced by the accompanying script: 1 of 12 defines a rigorous denominator, with a further 6 partial; 0 of 12 are externally audited; 0 of 12 are externally reproducible; 2 of 12 carry an independent check of the specific figure. Two of 12 are targets or predictions rather than current measurements. Separately, and not scored, 3 of 12 isolate the research-loop subset. The unweighted convenience index averages 0.50 out of 4; the counts, not the index, are the finding. Averaging a measurement together with a target is a fair objection to any such index, so the script prints the subsets: the ten current claims average 0.50 and the two forward-looking ones average 0.50, the same as the whole set. Neither forward-looking row is pending, since both horizons have elapsed, so nothing here is marked unaudited for the reason that it is about the future.

The headline percentages span that whole range. Checkability does not follow them, and the two hardest tests are unmet across a claim set spanning almost two years.

Four of the claims read differently in their primary source than in general circulation, and in each case the source is narrower.

**Salesforce's figure is reshaped mid-interview.** Benioff first states a productivity level, saying they are looking at productivity of 30 to 50 percent this year in key functions including engineering, coding and support. The interviewer restates that as AI doing 30 to 50 percent of the work. Benioff adopts the restatement in his next sentence, and that is the version that has circulated since. A team 30 percent more productive has not handed 30 percent of its work to anything. The claim is his, since he agreed to it, but its origin is a paraphrase.

**Microsoft's figure is scoped to some projects.** The 20 to 30 percent covers code in their repositories in some of their projects, not across all of them. Nadella separately tracks an acceptance rate he places at 30 to 40, rising. Two Microsoft numbers are therefore in circulation, of which only one is the repository share. He also notes the split by language, with Python strong and C++ weak, and that agentic coding is highest on greenfield work while little of their work is greenfield.

**The OpenAI conference claim is not about OpenAI.** Asked how founders should build, Brockman says agentic tools went from writing 20 percent of your code to 80 percent of your code over the course of December. The subject is the listener's codebase. No figure for OpenAI's own internal code appears anywhere in the talk, which makes this a claim about a product's capability rather than a disclosure about the speaker's company.

**Amodei's prediction carries a qualifier that is usually dropped.** Immediately after the 90 percent figure he says the programmer still specifies the conditions of the work, the overall application being built and the design decisions.

One line from a graded party describes the genre. Asked at the same event for Meta's figure, Zuckerberg says he does not have the number to hand, and that many of the statistics people cite are effectively of the autocomplete variety.

Construct-level checks sit well below the headline figures. Redwood Research put company-wide merged lines at Anthropic nearer 50 than 90 percent and found the answer swings on definition. METR's July 2025 randomised controlled trial found experienced developers 19 percent slower with frontier tools while believing themselves 20 percent faster. A 2025 study in Science puts AI-written US GitHub Python functions at roughly 29 percent.

## One organisation, three levels in six weeks

The clearest evidence that these figures are definition-dependent comes from comparing a single company with itself rather than with its competitors.

Anthropic carries the best-specified disclosure in the set. Its June 2026 Institute paper states the denominator explicitly, reporting that as of May 2026 more than 80 percent of the code merged into its codebase was authored by Claude, and it states the direction of its own measurement bias, noting that the attribution pipeline has gaps and that unattributed lines include auto-generated artefacts. That earns the only full mark for definition here.

Six weeks earlier, at a public conference, an Anthropic engineer said in one talk that the Claude Code codebase is at a hundred percent, that this had been so since around October or November 2025, and that there is no manually written code anywhere at the company, with all SQL written by models. Thirty-one seconds before that last statement, in the same answer, he said they use Opus 4.7 to write most of their code.

So within roughly six weeks the same organisation has three levels on the public record: more than 80 percent of merged code, most of our code, and no manually written code anywhere. All three are defensible under different definitions and scopes, and none contradicts the others once the scope is fixed, which is the point. Comparing Microsoft with Google invites the objection that two firms simply measure different things. This is the same instability with that objection removed, at the company that specifies its measure most carefully.

## The research-loop subset

Three of the twelve claims bear on the training and evaluation apparatus rather than on product code.

Meta's April 2025 target is stated in terms of building an AI and machine learning engineer to advance Llama development itself. The figure follows as the reason for that focus. Read that way it isolates the research loop. A reader taking "the development" as generic would score the row otherwise, and the data records both readings.

OpenAI's February 2026 launch post states that the model was the first instrumental in creating itself. It says the team used early versions to debug its own training, to manage its own deployment, as well as to diagnose test results and evaluations. A dedicated section names monitoring and debugging the training run, adapting the harness and scaling clusters at launch. The claim scores zero. There is no percentage, no base, no count, while the post itself says the uses are difficult to fully enumerate.

One negative in that document is precise and checkable. The words "self-improvement" and "recursive" do not appear in it, while the same post classifies the model as the first the company rates at High capability for cybersecurity under its Preparedness Framework. The lab graded the model formally against its own framework for one capability, made a research-loop claim in the same document, and made no self-improvement classification.

OpenAI's August 2026 figure is throughput rather than code share: experiments per researcher doubled by July 2026. The base is per researcher, but "experiment" is undefined and no absolute count is given.

## Layer 2: the register

Twelve rows: four red lines, two observed events, one independent assessment, one self-assessment, one policy instrument and three timeline claims. No lab reports its recursion red-line crossed.

The register now carries an independent cross-lab instrument. METR ran an entity-based pilot from February to April 2026, assessing risks from AI agents used inside frontier developers. Four firms took part: Anthropic, Google, Meta, OpenAI. Each supplied access to internal models, to raw chains of thought, as well as to non-public information on how AI is used internally and on the pace of progress. Companies did not report evidence of dramatic speed-ups attributable to AI research automation, and Anthropic argued it had not seen a doubling as of April 2026.

Two observed events are recorded. AlphaEvolve remains the bounded case, a Gemini-powered agent that optimised a kernel used to train Gemini for roughly a 1 percent end-to-end training saving. OpenAI's Codex claim is the second, recorded as an event and explicitly not as a red-line crossing.

The FRONTIER Act, introduced in July 2026, is recorded on status only. It would require frontier developers to report periodically to the Department of Commerce on catastrophic risks arising from internal use, converting the disclosure METR piloted voluntarily into a duty.

Timeline claims are new in this version. A self-declared arrival date is the same kind of object as a self-declared threshold, so it belongs in this register rather than in a separate instrument. Amodei's code-share prediction is the only one whose horizon has elapsed, and it is checkable because the same organisation later published a figure on the same subject. Hassabis gives 2030 for AGI. OpenAI states an intern-level research assistant by September 2026 and a fully automated researcher by March 2028. What the timeline rows show is a gap rather than a date: none of the pending claims carries a definition of what would count as arrival, or a test by which it would be recognised.

One dated sequence is worth preserving rather than collapsing. METR reports no dramatic speed-up as of February to April 2026, and OpenAI reports doubled experiments per researcher by July 2026. Those are compatible in time order, and neither is an audit of the other.

## Prior art

This is a claims referee, not a capability benchmark. Existing benchmarks, including the RE-Bench family, MLE-bench and PaperBench, measure what AI research agents can do on curated ground-truth tasks, and newer suites extend that to closed-loop research work. Chan and colleagues' "Measuring AI R&D Automation" sets out a measurement agenda for research automation and calls for third parties to track it. This scorecard is the narrowed complement to that agenda: it grades the disclosures that already exist against those criteria, then dates the labs' own red-lines as well as their stated arrival dates.

Corrections to version 0, including three counts that were wrong at the date of deposit, are recorded in full in the accompanying changelog.

## Limitations

- **This grades claims, not ground truth.** Every input is self-reported and no lab shares raw telemetry. Measuring disclosure quality is the honest framing, not a limitation smuggled in.
- **The denominators are incompatible.** Written by software, new code approved by engineers, lines merged, and involved in are not the same measure. The spread is reported rather than resolved into a single comparable number.
- **The set is twelve claims from ten organisations.** It is not a census, and a claim absent from the set is not a claim that does not exist.
- **Six of the eighteen sources are transcripts rather than published text**, as the Verification section sets out. They locate, date and scope a claim reliably. Speaker attribution was confirmed against the audio where a finding turned on it, and the remaining transcripts have a single interviewee.
- **Source files are not deposited.** They are third-party material and this deposit's licence covers the author's own work, not theirs, so no copy is redistributed. The register carries an address, a retrieval date and a hash for each, so a reader fetches a source directly rather than receiving a copy.
- **The hashes do not all reproduce for a reader.** Stable files such as the arXiv papers will. Browser captures will not, because a capture embeds session data and timestamps, so the same address saved later yields a different value. For those the hash shows the held copy is unaltered rather than offering a value a reader can re-derive.
- **This is not a forecast of a crossing.** The framed risk is pacing, capability outrunning safety work. The register is descriptive and dated.

## Reproduction

    python3 reproduce_v0.1.py

Standard library only, no network. It verifies every held source against its recorded hash, checks that each claim citing a primary has one in the register, regenerates every table and count above, and exits non-zero on any integrity failure. Run from the deposit, where the source files are absent by design, it reports why, skips the hash check and still regenerates every table.

Six of the eighteen sources are transcripts and none is redistributed here, so the script prints, for each one, the address of the recording and the timestamp at which the words occur. A transcript-anchored claim is therefore checked at the recording itself rather than against the author's transcript of it, and that check needs no file from this deposit.

## Verification

All twelve claims are traced to a primary document held locally and hash-verified, listed with address, retrieval date and SHA-256 in the source register, which is the trace, and, for the six transcripts, with the timestamp range at which the quoted words occur; the reproduction script fails if a claim cites a primary the register does not hold. Twelve of the eighteen sources are official text or the subject's own writing, comprising company posts, an official conference transcript published by the host, a social post, an event page, four arXiv papers and the METR report. Five are transcripts generated locally with Whisper large-v3 from publicly posted video. One is an auto-generated transcript taken from a video page rather than produced here. All six are labelled as machine or auto transcripts in the register. The four column scores are derived from the claims file by the stated rule and are not reported by any source; the index out of four is an unweighted sum offered as a convenience measure. The comparisons attributed to Redwood Research, to METR's July 2025 trial, as well as to the 2025 Science study, come from those parties' own published accounts. None was re-derived here. No figure in this piece is a measurement of automation: every percentage is a claim made by the named party.

## Conflict of interest and scope

This work grades public claims by AI vendors as well as adopters. Three of the graded parties supply tools used to produce or review it. Anthropic holds the highest-scoring row, is the most vocal party on recursive self-improvement, is named by Snap as the vendor behind its own figure, and makes the model used to draft this text. Google holds a graded row and makes the model used to review the draft. OpenAI is a graded party and its model assisted with the pre-publication red-team review. No row was softened or sharpened for any vendor, and every claim is anchored to a held primary so a reader can check the graded text against the source without trusting any party or the author. The research design, method, sourcing decisions and analytical judgements are the author's. This text was artificially generated with AI assistance and reviewed by the author before publication. The assisting model is not always a neutral party to the subject matter. Independent analysis and open-science documentation only, not investment advice. No warranty is offered beyond the terms of the CC BY 4.0 licence.
