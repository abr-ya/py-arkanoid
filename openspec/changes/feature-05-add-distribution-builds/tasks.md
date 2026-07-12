## 1. Resource Paths

- [ ] 1.1 Add a resource resolver for development and packaged execution.
- [ ] 1.2 Update level, asset, and leaderboard path usage to go through the resolver.

## 2. Build Scripts

- [ ] 2.1 Add Windows PyInstaller build script.
- [ ] 2.2 Add Linux PyInstaller build script.
- [ ] 2.3 Include levels, assets, and local runtime data defaults in packaged builds.
- [ ] 2.4 Add a GitHub Actions workflow that builds and uploads the Windows `.exe` artifact.
- [ ] 2.5 Add or document a Linux tarball artifact for Ubuntu and Linux Mint.

## 3. Linux Installer Decision

- [ ] 3.1 Compare `.deb`, AppImage, and tarball for this project.
- [ ] 3.2 Implement only the selected low-risk format in this slice, or record installer packaging as a follow-up.

## 4. Documentation And Verification

- [ ] 4.1 Add README instructions for development run, local packaged builds, and CI artifact downloads.
- [ ] 4.2 Add a manual smoke checklist for packaged artifacts.
- [ ] 4.3 Verify Linux build locally when environment allows.
- [ ] 4.4 Document Windows build verification through GitHub Actions if it cannot be run locally.
