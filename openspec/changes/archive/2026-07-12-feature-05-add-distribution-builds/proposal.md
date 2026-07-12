## Why

After the game is playable and has local records, it should be easy to share with people who do not have Python installed. This change prepares Windows and Linux distribution artifacts before adding more content and feedback polish.

## What Changes

- Add PyInstaller-based build scripts for Windows and Linux.
- Add GitHub Actions workflow support for building the Windows `.exe` on Windows.
- Produce a Linux artifact suitable for Ubuntu and Linux Mint.
- Document whether `.deb` or AppImage packaging should be added now or deferred.
- Include level files and assets in packaged builds.
- Document local run and packaged run flows.
- Add smoke checks for packaged artifacts where possible.

## Capabilities

### New Capabilities

- `distribution-builds`: Platform-specific packaged builds, CI artifacts, Linux packaging options, and build documentation.

### Modified Capabilities

None.

## Impact

- Adds build scripts and PyInstaller dependency.
- Adds CI workflow files if GitHub Actions is selected.
- May adjust asset and data path resolution.
- Does not guarantee cross-compilation; each platform builds its own artifact.
