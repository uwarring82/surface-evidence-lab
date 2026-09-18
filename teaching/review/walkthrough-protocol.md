# Walkthrough protocol

Prepared 17 September 2026 for [issue 01](../../planning/issues/01-teaching-prototype.md). Record each walkthrough in a copy of the [record form](walkthrough-record.md). This protocol does not decide FP-2 readiness; the project lead decides on the recorded evidence.

## Purpose

Find out whether a student can work through the packet as written: whether each question can be answered from the supplied sources, how long it takes, where people get stuck, and what must change before classroom use. The walkthrough is the evidence for status item U7. It does not touch U1–U4.

## Who and which method

Name every reviewer and their role. Record the method as exactly one of these, and never describe a method as more than it was:

| Method | What it is | What it can show |
|---|---|---|
| Instructor walkthrough | An instructor answers the worksheet as a student would, without the instructor notes, then compares their answers with the notes | Answerability, wording problems and reviewer completion time; student timing remains untested |
| Peer walkthrough | A tutor or colleague who did not write the materials does the same | The above, less biased by knowing the intended answers |
| Student pilot | One or more students work the packet under course-like conditions | Real timing and comprehension. Needs the students' agreement; record no names or personal data in the repository |

An AI desk check is preparation, not a walkthrough. The [2026-09-17 desk check](ai-desk-check-2026-09-17.md) lists points to probe; it is not evidence for U7.

## Before starting

1. Work from a clean checkout of the commit you are reviewing: check it out, confirm `git status` reports no changes, and record `git rev-parse --short HEAD`. Findings then refer to fixed text.
2. Decide the session length available in FP-2 and write it on the record form; timing is judged against it.
3. Check access to Seibert et al. (2020) through the [DOI link](https://doi.org/10.1021/acs.langmuir.0c00748) from the network students will use, on and off campus if both apply. The paper is not supplied in the repository.
4. Prepare the student materials only: [worksheet](../student-worksheet.md), [figure sheet](../figure-sheet.md), [claim table](../claim-table.md) and the linked papers. Keep the [instructor notes](../instructor-notes.md) closed until the comparison step.
5. If the packet may be printed, print the figure sheet once on A4 in greyscale and check that the Fig. 5 panel labels are legible.

## During the walkthrough

Work in the order of the worksheet. For each part, note start and stop times. For each question:

- write an answer before looking at the instructor notes;
- mark whether it could be answered from the supplied materials: yes, partly or no;
- record where you got stuck: unclear wording, missing information, access, jargon or an ambiguous figure;
- note any source statement you had to search for, with page and figure.

Complete the claim table as a student would: at least one claim for each relationship kind (specimen identity, spatial correspondence, state history), with at least one supported and at least one genuinely unresolved relationship. Unknown chemical identity alone does not count as unresolved.

## After the walkthrough

1. Compare your answers with the instructor notes. Record every place where a reasonable answer differs from the notes, and whether the notes or the worksheet should change.
2. List proposed revisions. Make them in separate commits that cite the record.
3. List the teaching limitations that remain after revision.
4. Give a recommendation: ready, ready after listed revisions, or not ready. The project lead records the decision and updates U7 in [STATUS.md](../../STATUS.md) only on this evidence.

## Readiness criteria

A recommendation of "ready" needs all of the following:

- Every core question (Parts A and B, questions 1–10) is answerable from the supplied materials, or has been revised until it is.
- No open factual discrepancy between the worksheet, the instructor notes and the sources.
- The claim-table requirement can be met from the core cases.
- The core parts fit the session length recorded above.
- Seibert access works for students, or an alternative route to Fig. 2 is recorded.
- The figure sheet is legible in the medium students will use.

Optional Parts C and D do not block readiness, but record their timing and problems too.

## Points to probe

From the [AI desk check](ai-desk-check-2026-09-17.md) of commit `7b8b789`. Its suggestions 1–6 (claim-table instructions, Xu interval, Part D comparison, Seibert summary, the access fallback for Q2 and Q4, and Q9 guidance) were applied before the walkthrough: check that they work. The other suggestions are still open: check how much they matter in practice.

- **Seibert access (Part A):** does access work for students? If it fails, does the instructor's description of Fig. 2 carry Q2 far enough, and what happens to Q4?
- **Claim table:** do reviewers find the template from the worksheet? Do they meet the supported/unresolved rule without being told it?
- **Q9:** with the added locators, does the reviewer find evidence that separates a changed specimen from a changed imaging response, or only restate the authors' tip-change claim?
- **Q11:** is the 140-minute interval treated as reported or as inferred?
- **Q13:** is the linked Lu paper treated as the one Seibert challenges?
- **Fig. 5:** are the scan arrows, discontinuities and colour ranges legible, and are different colour ranges mistaken for contrast changes?
- **Jargon:** which terms needed looking up (empty/filled states, band bending, tip termination, adhesive image, registration)?
- **Instructor notes:** where did a reasonable answer differ from the notes, particularly for Q2, Q4, Q7–Q10, Q12 and Q14, which the notes barely cover?
