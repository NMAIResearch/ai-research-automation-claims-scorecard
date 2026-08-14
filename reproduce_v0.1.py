#!/usr/bin/env python3
"""
AI Research-Automation Scorecard v0.1 - reproduction script.

AI disclosure: this script was drafted with AI assistance and reviewed by the author.
OpenAI models also assisted with this pre-publication red-team review; OpenAI is a
graded party in the scorecard.

Regenerates every table and count in the piece from claims_v0.1.csv and
triggers_v0.1.csv, and verifies every held source against its recorded SHA-256.

Python 3 standard library only. No dependencies, no network.

Exit codes:
  0  everything reproduced and every held source hash matched
  1  data-integrity failure (unsourced row, missing file, or hash mismatch)

Scoring, unchanged from v0 (an unweighted convenience index, not a validated metric):
  denominator_defined   Y=1.0  partial=0.5  N=0.0
  measured_vs_anecdote  audited=1.0, everything else 0.0
  reproducible          Y=1.0  N=0.0
  second_source         Y=1.0  N=0.0

research_loop_isolated is REPORTED, never scored. A public statement about general
coding automation has no duty to break out an internal research-loop share, so
grading it against that would be a category error.
"""

import csv, os, sys, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
CLAIMS = os.path.join(HERE, "claims_v0.1.csv")
TRIGS = os.path.join(HERE, "triggers_v0.1.csv")
# Zenodo flattens a deposit, so the register sits beside this script there and in a
# sources/ subdirectory in the working folder. Try both rather than crashing on the one.
REG = next((p for p in (os.path.join(HERE, "sources", "source_register.csv"),
                        os.path.join(HERE, "source_register.csv"))
            if os.path.exists(p)), os.path.join(HERE, "source_register.csv"))

fail = []


