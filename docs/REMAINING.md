# Remaining steps before submission

The core implementation and report draft are complete; required audit evidence and human decisions are pending.

1. The report uses the assignment’s workflow terminology and names the actual model in Attribution.
2. Supply your teammate's repository URL. Run the `.claude/agents/leakage-auditor.md` reviewer in a fresh Claude Code context against that repo, paste its output verbatim into docs/AUDIT.md, then write your own verdict about findings that change a number.
3. Install requirements, configure Ollama/Claude Code using README.md, run `make check-model`, then `python agent/audit.py . --out reports/audit.jsonl`. Check that this is a successful schema-compliant audit, address/explain findings, and commit the real output. The recorded attempt currently fails because the SDK is missing; neither model runtime is installed.
4. The hook script was tested by direct invocation. Reproduce Edit/Write hook dispatch in Claude Code and record actual repair turns if the instructor requires the specified harness evidence. The Bash-copy experiment used a disposable copy to preserve the submission's immutable CSV.
5. Read REPORT.md and docs/DECISIONS.md. Endorse or revise feature retention, transformation availability, the forecast-weather caveat, and the ridge/persistence deployment argument. Replace pending attribution with only decisions you actually make. Supply your name if desired. Do not claim agent proposals as prior personal decisions.
6. The workspace forbids creating `.git`, so the full required commit sequence is in `bikeshare-assignment.bundle`. Recover a normal repo in a new directory from your own terminal:

   ```sh
   git clone /absolute/path/to/bikeshare-open-starter/bikeshare-assignment.bundle bikeshare-open
   cd bikeshare-open
   python3.12 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   make all
   make test
   ```

   The first commit is the unmodified starter; do not squash the history. Do remaining work in this recovered repository and commit audit evidence and your revisions. The original starter folder contains the same final files but no local `.git` directory.
7. Create a GitHub repository, push the recovered history, verify access for graders, and submit its URL through the course form. No repository has been published or submitted by the agent.

See docs/AUDIT.md for real failure output. reports/audit.jsonl is absent deliberately; it is a required unfinished deliverable.
