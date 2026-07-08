# Agent Collaboration Guide

This repo values low-token, user-assisted collaboration. Prefer the smallest
useful context pass before acting.

## Token Economy

- Start from the selected OpenSpec change: run `openspec list --json` only when
  the active change is unclear, then use `openspec status --change <name> --json`
  and `openspec instructions apply --change <name> --json`.
- Read the `contextFiles` returned by OpenSpec before reading broader repo
  files.
- Ask the user for missing context instead of searching broadly when the needed
  information is not clearly discoverable from the selected change.
- When a command is useful but can be run by the user, provide the exact command
  and explain what output is needed instead of running it automatically.
- Keep progress updates short. Report the current task, blocker, or result; do
  not restate the full OpenSpec workflow unless asked.
- Prefer focused diffs and focused verification. Avoid unrelated refactors,
  broad file scans, and full test runs unless the change risk requires them or
  the user asks.
- If a verification step is skipped because the user will run it, record that in
  the final handoff.

## OpenSpec Defaults

- Treat `openspec/backlog.md` as the navigation point for planned work.
- Treat `openspec/changes/<change-name>/` as the source of truth while a feature
  is active.
- Treat `openspec/specs/` as accepted product behavior after implementation and
  archive.
- Before implementing a later feature, review only the feature's artifacts plus
  the code touched by earlier changes unless there is a concrete reason to read
  more.
