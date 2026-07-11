import json
from datetime import UTC, datetime

from arkanoid.core.leaderboard import LeaderboardRecord, LeaderboardStore, sort_records


def test_leaderboard_record_serializes_to_json() -> None:
    timestamp = datetime(2026, 7, 11, 12, 30, tzinfo=UTC)
    record = LeaderboardRecord.create("ab", 250, timestamp)

    assert record.to_json() == {
        "name": "AB",
        "score": 250,
        "timestamp": "2026-07-11T12:30:00+00:00",
    }


def test_sort_records_keeps_top_ten_scores_descending() -> None:
    records = [
        LeaderboardRecord(name=f"P{index}", score=index * 100, timestamp="2026-07-11T00:00:00+00:00")
        for index in range(12)
    ]

    sorted_records = sort_records(records)

    assert [record.score for record in sorted_records] == [
        1100,
        1000,
        900,
        800,
        700,
        600,
        500,
        400,
        300,
        200,
    ]


def test_leaderboard_store_loads_missing_empty_and_corrupted_files_as_empty(tmp_path) -> None:
    missing_store = LeaderboardStore(tmp_path / "missing.json")
    assert missing_store.load_records() == []

    empty_path = tmp_path / "empty.json"
    empty_path.write_text("", encoding="utf-8")
    assert LeaderboardStore(empty_path).load_records() == []

    corrupted_path = tmp_path / "corrupted.json"
    corrupted_path.write_text("{not json", encoding="utf-8")
    assert LeaderboardStore(corrupted_path).load_records() == []
    assert corrupted_path.read_text(encoding="utf-8") == "{not json"


def test_leaderboard_store_saves_records_as_top_ten_json(tmp_path) -> None:
    store = LeaderboardStore(tmp_path / "leaderboard.json")
    records = [
        LeaderboardRecord(name=f"P{index}", score=index, timestamp="2026-07-11T00:00:00+00:00")
        for index in range(12)
    ]

    saved = store.save_records(records)
    payload = json.loads((tmp_path / "leaderboard.json").read_text(encoding="utf-8"))

    assert [record.score for record in saved] == list(range(11, 1, -1))
    assert [record["score"] for record in payload["records"]] == list(range(11, 1, -1))


def test_leaderboard_store_adds_record_to_existing_scores(tmp_path) -> None:
    store = LeaderboardStore(tmp_path / "leaderboard.json")
    store.save_records(
        [
            LeaderboardRecord(name="AAA", score=100, timestamp="2026-07-11T00:00:00+00:00"),
            LeaderboardRecord(name="BBB", score=300, timestamp="2026-07-11T00:00:00+00:00"),
        ]
    )

    records = store.add_record(
        LeaderboardRecord(name="CCC", score=200, timestamp="2026-07-11T00:00:00+00:00")
    )

    assert [(record.name, record.score) for record in records] == [
        ("BBB", 300),
        ("CCC", 200),
        ("AAA", 100),
    ]
