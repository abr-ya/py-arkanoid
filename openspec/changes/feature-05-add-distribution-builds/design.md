## Context

The broad original plan included Windows and Linux binaries. Packaging now moves ahead of polish so the game can be shared early, while the remaining feature work can still improve the packaged experience incrementally.

## Goals / Non-Goals

**Goals:**

- Build one executable file per target platform.
- Build the Windows `.exe` through GitHub Actions on a Windows runner.
- Build or document a Linux artifact that works on common Ubuntu and Linux Mint environments.
- Package levels and assets with the executable.
- Document reproducible build commands.
- Decide whether a Linux installer format belongs in this slice.

**Non-Goals:**

- Cross-compiling Windows binaries from Linux.
- Full Linux installer polish unless the selected package format is small enough for this slice.
- Code signing.

## Decisions

### Build tool

Use PyInstaller first because it is common for Pygame projects and matches the original plan. Nuitka can be evaluated later if artifact size or startup time becomes a problem.

### Platform builds

Build Windows artifacts on Windows and Linux artifacts on Linux. Avoid promising cross-compilation.

### GitHub Actions

Add CI packaging for Windows first because it removes the need for a local Windows machine. The workflow should upload the `.exe` or zipped artifact for manual download. Linux CI can be included if dependency installation and SDL runtime needs stay simple.

### Linux packaging options

Start with a portable tarball containing the Linux executable and any support files. Document `.deb` for Ubuntu/Linux Mint as the most natural installer follow-up, and AppImage as a possible later option if a single-file desktop-style package becomes more important than repository-native packaging.

### Resource resolution

Centralize resource-path lookup so development runs and packaged runs can both find levels, assets, and leaderboard storage.

## Risks / Trade-offs

- [Risk] PyInstaller asset paths differ from development paths. -> Mitigation: add a resource resolver and package smoke checks.
- [Risk] Windowed packaged apps can hide errors. -> Mitigation: keep a console/debug build option for troubleshooting.
- [Risk] GitHub Actions artifacts may pass build but fail on a real desktop. -> Mitigation: include manual smoke checklist and keep local source runs unchanged.
- [Risk] Linux installer formats add packaging churn. -> Mitigation: ship tarball first, then make `.deb` or AppImage a follow-up if needed.
