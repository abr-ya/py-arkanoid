## 1. Resource Paths

- [x] 1.1 Add a resource resolver for development and packaged execution.
- [x] 1.2 Update level, asset, and leaderboard path usage to go through the resolver.

## 2. Build Scripts

- [x] 2.1 Add Windows PyInstaller build script.
- [x] 2.2 Add Linux PyInstaller build script.
- [x] 2.3 Include levels, assets, and local runtime data defaults in packaged builds.
- [x] 2.4 Add a GitHub Actions workflow that builds and uploads the Windows `.exe` artifact.
- [x] 2.5 Add or document a Linux tarball artifact for Ubuntu and Linux Mint.

## 3. Linux Installer Decision

- [x] 3.1 Compare `.deb`, AppImage, and tarball for this project.
- [x] 3.2 Implement only the selected low-risk format in this slice, or record installer packaging as a follow-up.

## 4. Documentation And Verification

- [x] 4.1 Add README instructions for development run, local packaged builds, and CI artifact downloads.
- [x] 4.2 Add a manual smoke checklist for packaged artifacts.
- [x] 4.3 Verify Linux build locally when environment allows.
- [x] 4.4 Document Windows build verification through GitHub Actions if it cannot be run locally.
