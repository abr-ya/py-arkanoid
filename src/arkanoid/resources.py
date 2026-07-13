from __future__ import annotations

import os
import sys
from pathlib import Path

APP_DIR_NAME = "py-arkanoid"


def is_frozen() -> bool:
    return bool(getattr(sys, "frozen", False))


def project_root() -> Path:
    return Path(__file__).resolve().parents[2]


def resource_root() -> Path:
    bundle_root = getattr(sys, "_MEIPASS", None)
    if bundle_root:
        return Path(bundle_root)
    return project_root()


def resource_path(*parts: str) -> Path:
    return resource_root().joinpath(*parts)


def levels_dir() -> Path:
    return resource_path("levels")


def sounds_dir() -> Path:
    return resource_path("src", "arkanoid", "assets", "sounds")


def user_data_dir() -> Path:
    override = os.environ.get("ARKANOID_DATA_DIR")
    if override:
        return Path(override).expanduser()
    if not is_frozen():
        return Path.cwd()

    if sys.platform == "win32":
        base = os.environ.get("APPDATA")
        if base:
            return Path(base) / APP_DIR_NAME
    elif sys.platform == "darwin":
        return Path.home() / "Library" / "Application Support" / APP_DIR_NAME

    base = os.environ.get("XDG_DATA_HOME")
    if base:
        return Path(base) / APP_DIR_NAME
    return Path.home() / ".local" / "share" / APP_DIR_NAME


def leaderboard_path() -> Path:
    return user_data_dir() / "leaderboard.json"
