"""Validation-only feature ablation and residual-target experiment."""
import json
from sklearn.base import clone
from sklearn.metrics import r2_score, mean_absolute_error
from src.features import build_features, feature_columns
from src.ingest import load_raw
from src.train import temporal_split, MODELS
from src.config import TARGET, ROOT


def score(y, prediction):
    return {'r2': round(float(r2_score(y, prediction)), 4),
            'mae': round(float(mean_absolute_error(y, prediction)), 1)}


def run():
    df = build_features(load_raw())
    train, valid, _ = temporal_split(df)
    cols = feature_columns(df)
    result = {}
    for label, columns in [('before', [c for c in cols if c != 'cnt_std_7']), ('after', cols)]:
        result[label] = {}
        for name, prototype in MODELS.items():
            model = clone(prototype).fit(train[columns], train[TARGET])
            result[label][name] = score(valid[TARGET], model.predict(valid[columns]))
    # Pre-specified additive residual: predict today's change from yesterday.
    # Inverse transform uses yesterday's observed demand, available one day ahead.
    tree = clone(MODELS['hgb']).fit(train[cols], train[TARGET] - train.cnt_lag_1)
    prediction = tree.predict(valid[cols]) + valid.cnt_lag_1
    result['residual_hgb_valid'] = score(valid[TARGET], prediction)
    path = ROOT / 'reports' / 'validation_experiments.json'
    path.parent.mkdir(exist_ok=True)
    path.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))

if __name__ == '__main__':
    run()
