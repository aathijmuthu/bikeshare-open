# Remaining steps before submission

The repository is public at https://github.com/aathijmuthu/bikeshare-open. The report and methodological decisions were reviewed and accepted by the user. The peer review is complete and recorded at docs/AUDIT.md with exact output and evidence.

1. Review the draft peer-audit verdict in docs/AUDIT.md and endorse or revise it as your own assessment. The independent agent used the starter reviewer checklist; it did not run the Claude Code slash command.
2. Complete the own-repository SDK audit. Install requirements, configure the local runtime using README.md, run `make check-model`, then `python agent/audit.py . --out reports/audit.jsonl`. Inspect the real schema-compliant output, fix or explain any findings, and commit the output. The recorded attempt failed because the SDK was missing; reports/audit.jsonl remains absent.
3. The source-fault hook script was tested by direct invocation. Automatic Edit/Write hook dispatch and interactive repair turns were not measured. Reproduce that evidence in the requested harness if required. The Bash-copy test used a disposable copy to preserve the raw CSV.
4. The normal Git checkout is /tmp/bikeshare-open-submission. Push its new commits from your regular terminal: `git -C /tmp/bikeshare-open-submission push origin main`. The source workspace cannot use the stored SSH key. Its copy of the preserved history is also saved in bikeshare-assignment.bundle; do not squash the history.
5. After completing the remaining audit evidence, run `make all` and `make test`, check the report table against metrics.json, commit/push the final evidence, and submit the public repository URL through the course form. Submission has not been performed.

Keep a durable clone outside /tmp for subsequent work; /tmp is temporary. The workspace still contains the final files and a Git bundle with the full history.
