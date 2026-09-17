# Surface Evidence Lab

A literature-based FP-2 teaching lab on how surface-microscopy observations support physical explanations, specimen identity, spatial correspondence and specimen histories.

**Status, 17 September 2026:** the first-pass literature scout is complete and two teaching cases have worksheet and instructor drafts. Figure layout and a teaching walkthrough remain open. The observatory is a conceptual architecture; no graph service, scientific schema or research pipeline has been implemented. The evidence archive was assembled on 10 September 2026; this packaging pass adds no new literature verification.

The teaching core studies **adsorbed gas versus organic contamination at graphite–water interfaces** (Seibert, 2020) and **probe-induced changes on H–Si(100)** (Croshaw, 2020). The proposed research layer would address **bulk diffusion versus ambient contamination**. These are distinct physical questions.

## Start here

1. Read [current status](STATUS.md) and the [task card](planning/task-card.md).
2. Review the [student worksheet](teaching/student-worksheet.md), [instructor notes](teaching/instructor-notes.md) and [editable claim table](teaching/claim-table.md).
3. Follow the [repository setup instructions](SETUP.md). Verify the preserved sources with `python3 scripts/verify_sources.py --require-local-archive` when using the complete ZIP.
4. Take the next task from the [roadmap](ROADMAP.md) and [issue drafts](planning/issues/README.md).

## Repository map

| Location | Contents |
|---|---|
| `teaching/` | Review drafts, blank claim table, figure preparation brief |
| `literature/` | Scout and human/machine-readable source manifests: 15 source records |
| `sources/` | Eight preserved files associated with the CC BY sources and their provenance records |
| `local-source-archive/` | Xu XML and unchanged Lu PDF, included in this ZIP but ignored by Git by default |
| `docs/` | Architecture brief, decisions, evidence and time-model requirements |
| `planning/` | Task card and actionable issue drafts |
| `scripts/` | Source-integrity verification using only the Python standard library |
| `RIGHTS.md` | Original-material licence status and source-specific distribution policy |

The ZIP is a source-preservation and repository handoff bundle. It is not the finished public course packet. Third-party sources retain their individual terms, and a licence for the original project material has not yet been selected. See [rights](RIGHTS.md).

No live lab agreement, deposition platform or application framework is needed to finish the introductory packet. The longer-term tracking and history-gap safeguards remain explicit prerequisites for research functionality that depends on them.
