## Results

This analysis predicts daily Capital Bikeshare demand using the supplied 728-row mirror, spanning January 3, 2011 through December 31, 2012. March 10, 2011 is absent. Weather labels are GOOD (463), MISTY (245), and BAD (20). These facts were computed from the actual CSV; the schema and exploration evidence are in `reports/data_profile.json`.

The split is 2011 for training, January–June 2012 for validation, and July–December 2012 for testing. Calendar reindexing occurs before lag construction. Seven initial days and seven days affected by the missing observation are excluded, leaving 348 training, 182 validation, and 184 test observations. Both feature variants use exactly these rows. Ridge uses a training-fitted standard scaler and alpha 1; gradient boosting uses random seed 0 and 300 iterations. The before variant has 14 features; the after variant has 15.

The new feature, `cnt_std_7`, measures population standard deviation over the previous seven calendar days. For a prediction on February 15, its inputs are February 8–14. Its hand-calculated test was written and committed before implementation; the initial KeyError and subsequent passing checks are recorded in `docs/SEEDED_FAULTS.md`. No longer warm-up was necessary. The availability argument assumes yesterday's count is final when today's prediction is made.

The table is generated from `reports/metrics.json`; MAE is measured in rides per day. Top-level model entries are the final feature set, and `before_feature` contains the matched-row ablation. Both are the untransformed target pipeline.

| Feature set | Model | Validation R² | Validation MAE | Test R² | Test MAE |
|---|---|---:|---:|---:|---:|
| Before | baseline_mean | -0.9318 | 2002.2 | -2.1441 | 2847.7 |
| Before | baseline_persistence | 0.4507 | 900.6 | 0.5099 | 840.1 |
| Before | ridge | 0.6475 | 832.9 | 0.5833 | 947.1 |
| Before | hgb | 0.2185 | 1296.6 | -0.4975 | 1972.6 |
| After | baseline_mean | -0.9318 | 2002.2 | -2.1441 | 2847.7 |
| After | baseline_persistence | 0.4507 | 900.6 | 0.5099 | 840.1 |
| After | ridge | 0.7224 | 700.4 | 0.6356 | 840.3 |
| After | hgb | 0.0977 | 1381.6 | -0.6959 | 2108.4 |

The feature was retained based on validation: ridge gained 0.0749 R² and reduced MAE by 132.5 rides. It hurt the tree's validation R² by 0.1208. This is evidence for retaining it in the ridge comparison, not a universal claim about volatility features. Selection was recorded in a commit before the final test table was generated. The residual-target experiment below also used validation only. Test results were then computed for the frozen before/after comparison; subsequent regeneration checks verify reproducibility rather than guide changes. The starter's existing contract test itself evaluates test R², so “test untouched” should not be read as a claim that no automated test ever accessed those rows.

Reproduce the table with Python 3.12, `pip install -r requirements.txt`, then `make all`. Run `make test` for verification, and `python -m src.experiments` for the validation-only experiments. Core and transitive pipeline package versions are pinned. The raw CSV retains its starter SHA-256; loading a modified version now raises before modelling.

## Headline finding

The apparently perfect model is invalid: casual plus registered equals total demand exactly, and a least-squares identity check gives a maximum residual of about 9.1e-12. Under the temporal split, the training-mean baseline instead scores test R² -2.1441, persistence scores 0.5099, original ridge scores 0.5833, and original gradient boosting scores -0.4975. The observed annual mean rises from 3427.3 to 5599.9 rides, about 63.4%; 56.5% of test observations exceed the training maximum of 6043. Tree leaf predictions average training responses and cannot extrapolate beyond that range, which helps explain their failure under growth. After adding volatility, ridge reaches R² 0.6356 while the tree falls to -0.6959; despite its negative R², the tree still beats the training-mean baseline. The feature is retained because of the earlier validation gain; its final test gain is 0.0523 R² and its MAE reduction is 106.8 rides.

