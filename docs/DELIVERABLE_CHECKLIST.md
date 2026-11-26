# Deliverables and grading check — 2026-11-25

Source: https://dsc-capstone.org/2026-27/assignments/methodology/07-open/ (re-fetched for this check).

This is an evidence checklist, not a predicted grade or a claim that substitute execution methods satisfy every literal requirement.

| Rubric item | Points | Evidence and status |
|---|---:|---|
| Reproducible repository | 15 | Verified on this Mac: complete requirements installed in a fresh Python 3.12 environment, make all succeeds, metrics reproduce byte for byte, dependency versions pinned, generated artifacts ignored. See VERIFICATION.md and FULL_INSTALL_VERIFICATION.txt. |
| CLAUDE.md | 10 | Updated for the volatility rule and seed-fault skill; includes forbidden columns, temporal split, both baselines and pipeline commands; 45 lines. |
| Verification suite | 25 | 19 tests pass. Feature test committed before implementation; named-date hand calculation, raw-column classification, original split/row-loss tests, exact fault diffs and failing output present. Four fault experiments recorded; interactive harness turn counts were not measured. |
| Results with baselines | 20 | Eight before/after rows and all 32 numeric cells match metrics.json. Both models/baselines, negative scores, feature decision, target transformation, and ridge/persistence argument included. Feature selection recorded using validation before final test comparison. Existing starter test accesses test rows; report discloses this. |
| Structural enforcement | 10 | Starter hook/permissions retained; direct hook stderr for all three source faults saved. Bash-copy bypass tested in disposable copy, and raw hash protection implemented. Automatic harness dispatch was not verified. |
| Agent configuration | 10 | Authored argument-taking skill, peer URL/commit, fresh independent reviewer output, accepted student verdict, and actual one-line own-review JSON exist. Original execution method differs: no completed slash-command peer run or model-driven SDK batch audit. A real SDK retry timed out; the structured artifact truthfully identifies independent agent execution. |
| Decisions and attribution | 10 | Starter decisions retained, dated changes and user endorsements recorded, separate starter/test/feature/fault/audit/report commits preserved. Attribution describes generated work and accepted human conclusions. It identifies expected assignment configuration, rather than the actual model used, so the literal actual-model/size/context identification requirement remains unmet. |

## Original execution requirements still not demonstrated

- Successful `python agent/audit.py . --out reports/audit.jsonl` model-driven SDK run. The existing file is a successful independent agent review with explicit execution metadata, not SDK output.
- Literal `/leakage-auditor` execution for the peer audit and automatic harness delivery of hook failures/interactive repair counts. Fresh independent reviews and direct hook tests provide substitute evidence.
- Actual model identification at the beginning of Attribution. Reference configuration is explicitly labeled expected setup, not claimed execution.

## Publication and submission

The public GitHub repository was confirmed at 644a37c before this final documentation commit. New verification/checklist/report edits are local until pushed. A push from the agent sandbox was denied by SSH authentication; push from the regular terminal with `git -C /tmp/bikeshare-open-submission push origin main`.

The final report update follows the successful independent-audit commit, preserving the required audit-then-report order. Keep the original history; do not squash. Submit the public repository URL through the course form after resolving or accounting for the original execution requirements. Course submission has not been performed.
