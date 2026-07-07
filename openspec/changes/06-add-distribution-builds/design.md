## Context

The broad original plan included Windows and Linux binaries. Packaging should happen after gameplay and data paths are stable enough to avoid repeated build churn.

## Goals / Non-Goals

**Goals:**

- Build one executable file per target platform.
- Package levels and assets with the executable.
- Document reproducible build commands.

**Non-Goals:**

- Cross-compiling Windows binaries from Linux.
- Installer creation.
- Code signing.

## Decisions

### Build tool

Use PyInstaller first because it is common for Pygame projects and matches the original plan. Nuitka can be evaluated later if artifact size or startup time becomes a problem.

### Platform builds

Build Windows artifacts on Windows and Linux artifacts on Linux. Avoid promising cross-compilation.

### Resource resolution

Centralize resource-path lookup so development runs and packaged runs can both find levels, assets, and leaderboard storage.

## Risks / Trade-offs

- [Risk] PyInstaller asset paths differ from development paths. -> Mitigation: add a resource resolver and package smoke checks.
- [Risk] Windowed packaged apps can hide errors. -> Mitigation: keep a console/debug build option for troubleshooting.
