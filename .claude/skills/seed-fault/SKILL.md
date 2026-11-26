---
name: seed-fault
description: Reproduce one reversible methodology fault and record real test and hook output.
allowed-tools: Read, Edit, Write, Bash
---

For $ARGUMENTS (forbidden, rolling, or weather):
1. Start with passing tests and save the original source bytes. Never change raw data.
2. Change only the requested fault: include registered in feature_columns, remove the shift before cnt_roll_7, or suppress the unknown-weather ValueError.
3. Run `make test`; save stdout, stderr, and exit status, without claiming a pass.
4. Feed the edited file path as JSON tool_input.file_path to `.claude/hooks/check_leakage.sh`; save stderr and exit status. Direct invocation tests the hook script, not Claude Code dispatch.
5. Restore the saved source in a finally block. Run `make test` again.
6. Append the exact diff, captured outputs, and actual repair count to docs/SEEDED_FAULTS.md. Never invent agent turns or a Claude session.
7. Commit the experiment with the fault and restoration described in the message.
