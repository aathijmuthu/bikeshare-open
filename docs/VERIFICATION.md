# Final verification — 2026-11-25

A fresh checkout from the preserved Git history was created at `/tmp/bikeshare-clean-verification`. It used the verified Python 3.12 virtual environment, with OMP_NUM_THREADS=1 (limits runtime threads; does not change the model parameters).

- `make all`: exit 0.
- `cmp reports/metrics.json /tmp/bikeshare-clean-verification/reports/metrics.json`: exit 0; byte-identical output.
- `make test` in the fresh checkout: `19 passed in 0.80s`.
- `python -m pip check`: `No broken requirements found.`
- Raw SHA-256: `a6bed1577f6e4de56dcfae6d8315985073cc0ad3446c8c99ed60c86a0b5ad9dc`.
- CLAUDE.md: 45 lines (under the 60-line requirement).

This verifies a fresh source checkout using the installed core dependency environment. It does not claim a fresh network installation of the entire requirements file: the Claude Agent SDK remains uninstalled and its audit remains pending. See AUDIT.md and REMAINING.md.
