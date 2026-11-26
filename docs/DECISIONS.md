# Decisions

One line per methodological decision: what you chose, why, and what it changed.
Agents append here via the `/new-feature` skill; you append here by hand.

- Exclude `casual`, `registered`: they sum to `cnt` exactly. Leaky model R^2 1.000 -> honest ridge 0.583.
- Exclude `cnt_2d_bfr`: a shipped 2-day lag we cannot test the alignment of. Build our own lags instead.
- Exclude `instant`, `yr`, `days_since_2011`: time indexes let a tree predict a flat constant past 2011 and a linear model extrapolate a trend we have no grounds for.
- Split 2011 / H1 2012 / H2 2012 by date. Test set touched once, after all feature work.
- Report mean and persistence baselines with every score. Persistence (test R^2 0.510, MAE 840) is within 0.07 R^2 of ridge and beats it on MAE; that caveat goes in the report.
- 2026-11-25 (agent proposal): Add cnt_std_7, the population standard deviation of demand on the previous seven calendar days; it is available after yesterday closes and needs no larger warm-up. Validation ridge R² 0.6475 -> 0.7224 (+0.0749), MAE 832.9 -> 700.4; hgb R² 0.2185 -> 0.0977 (-0.1208). Keep for the ridge comparison based on validation, before evaluating final test metrics; subsequently reviewed and accepted by the user.
- 2026-11-25 (agent proposal): Model the target difference cnt(t)-cnt(t-1), then add yesterday back. Validation residual-tree R² 0.5642 and MAE 885.8 versus untransformed tree 0.0977/1381.6 and ridge 0.7224/700.4. Defensible only for rolling one-day predictions with yesterday observed; do not replace the untransformed headline models.
- 2026-11-25: Update CLAUDE.md with volatility convention, seed-fault skill, and same-day weather availability caveat. Preserve starter constraints and both baselines.
- 2026-11-25: Add explicit raw-column classifications and alias detection; unknown weather must raise. Add immutable raw SHA-256 validation to catch writes outside Edit/Write hooks.
- 2026-11-25: The agent performed implementation and deterministic checks. Independent reviewer and SDK audit runs remain pending. The user subsequently reviewed and accepted the methodological conclusions.
- 2026-11-25: Freeze before/after comparison before final test scoring; top-level metrics remain final untransformed models, before_feature preserves original features on the same rows. Regeneration is verification only.
- 2026-11-25 (agent proposal): Keep persistence as deployment default pending forecast-weather validation and a cost function. Final ridge test R² 0.6356 versus 0.5099 but MAE 840.3 versus 840.1 does not establish a daily absolute-error advantage; subsequently reviewed and accepted by the user.
- 2026-11-25: Pin already-required transitive pipeline dependencies to the verified environment; introduce no new modelling dependency.

- 2026-11-25: After reviewing REPORT.md and this log, the user accepted feature retention, the residual transformation’s rolling one-day availability argument, and persistence as the deployment default pending forecast-weather validation. These conclusions originated as agent proposals and were endorsed after review.
- 2026-11-25: Audit teammate bcan13/ma6 at commit 43783db924272cf22fe64551adf1e5f29c0f3eaf using a fresh independent reviewer and the starter checklist. All five checks pass under its disclosed weather/forecast assumptions; 17 tests pass and both metric files reproduce exactly with peer-pinned numerical packages. Save reviewer output verbatim and a draft verdict for student review; do not treat this as our own-repository SDK audit.
- 2026-11-25: Before the own-repository SDK run, repair the starter identity tool to accept the pipeline’s Parquet output and require absolute paths; scope identity candidates to actual model inputs, distinguish historical lags from future-target leakage, resolve repository paths, and explicitly load project/local endpoint settings.
- 2026-11-25: The user reviewed and accepted the peer-audit verdict in docs/AUDIT.md, then requested a fresh independent agent audit of this repository rather than running the local-model SDK workflow. Record that execution method explicitly.
- 2026-11-25: Complete the requested own-repository independent agent audit at d5af212023431bf5e906499f4f7b25de8381802c: 19 tests pass, both metric files and 32 table values match, no material findings. Save actual one-line JSON with execution metadata and full evidence; do not label this as SDK batch output.
- 2026-11-25: Document the assignment-specified reference setup (Claude Code harness, qwen3.5:9b through Ollama, 64k context) separately from the independently verified execution method.
- 2026-11-25: Final rubric review verifies every required path, five report sections, eight comparison rows/32 exact values, unchanged raw hash and retained starter files. A fresh full requirements installation (including SDK 0.2.172) reproduces both metric files byte for byte and passes 19 tests; preserve exact logs and environment. Keep the incomplete 25-second SDK retry separate from the successful independent agent audit.