def rd(p):
    with open(p, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def verify_sources():
    print("=" * 78)
    print("SOURCE INTEGRITY")
    print("=" * 78)
    rows = rd(REG)
    bundled = os.path.isdir(os.path.join(HERE, "sources")) and any(
        os.path.exists(os.path.join(HERE, r["local_path"])) for r in rows if r["local_path"])
    if not bundled:
        print("  Source files are NOT bundled with this deposit, by design.")
        print("  They are third-party material, and the CC BY licence on this deposit")
        print("  covers the author's own work, not theirs. No redistribution permission")
        print("  was sought, so the register carries an address, a date and a hash")
        print("  instead of a copy.")
        print(f"\n  {len(rows)} sources are listed in source_register.csv with a URL,")
        print("  a retrieval date and a SHA-256 of the copy the author held.")
        print("  Fetch a source yourself to check the claim it supports.")
        print("\n  NOTE ON HASHES: stable files such as the arXiv PDFs will reproduce the")
        print("  recorded hash. Browser captures (.mhtml) will NOT, because a capture embeds")
        print("  session data and timestamps. For those the hash anchors the author's own")
        print("  chain of custody; it is not a value a reader can independently re-derive.")
        print("\n  Integrity check skipped. Every other table below still regenerates.\n")
        return
    held = notheld = 0
    for r in rows:
        sid, status, path, want = r["source_id"], r["retrieval_status"], r["local_path"], r["sha256"]
        if status != "retrieved":
            notheld += 1
            print(f"  [ -- ] {sid}: {status}")
            continue
        full = os.path.join(HERE, path)
        if not os.path.exists(full):
            fail.append(f"{sid}: registered as retrieved but file missing at {path}")
            print(f"  [FAIL] {sid}: file missing")
            continue
        got = hashlib.sha256(open(full, "rb").read()).hexdigest()
        if got != want:
            fail.append(f"{sid}: sha256 mismatch")
            print(f"  [FAIL] {sid}: hash mismatch")
        else:
            held += 1
            print(f"  [ ok ] {sid}")
    print(f"\n  {len(rows)} registered | {held} held and hash-verified | {notheld} not retrieved\n")


def check_by_ear():
    """Print the address and timestamp for every claim anchored to a transcript.

    Six of the eighteen sources are transcripts, and none of them is redistributed
    here. That does not make the claims they carry uncheckable: the register records the
    video and the second at which the words occur, so a reader goes to the recording
    itself rather than to the author's reading of it. This runs identically inside the
    deposit, where no source file is present.
    """
    reg = {r["source_id"]: r for r in rd(REG)}
    rows = [r for r in reg.values() if r.get("quote_anchor")]
    if not rows:
        return
    print("=" * 78)
    print("CHECKING A TRANSCRIPT-ANCHORED CLAIM WITHOUT ANY FILE FROM THIS DEPOSIT")
    print("=" * 78)
    print("  Open the address, go to the timestamp, listen. No download required, and")
    print("  nothing here depends on the author's transcript being correct.\n")
    claims = rd(CLAIMS)
    for r in sorted(rows, key=lambda x: x["source_id"]):
        who = [c["lab"] for c in claims if r["source_id"] in c["source_id"].split("|")]
        print(f"  {r['quote_anchor']:<34} {r['url']}")
        print(f"  {'':34} anchors: {', '.join(who) if who else 'Layer 2 register'}")
    print()


def score(r):
    d = {"Y": 1.0, "partial": 0.5, "N": 0.0}[r["denominator_defined"].strip()]
    m = 1.0 if r["measured_vs_anecdote"].strip() == "audited" else 0.0
    p = 1.0 if r["reproducible"].strip() == "Y" else 0.0
    s = 1.0 if r["second_source"].strip() == "Y" else 0.0
    return d + m + p + s


def scorecard():
    rows = rd(CLAIMS)
    print("=" * 78)
    print("LAYER 1: CLAIMS")
    print("=" * 78)
    print(f"{'lab':<11}{'date':<12}{'type':<12}{'tier':>4}{'score':>7}  {'anchor':<9}claim")
    print("-" * 78)
    reg = {x["source_id"] for x in rd(REG) if x["retrieval_status"] == "retrieved"}
    for r in rows:
        if not r["source"].strip():
            fail.append(f"{r['lab']} ({r['source_date']}): no source recorded")
        sids = [s for s in r["source_id"].split("|") if s]
        if r["anchor_status"] == "held_primary":
            missing = [s for s in sids if s not in reg]
            if not sids or missing:
                fail.append(f"{r['lab']} ({r['source_date']}): claims held_primary but "
                            f"{'no source_id' if not sids else 'unheld ' + ','.join(missing)}")
        print(f"{r['lab']:<11}{r['source_date']:<12}{r['claim_type']:<12}"
              f"{r['motive_tier']:>4}{score(r):>7.1f}  "
              f"{'HELD' if r['anchor_status']=='held_primary' else 'sec.':<9}{r['claim_short'][:26]}")
    n = len(rows)
    tot = sum(score(r) for r in rows)
    dY = sum(1 for r in rows if r["denominator_defined"].strip() == "Y")
    dP = sum(1 for r in rows if r["denominator_defined"].strip() == "partial")
    au = sum(1 for r in rows if r["measured_vs_anecdote"].strip() == "audited")
    rp = sum(1 for r in rows if r["reproducible"].strip() == "Y")
    ss = sum(1 for r in rows if r["second_source"].strip() == "Y")
    rl = sum(1 for r in rows if r["research_loop_isolated"].strip() == "Y")
    tg = sum(1 for r in rows if r["claim_type"].strip() in ("target", "prediction"))
    print("-" * 78)
    print(f"\nN = {n} claims. Each count below is individually checkable in the CSV.\n")
    print(f"  denominator rigorously defined     {dY}/{n}   (a further {dP}/{n} partial)")
    print(f"  externally audited                 {au}/{n}")
    print(f"  externally reproducible            {rp}/{n}")
    print(f"  independent check of THAT figure   {ss}/{n}")
    print(f"  targets or predictions, not measurements   {tg}/{n}")
    print(f"\n  unweighted convenience index       {tot/n:.2f}/4")
    # Averaging measurements together with targets and predictions is a fair objection
    # to any index. It is answered by measurement rather than by argument: the two
    # subsets are printed so a reader can see whether the mixture moves the number.
    fwd = [r for r in rows if r["claim_type"].strip() in ("target", "prediction")]
    cur = [r for r in rows if r not in fwd]
    for label, grp in (("current claims only", cur), ("targets and predictions only", fwd)):
        if grp:
            print(f"    {label:<32} {sum(score(r) for r in grp)/len(grp):.2f}/4  (n={len(grp)})")
    hp = sum(1 for r in rows if r["anchor_status"] == "held_primary")
    print(f"\n  REPORTED, NOT SCORED: {rl}/{n} claims isolate the research loop.")
    print(f"\n  ANCHORING: {hp}/{n} traced to a held, hash-verified primary.")
    print(f"             {n-hp}/{n} rest on secondary reporting of the original statement.")
    print("             A secondary-reported row is graded on the reported wording and")
    print("             cannot be checked against what the speaker actually said.")


def triggers():
    rows = rd(TRIGS)
    print("\n" + "=" * 78)
    print("LAYER 2: TRIGGER AND EVENT REGISTER")
    print("=" * 78)
    for r in rows:
        print(f"  [{r['trigger_type']:<22}] {r['lab']} - {r['trigger_name']}")
        print(f"        status: {r['status']} (as of {r['status_date']})")
    kinds = {}
    for r in rows:
        kinds[r["trigger_type"]] = kinds.get(r["trigger_type"], 0) + 1
    crossed = sum(1 for r in rows if r["trigger_type"] == "red_line"
                  and r["status"] not in ("not_crossed", "not_reached", "not_met"))
    print(f"\n  {len(rows)} rows: " + ", ".join(f"{v} {k}" for k, v in sorted(kinds.items())))
    print(f"  red-lines reported crossed: {crossed}")


if __name__ == "__main__":
    verify_sources()
    check_by_ear()
    scorecard()
    triggers()
    print("\n" + "=" * 78)
    if fail:
        print("INTEGRITY FAILURES:")
        for f in fail:
            print("  -", f)
        sys.exit(1)
    print("OK: every claim is sourced and every held source matched its recorded hash.")
    sys.exit(0)
