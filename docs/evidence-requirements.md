# Evidence and revision requirements

Requirements for later evaluation, not a scientific data schema.

Each relationship claim should identify the records and physical scope it concerns, the relationship kind, the claimant/source, the evidence locator, unresolved information and the inference affected. Track disagreement independently from origin and uncertainty. A chemical assignment is a physical interpretation; do not use it as the required unresolved relationship claim.

A state-history interval should preserve known events, the source of each statement, the interval's boundaries and explicit gaps. Six weeks under recorded sealed storage and six weeks with undocumented shared storage are different evidence situations. Neither justifies claiming that all unrecorded events are impossible.

## Time fields to distinguish

| Concept | Meaning | Current handling |
|---|---|---|
| Measurement/event time | When the physical observation or intervention occurred | Record reported relative/absolute times; otherwise unknown |
| Claim's physical scope | Which observation, state or interval the assertion concerns | Preserve exact record/panel scope; do not merge experiments |
| Source publication time | When the cited interpretation was published | Retain separately; not a substitute for measurement time |
| Observatory record/revision time | When the system received or revised a claim | Not implemented; do not fabricate historical ingestion dates |
| Retrieval time | When the preserved bytes were fetched | Existing manifest records UTC values |

Bitemporal resolution concerns the physical/valid-time scope and the record/revision history. Publication and retrieval dates add provenance. A later claim about a comparable phenomenon does not automatically supersede a claim about an earlier exact specimen or image.

## Exercises that would test the model

- Reconstruct a genuine tracked longitudinal sequence while retaining unknown events and uncertain correspondence.
- Compare histories with different documented and missing intervals and show which inference changes.
- Preserve an actual earlier assertion and a documented later revision concerning the same records; query what the representation would return before and after that revision. A hypothetical example can test code paths but cannot meet the real-literature safeguard.
- Evaluate a registration against an independently stated spatial tolerance, with evidence beyond the fitting residual and with calibration assumptions recorded.

None of these acceptance checks has been passed by a graph implementation. Published images may include scale bars or coordinate information, but the inspected teaching material has not supplied a validated registration basis. Real data, appropriate metadata and independent evaluation remain necessary.
