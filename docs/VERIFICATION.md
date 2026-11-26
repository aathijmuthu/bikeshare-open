# Final verification — 2026-11-25

A fresh checkout at commit 644a37c was created in /tmp/bikeshare-full-install-source, with a new Python 3.12 environment at /tmp/bikeshare-full-install-venv. All dependencies in requirements.txt, including claude-agent-sdk==0.2.172, were installed successfully. Because pip's direct network access is blocked in this sandbox, official PyPI wheels and metadata were fetched through permitted curl calls, and pip resolved/installed them using --no-index --find-links. No dependency requirement was removed or bypassed. This checks fresh installation from official wheels on this Mac, not every OS/Python combination.

- `make all`: exit 0; reports/metrics.json byte-identical to the committed artifact.
- `make test`: 19 passed; exit 0.
- `python -m src.experiments`: exit 0; reports/validation_experiments.json byte-identical to the committed artifact.
- `python -m pip check`: no broken requirements; exit 0.
- SDK import succeeds; project/local setting sources supported.
- Actual SDK-decorated identity tool handles CSV/Parquet leaked and clean examples correctly, and rejects relative paths.
- jsonschema validates the saved independent-agent audit JSON against REPORT_SCHEMA.
- All 12 required paths exist, exactly five report sections and eight result rows are present, and all 32 numeric cells match metrics.json.
- CLAUDE.md is 45 lines; all starter files remain; generated datasets, environments, and caches are untracked.
- Raw SHA-256 remains a6bed1577f6e4de56dcfae6d8315985073cc0ad3446c8c99ed60c86a0b5ad9dc.

Full runtime output: FULL_INSTALL_VERIFICATION.txt. Installed package versions: FULL_INSTALL_ENVIRONMENT.txt.

The earlier independent-review environment did not contain the SDK; its original evidence is retained unchanged. This later full installation supersedes that installation limitation, but does not turn the independent review into an SDK batch run. A subsequent SDK attempt using the local endpoint was bounded to 25 seconds and timed out without a completed result; actual warnings/output are in SDK_RETRY.txt. Neither automatic hook dispatch nor interactive harness repair turns have been verified.
