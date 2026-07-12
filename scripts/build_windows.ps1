$ErrorActionPreference = "Stop"

$Root = Resolve-Path (Join-Path $PSScriptRoot "..")
Set-Location $Root

python -c "import PyInstaller" 2>$null
if ($LASTEXITCODE -ne 0) {
    python -m pip install -e ".[build]"
}
python scripts/build_pyinstaller.py --clean

$ArtifactDir = Join-Path $Root "dist\windows"
New-Item -ItemType Directory -Force -Path $ArtifactDir | Out-Null
Copy-Item -Force "dist\arkanoid.exe" (Join-Path $ArtifactDir "arkanoid.exe")

Write-Host "Windows artifact: dist\windows\arkanoid.exe"
