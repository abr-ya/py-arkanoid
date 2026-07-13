from __future__ import annotations

import argparse

from arkanoid.core.game import create_session
from arkanoid.pygame_app import run
from arkanoid.resources import leaderboard_path, levels_dir


def main() -> None:
    parser = argparse.ArgumentParser(prog="py-arkanoid")
    parser.add_argument(
        "--smoke",
        action="store_true",
        help="load runtime resources and exit without opening the game window",
    )
    args = parser.parse_args()
    if args.smoke:
        session = create_session()
        print(
            "arkanoid smoke ok: "
            f"level={session.level.number} "
            f"levels_dir={levels_dir()} "
            f"leaderboard={leaderboard_path()}"
        )
        return
    run()


if __name__ == "__main__":
    main()
