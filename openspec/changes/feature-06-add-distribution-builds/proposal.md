## Why

After the game is playable, it should be easy to share with people who do not have Python installed. This change packages the game into platform-specific single-file artifacts.

## What Changes

- Add PyInstaller-based build scripts for Windows and Linux.
- Include level files and assets in packaged builds.
- Document local run and packaged run flows.
- Add smoke checks for packaged artifacts where possible.

## Capabilities

### New Capabilities

- `distribution-builds`: Platform-specific packaged builds and build documentation.

### Modified Capabilities

None.

## Impact

- Adds build scripts and PyInstaller dependency.
- May adjust asset and data path resolution.
- Does not guarantee cross-compilation; each platform builds its own artifact.
