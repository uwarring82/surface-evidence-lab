# AI desk check, 17 September 2026

**This is not a walkthrough.** An AI agent read the student materials against the sources to find questions that cannot be answered, factual mismatches and likely stumbling points. It measured no timings and involved no students or instructors. It prepares the [walkthrough](walkthrough-protocol.md) and is not evidence for U7.

**Record status:** the findings below describe commit `7b8b789` and are kept unchanged. Suggestions 1–4 were applied on 17 September 2026 and suggestions 5 and 6 on 18 September 2026; the rest remain open.

## Method

- **Reviewed:** commit `7b8b789`, specifically the worksheet, instructor notes, claim table and figure sheet.
- **Reviewer:** a Claude agent working read-only. It did not see earlier review conclusions.
- **Sources read:**
  - Seibert: publisher PDF, all pages as text, with Fig. 2 rendered.
  - Croshaw: PDF, XML, the Fig. 5 image, and the Supporting Information captions for S15–S17.
  - Xu: the full XML.
  - Lu: the full PDF text.
- **Not checked:** Seibert's Supporting Information, and the Xu and Lu figure images.
- **Spot-check:** every discrepancy listed below was then checked against the source text by a second Claude session. Two items were not independently checked and are marked as such: the pixel measurements and the judgement calls.

## Answerability

| Question | Answerable from supplied materials | Main limit |
|---|---|---|
| 1 | Partly | Nitrogen details and further controls are only in the paywalled paper |
| 2 | Partly; yes with Fig. 2 | Landmark evidence needs access to Fig. 2 |
| 3 | Yes | Stronger answers use counts the worksheet omits |
| 4 | Partly | Protocol differences are only in the paper's experimental section |
| 5, 6 | Yes | — |
| Probability exercise | Yes | — |
| 7, 8, 10 | Yes | Jargon: empty/filled states, band bending |
| 9 | Partly | Useful evidence is on pages the worksheet does not point to |
| 11 | Partly | The 140-minute interval is inferred, not reported |
| 12 | Yes | Few genuine contradictions to find |
| 13 | Partly | The linked Lu paper is not the one Seibert cites |
| 14 | Yes | Abstract without an example |
| Claim-table submission | Partly | Worksheet and template disagree |

## Discrepancies, most serious first

1. **Submission instructions and claim table disagree.**
   - The worksheet's Submission section lists six columns and does not link [claim-table.md](../claim-table.md).
   - The template has ten columns, a separate dates table, and the rule that at least one relationship must be supported and one genuinely unresolved (chemical identity alone does not count). The worksheet never states that rule.
   - The template uses internal terms students will not know: "U3", "observatory schema", "ingestion dates".
   - The instructor notes give no grading guidance for the table.
2. **Part D pairs Seibert with a Lu paper that Seibert does not cite.**
   - Seibert's nitrogen citations are Lu et al., *Langmuir* 28, 12691 (2012) and Lu et al., *Appl. Surf. Sci.* 304, 56 (2014) (refs 5–6). They are not the linked *Sci. Rep.* 4, 7189 (2014).
   - Lu's *Sci. Rep.* experiments used water pressurised to 2.4–3.7 atm with nitrogen or oxygen, injected with a disposable syringe (Methods). Seibert's glass references say only that nitrogen was present.
   - The notes' "related phenomena" wording is correctly cautious, but students may still write that Seibert refutes this paper.
3. **The Xu interval is presented as reported.**
   - Both the worksheet (Q11) and the instructor notes say the text reports "30 and 170 minutes after immersion, an interval of 140 minutes".
   - The XML says the Fig. 4e image is of the same scan area "after 170 min", without saying when the 170 minutes start. "140" does not appear in the text.
   - The 140-minute reading is plausible but should be labelled as an inference, which is exactly the distinction the exercise teaches.
4. **The Seibert summary omits facts that change strong answers to Q1, Q3 and Q4.** All are on p. 7790:
   - more than 100 independent standard (plastic-syringe) experiments, about 80 % of which showed stripes;
   - the authors chose seven glass-syringe repeats *because* of the one-in-five absence rate;
   - stripes did form with a glass syringe cleaned with surfactant solution;
   - protocols varied: two AFM instruments, two water purification setups, some NaCl solutions, some graphite aged in air.
5. **Part A depends on access to the paper.** Fig. 2 is not reproduced, and Q2 and Q4 need it. There is no fallback if subscription access fails.
6. **Q9 has no expected answer and points nowhere.**
   - The authors present the tip change in (h) as *supporting* evidence for hydrogen removal (p. 1356), not as a confound.
   - Relevant evidence the worksheet does not point to: p. 1347 (tip functionalisation changes STM contrast), p. 1352 (images taken while monitoring for tip changes; hydrogen removal occurs easily) and Supporting Information Figs. S16–S17.
   - The notes should list what a strong answer uses, e.g. comparison with sequences (a–c) and (d–f), where no tip change is asserted.
