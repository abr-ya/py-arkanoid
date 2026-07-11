from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

MAX_LEADERBOARD_RECORDS = 10
DEFAULT_LEADERBOARD_PATH = Path("leaderboard.json")


@dataclass(frozen=True, slots=True)
class LeaderboardRecord:
    name: str
    score: int
    timestamp: str

    @classmethod
    def create(cls, name: str, score: int, timestamp: datetime | None = None) -> LeaderboardRecord:
        created_at = timestamp or datetime.now(UTC)
        return cls(
            name=_normalize_name(name),
            score=max(0, int(score)),
            timestamp=created_at.isoformat(),
        )

    @classmethod
    def from_json(cls, data: object) -> LeaderboardRecord:
        if not isinstance(data, dict):
            raise ValueError("Leaderboard record must be an object.")

        name = data.get("name")
        score = data.get("score")
        timestamp = data.get("timestamp")
        if not isinstance(name, str) or not isinstance(score, int) or not isinstance(timestamp, str):
            raise ValueError("Leaderboard record has invalid fields.")

        return cls(name=_normalize_name(name), score=max(0, score), timestamp=timestamp)

    def to_json(self) -> dict[str, object]:
        return {
            "name": self.name,
            "score": self.score,
            "timestamp": self.timestamp,
        }


class LeaderboardStore:
    def __init__(self, path: Path | str = DEFAULT_LEADERBOARD_PATH) -> None:
        self.path = Path(path)

    def load_records(self) -> list[LeaderboardRecord]:
        try:
            raw = self.path.read_text(encoding="utf-8")
        except OSError:
            return []

        if not raw.strip():
            return []

        try:
            payload = json.loads(raw)
            records = _records_from_payload(payload)
        except (json.JSONDecodeError, ValueError):
            return []

        return sort_records(records)

    def save_records(self, records: list[LeaderboardRecord]) -> list[LeaderboardRecord]:
        sorted_records = sort_records(records)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        payload = {"records": [record.to_json() for record in sorted_records]}
        self.path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        return sorted_records

    def add_record(self, record: LeaderboardRecord) -> list[LeaderboardRecord]:
        return self.save_records([*self.load_records(), record])


def sort_records(records: list[LeaderboardRecord]) -> list[LeaderboardRecord]:
    return sorted(records, key=lambda record: record.score, reverse=True)[:MAX_LEADERBOARD_RECORDS]


def _records_from_payload(payload: Any) -> list[LeaderboardRecord]:
    if not isinstance(payload, dict):
        raise ValueError("Leaderboard payload must be an object.")

    records = payload.get("records")
    if not isinstance(records, list):
        raise ValueError("Leaderboard payload must contain a records array.")

    return [LeaderboardRecord.from_json(record) for record in records]


def _normalize_name(name: str) -> str:
    normalized = name.strip().upper()[:3]
    return normalized or "AAA"
