## ADDED Requirements

### Requirement: Game builds into platform executable artifacts
The system SHALL provide scripts or documented commands to build a Windows `.exe` and a Linux executable using PyInstaller.

#### Scenario: Build Windows artifact
- **WHEN** the Windows build script runs on Windows with dependencies installed
- **THEN** it creates a runnable `arkanoid.exe` artifact

#### Scenario: Build Linux artifact
- **WHEN** the Linux build script runs on Linux with dependencies installed
- **THEN** it creates a runnable `arkanoid` artifact

### Requirement: Packaged artifacts include runtime resources
The build process SHALL include required levels and assets in packaged artifacts.

#### Scenario: Run packaged game
- **WHEN** the packaged game starts
- **THEN** it can load bundled levels and assets

### Requirement: Build documentation explains platform limits
The documentation SHALL explain that artifacts are built on their target platform unless a supported CI workflow is added.

#### Scenario: Read build docs
- **WHEN** a developer reads the build instructions
- **THEN** they can identify which platform is required for each artifact
