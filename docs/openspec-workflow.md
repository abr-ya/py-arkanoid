# OpenSpec Workflow

This project uses OpenSpec as a spec-driven workflow for implementing Arkanoid in small, reviewable feature slices.

## Document Roles

Keep roadmap, active changes, and accepted specs separate.

### Roadmap / Backlog

The roadmap is the list of planned features and priorities. It answers:

- What do we want to build next?
- What order should features happen in?
- Which ideas are deferred?

Recommended location:

- `docs/roadmap.md`
- `docs/backlog.md`

The roadmap may mention future work, but it is not the canonical description of what the game already supports.

### Main Specs

Main specs live in:

- `openspec/specs/...`

They describe the current accepted behavior of the product. A feature should appear in main specs only after it has been implemented, checked, and accepted.

Do not put future wishlist behavior directly into main specs. If main specs describe behavior that the code does not support yet, the specs stop being trustworthy.

### Change Specs

Active feature work lives in:

- `openspec/changes/<change-name>/...`

Each change contains the planned delta for one focused feature slice:

- `proposal.md` - why this change exists and what it changes
- `design.md` - how the change will be implemented
- `specs/.../spec.md` - delta specs for requirements added or modified by the change
- `tasks.md` - implementation checklist

## Recommended Branch Workflow

Use one branch per focused OpenSpec change.

```text
main
  docs/roadmap.md
  openspec/specs/...

feature/<change-name>
  openspec/changes/<change-name>/proposal.md
  openspec/changes/<change-name>/design.md
  openspec/changes/<change-name>/specs/.../spec.md
  openspec/changes/<change-name>/tasks.md
  implementation code
```

Suggested flow:

1. Keep the overall roadmap on `main`.
2. Pick the next small feature from the roadmap.
3. Create an OpenSpec change for that feature.
4. Create a matching feature branch.
5. Implement only that feature slice.
6. Mark completed tasks in `tasks.md`.
7. Sync the change's delta specs into `openspec/specs/...`.
8. Archive the completed change.
9. Merge the branch back to `main`.

After merge, `main` should contain:

- implemented code
- updated main specs
- archived change history
- roadmap/backlog updated with the completed item

## Agent Token Economy

Use the project structure to keep agent context small. The detailed
collaboration rules live in [`AGENTS.md`](../AGENTS.md).

Default agent flow:

1. Identify the active change from the user request or `openspec/backlog.md`.
2. Run `openspec status --change <change-name> --json`.
3. Run `openspec instructions apply --change <change-name> --json`.
4. Read only the returned `contextFiles` before touching broader repo context.
5. Ask the user for missing context when a broad search would be speculative.
6. Offer exact commands for the user to run when local/manual verification is
   enough and does not need agent-side execution.
7. Keep updates and handoffs focused on changed files, completed tasks,
   verification, and blockers.

Avoid re-reading the whole repo, re-explaining the workflow, or running broad
test/search commands unless the selected change or a failure makes that
necessary.

## Archive Meaning

Archiving a change does not mean deleting the plan. It means:

- the change has been implemented
- its tasks are complete
- its delta specs have been merged into main specs
- the change has been moved to `openspec/changes/archive/YYYY-MM-DD-<change-name>`

In practical terms, archive means "this feature is now part of the accepted product history."

## Arkanoid Roadmap Shape

Avoid one oversized `open-arkanoid` change that tries to cover the entire future game. Use a roadmap for the whole product and smaller changes for implementation.

Possible slices:

1. `playable-core` - window, paddle, ball, basic bricks, collisions, score, lives, game over
2. `levels-and-brick-types` - YAML levels, brick HP, level clear, progression
3. `local-leaderboard` - local JSON records, top 10, name entry, corruption fallback
4. `powerups` - wide paddle, slow ball, multi-ball, sticky paddle
5. `build-distribution` - PyInstaller/Nuitka scripts and release instructions
6. `online-leaderboard-client` - offline-safe HTTP client for a future server

## Key Rule

Use each artifact for one job:

- roadmap/backlog: planned future work
- `openspec/changes`: proposed active work
- `openspec/specs`: accepted current behavior
- `openspec/changes/archive`: completed change history

This keeps OpenSpec aligned with the project instead of turning the main spec into a wishlist.
