# Observatory architecture brief

Status: design direction consolidated from the discussion; no schema or implementation is frozen.

## Purpose and custody

The proposed observatory records versioned claims about relationships between scientific records and the evidence supporting them. Source labs retain authority over acquisition, handling and interpretation; durable repositories preserve source bytes. The observatory would supply the linkage and transformation layer.

This is not a claim that every laboratory already has a persistent archive. A future pilot must establish a working deposition route, retention responsibility and resolvable, versioned references. Taking custody of a deposited copy and asserting scientific provenance are separate responsibilities. The literature-first teaching packet can proceed independently of that choice.

## Claims and events

| Kind | Question | Typical evidence |
|---|---|---|
| Specimen identity | Is this the same physical object, or a documented descendant? | Identifiers, custody records, cleaving/reissue lineage |
| Spatial correspondence | Do these observations address the same region, and within what tolerance? | Image landmarks, coordinate conventions, transforms and validation |
| State history | What happened to that object between observations, and what is unknown? | Acquisition, transfer, storage, exposure, treatment and handling records |

A specimen may be the same object and region while its state changes intentionally. Acquisition is itself an event: beam-induced deposition, tip effects and damage may alter either specimen or observation response. Physical interventions and measurement conditions must not disappear into generic metadata.

Record the provenance of an assertion, its evidence availability, disagreement and any quantitative uncertainty separately. The inherited labels `verified`, `provider-asserted`, `opaque`, `unresolved` and `contested` mix these dimensions and are not a sound single status enum. A source assertion can be inspectable and disputed at the same time. Provider testimony is evidence about history, not independent confirmation of its completeness.

Quantitative uncertainty needs units, scope, method and assumptions; it may be unknown. Store achieved evidence and let a query supply the tolerance and other admissibility conditions. Do not invent a number for specimen identity or turn an uncertainty field into a universal quality score.

## Time and revision

Separate physical event/measurement time from when a claim is recorded or revised in the observatory. Also retain source publication and retrieval dates as provenance; neither is automatically the acquisition time or the date knowledge became available. Use intervals or explicit unknowns where appropriate. Retain superseded claims and their scope rather than overwriting them. See [evidence requirements](evidence-requirements.md).

## Spatial transformations

Future registration evidence should identify source/target records, coordinate conventions, transformation and domain of validity, landmark basis, achieved uncertainty and validation method. A fit residual on the landmarks used for fitting is not independent evidence of target-location accuracy. Multimodal contrast, calibration, drift and deformation affect transferability.

Deposited fiducials may perturb the surface chemistry being studied. External markers or intrinsic features are possible routes, each requiring validation; neither has been selected. Strong quantitative links may be rare. The design must remain useful with explicitly limited assertions. Stage metadata can help, but obtaining it alone does not validate registration.

## Two views and sequence

Teaching: a curated, access-relaxed view with annotations and explicit limits on any ground truth. Research: unresolved cases requiring continuous specimen histories and physical discrimination. Both could later render the same evidence model.

Build the standalone literature packet first. Treat teaching renderings as regenerable; a stable course release must not silently freeze a research schema. A real time-series module and history-gap exercise remain required before research depends on those mechanics. Current Markdown tables are teaching scaffolding, not a serialization decision.

## Deferred dependencies and feasibility

NOMAD/Oasis, NeXus application definitions, NFFA microscopy metadata and PSDI's AFM collection were raised as reuse leads. Their modality coverage, identifiers, preservation guarantees, export and licensing need verification against an actual pilot. This handoff does not establish their fit. Profile existing standards where suitable; retain novelty in relationship evidence rather than duplicate instrument metadata.

A supported deposition workflow still needs an institution to operate and retain it. Byte preservation also does not preserve a wafer: physical labels, retention, disposal, cleaving and reuse must be recorded. A later partner-lab pilot should first deliver acquisition-record/deposition tooling useful to that lab even without the observatory. Adoption is a feasibility test; no partner commitment currently exists.

Access controls for the two views, schema/serialization, registration thresholds, research specimen and implementation ownership are open. The present repository deliberately contains no placeholder service or speculative application stack.
