# FP-2 instructor notes

Draft for review · revised 17 September 2026 · Companion to [student worksheet](student-worksheet.md)

**Scope:** adsorbed gas versus organic contamination at graphite–water interfaces, followed by probe-induced changes on H–Si(100). This packet does not prefigure the research layer's bulk-diffusion question.

## Seibert: evidence and variability

The key asymmetry is seven reported stripe-free glass-syringe references versus variable stripe formation in more than 100 independent "standard" plastic-syringe experiments, about 80 % of which showed stripes. The authors state that they repeated the glass-syringe experiment seven times *because* stripes were absent in about one fifth of plastic-syringe experiments (p. 7790). A glass syringe "cleaned" with surfactant solution produced stripes again, which the authors attribute to surfactant residue (pp. 7790–7791); strong answers may use this as further support for a contamination route. Protocols varied across experiments: two AFM instruments, two water purification setups, some NaCl solutions and some air-aged graphite (p. 7790). The two within-sample exchange experiments add intervention evidence. They must not be pooled as if all protocols were identical or assigned the general plastic-syringe rate without qualification. Source: Seibert pp. 7790–7791 and Fig. 2, [publisher version](https://doi.org/10.1021/acs.langmuir.0c00748). Check that students can reach it; access may require an institutional subscription.

A strong answer concludes that the reported controls support syringe-associated contamination as an explanation for these observations and challenge nitrogen-alone sufficiency under the tested conditions. It does not establish a particular chemical species, universal stripe production after plastic use, or the origin of all earlier reported stripes. A non-stripe outcome does not by itself refute a probabilistic contamination mechanism.

Seven negatives are a finite sample, not proof of zero probability. Credit quantitative reasoning when its assumptions are stated. Two examples:

- If glass-syringe runs failed as often as plastic ones, seven absences in a row would be improbable (0.2⁷ ≈ 1.3 × 10⁻⁵, assuming independence).
- Seven negatives are still compatible with a per-run stripe probability of up to about 0.35 (one-sided 95 %).

The totals (">100", "approximately 80 %") are approximate, and "repeated seven times" is quoted as the authors wrote it. Independence, protocol comparability and selection of representative images require assessment. No exact significance test or causal probability should be demanded from these summaries alone.

For the optional toy calculation, 0.8² = 0.64 under the explicitly assumed independent, equal-probability model. It is the probability of two successes under that model, not a posterior probability for the physical mechanism. Treating the broader plastic-syringe rate as an established exchange-protocol rate is an error.

Useful proposed controls could include matched glass-to-glass exchange, randomized handling order on fresh samples, or independent chemical analysis of introduced material. Credit the discriminating predictions and handling of confounds, rather than a particular instrument choice.

## Croshaw: acquisition as an event

Fig. 5 contains three distinct examples, not nine successive frames of one experiment. Each row supplies a before/intervention/after sequence. The authors identify subsequent STM frames with the earlier frames. Changes during scanning and possible tip changes must be represented. Source: [Croshaw paper](../sources/croshaw-2020.pdf), Fig. 5 and adjacent text.

Credit answers that separate directly observed contrast discontinuities from assignments of hydrogen removal, charge changes or tip functionalisation. A persistent specimen and location do not imply an unchanged state. Exact timings and a full history are not supplied simply by a well-labelled sequence.

## Xu: caption correction and correspondence are different checks

The [article XML](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11614372/fullTextXML) supports two editorial caption corrections: the second-row adhesive partner of (e) is (f), and that of (g) is (h). The body text explicitly names 4f and 4g–h. Preserve the original bytes; place corrections only in commentary.

The Fig. 4 caption describes 4a as the surface immersed in water for 30 min and 4e as the same scan area "after 170 min". It does not say when the 170 minutes start. A 140-minute interval follows only if both times count from immersion, so credit students who label it an inference. The same-area claim for 4a and 4e is in the caption; the body's "same area" refers to 4f and 4b. Image inspection can assess visible landmarks; it cannot by itself certify registration uncertainty. With the presently supplied evidence, same-region correspondence to a quantitative tolerance is unresolved. Neither the presence nor magnitude of drift has been measured in this scout. This is a relationship uncertainty, distinct from chemical identification.

## Claim table: what to credit

Check the [claim table](claim-table.md) for four things:

- each relationship kind appears;
- at least one relationship is supported and at least one is genuinely unresolved;
- unknown chemical identity is not used as the unresolved one;
- claim origin, disagreement and quantitative uncertainty stay in separate columns.

Examples from the core cases:

| Kind | Supported | Genuinely unresolved |
|---|---|---|
| Specimen identity | Seibert Fig. 2a↔2b: same specimen, water exchanged in situ (Fig. 2 caption) | Croshaw's three sequences: whether they share a sample, preparation or instrument is not stated (p. 1356; Methods p. 1357 lists two instruments) |
| Spatial correspondence | Seibert Fig. 2a↔2b: the authors state the same surface area (p. 7790); no registration tolerance is given | Croshaw (h)↔(i): the caption gives the size of the (h) frame, not its position within (i) |
| State history | Croshaw (a)→(b)→(c): an abrupt change during the negative-bias scan that persists in (c) (p. 1356) | Croshaw (g)→(h)→(i): the tip state during (i) after the apex change, and whether it affects the contrast in (i) |

Two limits on the table:

- A genuinely unresolved specimen-identity claim exists only at the level of how experiments are grouped.
- No supplied source contains a real revision of a claim that two exact records show the same region. A hypothetical revision must be marked as such; it does not close status item U3.

The dates students enter when they edit the table are not observatory record or revision dates.

## Historical interpretations and untested mechanics

Lu et al., *Sci. Rep.* 4, 7189 (2014), and Seibert (2020) provide differently dated interpretations about related phenomena. They do not establish a reanalysis of the same specimen or correction of the same image-to-image link. Preserve assertions with their scopes; do not overwrite one with another merely because it is later.

Do not credit "Seibert refutes Lu (2014)". The facts that rule it out:

- **Citation.** Seibert does not cite this paper. Its challenge targets assignments of stripes to nitrogen, citing Lu et al., *Langmuir* 28, 12691 (2012) and *Appl. Surf. Sci.* 304, 56 (2014) (refs 5–6).
- **Gas.** Lu et al. attribute their 2D and 3D patterns mainly to oxygen accumulating at the interface (p. 2). They report that these structures were not seen with degassed water or with water saturated or supersaturated with nitrogen (p. 3). They conclude that oxygen and nitrogen adlayers can form (p. 5).
- **Conditions.** Their water was pressurised to 2.4–3.7 atm and injected with a disposable syringe on a silicone tube; the syringe material is not stated (Methods).

A strong answer notes the different gas and conditions. It may raise the syringe as a possible contamination route without claiming that route is established, and it keeps both claims with their scopes and publication dates (26 November 2014; 23 June 2020).

The two core cases teach spatial evidence and recorded interventions. Seibert's in-situ exchange supplies little challenge for characterising long missing intervals. Croshaw supplies measurement-induced events, but does not repair that limitation. No claim is made that either history is exhaustively documented.

Keep the tracked longitudinal linkage safeguard and the missing-history/gap-characterisation safeguard separately open. Also keep the real revision of an exact correspondence, quantitative registration validation, and classroom testing open. See [task card](../planning/task-card.md).

## Distribution and readiness

Use Croshaw as the CC BY figure core, with attribution based on its publisher licence notice. Seibert remains a core case but link-only: its earlier CC BY record was withdrawn on 17 September 2026, and its figures are not reproduced until permission for the exact version and figure is verified. Keep Xu and Lu link-only with original commentary in the public packet. This is a deliberate packaging choice; it is not a claim that noncommercial material can never be publicly shared or that every arrangement of unchanged panels is an adaptation.

The worksheet is a source-linked review draft. No finished figure layout or classroom trial has been completed. Historical linked readings are supplementary, so the core learning aims can be taught without reproducing their figures.
