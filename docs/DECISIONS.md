# Decisions

One line per methodological decision: what you chose, why, and what it changed.
Agents append here via the `/new-feature` skill; you append here by hand.

- Exclude `casual`, `registered`: they sum to `cnt` exactly. Leaky model R^2 1.000 -> honest ridge 0.583.
- Exclude `cnt_2d_bfr`: a shipped 2-day lag we cannot test the alignment of. Build our own lags instead.
- Exclude `instant`, `yr`, `days_since_2011`: time indexes let a tree predict a flat constant past 2011 and a linear model extrapolate a trend we have no grounds for.
- Split 2011 / H1 2012 / H2 2012 by date. Test set touched once, after all feature work.
- Report mean and persistence baselines with every score. Persistence (test R^2 0.510, MAE 840) is within 0.07 R^2 of ridge and beats it on MAE; that caveat goes in the report.
- 2026-11-25 (Codex proposal): Add cnt_std_7, the population standard deviation of demand on the previous seven calendar days; it is available after yesterday closes and needs no larger warm-up. Validation ridge R² 0.6475 -> 0.7224 (+0.0749), MAE 832.9 -> 700.4; hgb R² 0.2185 -> 0.0977 (-0.1208). Keep for the ridge comparison based on validation, before evaluating final test metrics; user review pending.
- 2026-11-25 (Codex proposal): Model the target difference cnt(t)-cnt(t-1), then add yesterday back. Validation residual-tree R² 0.5642 and MAE 885.8 versus untransformed tree 0.0977/1381.6 and ridge 0.7224/700.4. Defensible only for rolling one-day predictions with yesterday observed; do not replace the untransformed headline models.
- 2026-11-25: Update CLAUDE.md with volatility convention, seed-fault skill, and same-day weather availability caveat. Preserve starter constraints and both baselines.
- 2026-11-25: Add explicit raw-column classifications and alias detection; unknown weather must raise. Add immutable raw SHA-256 validation to catch writes outside Edit/Write hooks.
- 2026-11-25: Codex performed implementation and deterministic checks, not Claude Code/Ollama. Do not attribute these runs to an open-weight model or invent teammate audit evidence. Human methodological endorsement is pending.
- 2026-11-25: Freeze before/after comparison before final test scoring; top-level metrics remain final untransformed models, before_feature preserves original features on the same rows. Regeneration is verification only.
- 2026-11-25 (Codex proposal): Keep persistence as deployment default pending forecast-weather validation and a cost function. Final ridge test R² 0.6356 versus 0.5099 but MAE 840.3 versus 840.1 does not establish a daily absolute-error advantage; user judgment pending.
- 2026-11-25: Pin already-required transitive pipeline dependencies to the verified environment; introduce no new modelling dependency.