7. **The Xu editorial note is slightly stronger than its support, and misses one label slip.**
   - The body text names Fig. 4f as the adhesive image of the same area, which directly supports the (e)→(f) correction.
   - For (h), the body only refers to "Figures 4g and h", so the (g)→(h) correction is inferred from the panel pattern.
   - Missed slip: §2.3 says "red square area in Figure 2a" where Fig. 4a is meant.
   - The notes' "second-row" wording describes image layout that the XML cannot confirm.
8. **Figure sheet precision** (pixel measurements by the agent, not independently checked).
   - Within each Fig. 5 row, the before and after scale bars have equal length; across rows they differ, and (h) is the smallest frame.
   - The caption says the white box in (i) shows the *size* of the (h) frame, not its position. Measured against the bars, the box and the (h) frame differ by about a quarter.
   - Colour ranges differ between before and after panels (0–145 pm in (g), 0–50 pm in (i)).
9. **Minor.**
   - Part B gives no page locator (Fig. 5 and its discussion are on p. 1356).
   - The worksheet date line still reads 10 September although the text was revised on 17 September.
   - Terms such as in situ, terrace, empty/filled states, band bending, tip termination, adhesive image, micropancake, registration and contingency table have no glossary.

## Candidate claim-table rows (for instructors)

All three relationship kinds can be filled from the core cases:

| Kind | Supported | Genuinely unresolved |
|---|---|---|
| Specimen identity | Seibert Fig. 2a↔2b: the same specimen, with the water exchanged in situ (Fig. 2 caption) | Croshaw's three sequences: whether they come from one sample, preparation or instrument is not stated (p. 1356; Methods p. 1357 lists two instruments) |
| Spatial correspondence | Seibert Fig. 2a↔2b: the authors state the same surface area (p. 7790); no registration tolerance is given | Croshaw (h)↔(i): the caption gives the size of the (h) frame, not its position within (i) |
| State history | Croshaw (a)→(b)→(c): an abrupt change during the negative-bias scan that persists in (c) (p. 1356) | Croshaw (g)→(h)→(i): the tip state during (i) after the apex change, and whether it affects the contrast in (i) |

A genuinely unresolved specimen-identity claim exists only at the level of how experiments are grouped. No supplied source contains a real revision of a same-record correspondence, as [claim-table.md](../claim-table.md) already notes.

## Suggested revisions

Suggestions for the project lead, as made at `7b8b789`. See the record status at the top for which were applied later.

| # | Kind | Suggestion |
|---|---|---|
| 1 | Structural | Link the claim-table template from the Submission section, align the column lists, copy the supported/unresolved rule into the worksheet, and move internal terms (U3, observatory) to the instructor notes. Add grading guidance for the table |
| 2 | Factual | Q11 and notes: quote "after 170 min", say its starting point is not stated, and give 140 minutes as an inference |
| 3 | Factual | Part D: say that Seibert cites other Lu papers, not this one; point out the supersaturated-water conditions and the disposable syringe; update the notes |
| 4 | Factual | Part A table: add the >100 standard experiments at ≈80 %, the surfactant-cleaned glass-syringe result and the protocol variation (p. 7790) |
| 5 | Structural | Mark Q2 and Q4 as needing the paper; give instructors a short text description of Fig. 2 as a fallback |
| 6 | Wording | Q9: say how the authors use the tip change; point to pp. 1347, 1352, 1356 and Figs. S16–S17; add expected answer elements to the notes |
| 7 | Wording | Part B: add the page locators p. 1356, p. 1352 and Methods p. 1357 |
| 8 | Factual, minor | Xu note: separate the directly supported (e)→(f) correction from the inferred (g)→(h) one; add the §2.3 "Figure 2a" slip; drop "second-row" unless the image is checked |
| 9 | Wording | Figure sheet: equal before/after scale bars within rows; the white box gives size only; different colour ranges |
| 10 | Structural | Instructor notes: add expected elements for Q2, Q4, Q7–Q10, Q12 and Q14, and say whether quantitative extensions earn credit (for example, what seven negative references still allow) |
| 11 | Wording | Add a short glossary; update the worksheet date |

## Left for the human walkthrough

- Time per part, and whether Parts A and B fit the session.
- Whether students can open Seibert, and what they do if they cannot.
- Whether the jargon is understood without a glossary.
- Whether Fig. 5 scan arrows and discontinuities are legible on screen and in print.
- Whether students read Q13 as "Seibert refutes Lu".
- Whether students produce a genuinely unresolved, non-chemical claim, and whether graders agree on what counts.
- Whether the probability exercise clarifies or confuses.
- Whether different instructors grade consistently from the notes.
