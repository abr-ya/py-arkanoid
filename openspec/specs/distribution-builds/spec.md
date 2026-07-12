## Purpose

Define platform packaging, CI artifact generation, bundled resource handling,
and Linux distribution decisions for shareable Arkanoid builds.

## Requirements

### Requirement: Game builds into platform executable artifacts
The system SHALL provide scripts or documented commands to build a Windows `.exe` and a Linux executable using PyInstaller.

#### Scenario: Build Windows artifact
- **WHEN** the Windows build script runs on Windows with dependencies installed
- **THEN** it creates a runnable `arkanoid.exe` artifact

#### Scenario: Build Windows artifact in CI
- **WHEN** the GitHub Actions build workflow runs on a Windows runner
- **THEN** it uploads a downloadable Windows `.exe` or zipped Windows artifact

#### Scenario: Build Linux artifact
- **WHEN** the Linux build script runs on Linux with dependencies installed
- **THEN** it creates a runnable `arkanoid` artifact

### Requirement: Packaged artifacts include runtime resources
The build process SHALL include required levels and assets in packaged artifacts.

#### Scenario: Run packaged game
- **WHEN** the packaged game starts
- **THEN** it can load bundled levels and assets

### Requirement: Linux distribution path is documented
The build documentation SHALL explain the selected Linux distribution artifact for Ubuntu and Linux Mint and SHALL record whether `.deb` or AppImage packaging is included now or deferred.

#### Scenario: Read Linux packaging decision
- **WHEN** a developer reads the distribution docs
- **THEN** they can identify how to build and share the Linux artifact
- **AND** they can see whether installer packaging is current scope or a follow-up

### Requirement: Build documentation explains platform limits
The documentation SHALL explain that artifacts are built on their target platform unless a supported CI workflow is added.

#### Scenario: Read build docs
- **WHEN** a developer reads the build instructions
- **THEN** they can identify which platform is required for each artifact
