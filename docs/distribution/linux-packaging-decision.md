# Linux Packaging Decision

## Decision

Ship a portable PyInstaller tarball for this slice.

The first Linux artifact is `dist/arkanoid-linux.tar.gz`, produced by
`scripts/build_linux.sh`. It contains the packaged `arkanoid` executable and is
the lowest-risk option for Ubuntu and Linux Mint while the game is still moving.

## Options Considered

### Tarball

- Lowest packaging overhead.
- Works naturally with a PyInstaller one-file executable.
- Easy to produce locally and in CI.
- Does not provide desktop-menu integration.

### `.deb`

- Natural installer format for Ubuntu and Linux Mint.
- Can add desktop entries and icons later.
- Requires package metadata, install paths, and maintainer scripts.
- Better as a follow-up once icons, app metadata, and release naming settle.

### AppImage

- Friendly single-file desktop distribution.
- Useful if the project needs Linux desktop portability beyond Debian-family systems.
- Adds extra tooling and runtime packaging decisions.
- Better as a later distribution-polish slice if tarball sharing is not enough.

## Follow-Up

Add `.deb` packaging first if users need a real installer for Ubuntu/Linux Mint.
Consider AppImage later if a portable desktop artifact becomes more valuable.