These are retrospective scores conditional on observed same-day weather. Daily temperature, humidity, wind, and weather severity are not generally known before the day begins. A prospective deployment needs forecast weather or lagged weather and another evaluation; these numbers should not be presented as demonstrated operational forecasting accuracy. Likewise, persistence and rolling features use actual observations as each test day arrives. This is a rolling one-day prediction protocol, not a single forecast of all six months issued in June.

## Exercise 4: target transformation

I evaluated an additive residual target: z(t) = cnt(t) - cnt(t-1). Fit the tree on training z and reconstruct demand as predicted z(t) + cnt(t-1). The code is in `src/experiments.py`, with outputs in `reports/validation_experiments.json`. Yesterday's demand supplies a moving level, so the reconstructed prediction can exceed the original training maximum even when the predicted change stays within the tree's learned range. Neither a future target nor a validation-fitted transformer is needed.

With the final feature set, the residual tree achieves validation R² 0.5642 and MAE 885.8, compared with ordinary tree 0.0977/1381.6, persistence 0.4507/900.6, and ridge 0.7224/700.4. It substantially closes the gap with ridge but does not beat it. I tested this one prespecified transformation rather than searching for a winning target. Its availability is defensible for rolling one-day predictions with observed yesterday demand; it is unavailable for later horizons of a fixed-origin forecast without recursively predicted counts, which would require separate evaluation. Its improvement also partly reflects building persistence into the prediction, so comparison against persistence remains essential. I have not evaluated or selected this transformation on test. The committed headline metrics remain untransformed.

## Exercise 5: ridge vs persistence

I would retain persistence as the operational default until the forecast-weather evaluation and a decision-specific loss justify ridge. Before the new feature, ridge improves test R² by 0.0734 over persistence but increases MAE from 840.1 to 947.1 rides, a 107.0-ride penalty. After the feature, ridge improves test R² by 0.1257 while MAE is almost tied: 840.3 versus 840.1. The larger R² gain indicates lower squared error, which may matter if large demand misses are especially costly; the MAE comparison supplies little evidence of a typical daily-error advantage. Ridge's validation performance is encouraging, but one short future period does not establish operational superiority. A deployment choice needs the user's cost function and a valid weather information set. The assignment results support continued evaluation, not an unconditional deployment recommendation.

## Attribution

The work followed the assignment’s test-first feature, verification, seeded-fault, and validation workflows.

Agent-generated work:

- The agent wrote the volatility feature, new tests, hash guard, validation experiment, before/after metric generation, seed-fault skill, evidence documents, and this draft report.
- The agent ran the core pipeline, all tests, the three reversible source faults, direct hook invocations, and the Bash-copy bypass in a disposable copy. The agent preserved chronological commits using an external Git directory because workspace policy blocked `.git` creation.
- The original pipeline, reviewer, hook wiring, new-feature skill, and SDK auditor came from the starter. A fresh independent reviewer audited the teammate repository using the starter checklist; its output and evidence are in `docs/AUDIT.md`. The SDK attempt failed on missing `claude_agent_sdk`; `docs/AUDIT.md` records its actual output. The required `reports/audit.jsonl` is still pending.

Human decisions and remaining work:

- After reviewing the report and decision log, the user accepted retaining the volatility feature, the conditional validity of the residual-target transformation, and the recommendation to keep persistence as the deployment default pending forecast-weather validation.
- Target, forbidden columns, split, and baselines were provided by the assignment/starter. The agent proposed the feature, transformation, and deployment interpretation; the user reviewed and endorsed those conclusions afterward, as recorded in `docs/DECISIONS.md`.
- The repository is published at https://github.com/aathijmuthu/bikeshare-open. The teammate audit evidence is recorded in `docs/AUDIT.md`; the student’s verdict review and a successful own-repository SDK audit remain pending. After completing and committing that evidence, submit the repository URL through the course form.
