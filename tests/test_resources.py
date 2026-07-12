import sys

from arkanoid import resources


def test_development_resource_paths_use_project_root() -> None:
    assert resources.resource_path("levels").name == "levels"
    assert (resources.resource_path("levels") / "level_01.yaml").exists()


def test_development_leaderboard_path_uses_current_working_directory(monkeypatch, tmp_path) -> None:
    monkeypatch.chdir(tmp_path)
    monkeypatch.delenv("ARKANOID_DATA_DIR", raising=False)
    monkeypatch.setattr(sys, "frozen", False, raising=False)

    assert resources.leaderboard_path() == tmp_path / "leaderboard.json"


def test_frozen_resource_paths_use_pyinstaller_meipass(monkeypatch, tmp_path) -> None:
    monkeypatch.setattr(sys, "_MEIPASS", str(tmp_path), raising=False)

    assert resources.resource_path("levels") == tmp_path / "levels"
