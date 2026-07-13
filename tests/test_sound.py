from arkanoid.core.events import SoundEvent
from arkanoid.core.game import create_session
from arkanoid.pygame_app import _dispatch_sound_events
from arkanoid.sound import NoOpSoundService, sound_enabled


class FakeSoundService:
    def __init__(self) -> None:
        self.played: list[SoundEvent] = []

    def play(self, event: SoundEvent) -> None:
        self.played.append(event)


def test_dispatch_sound_events_uses_service_and_clears_queue() -> None:
    session = create_session()
    sound_service = FakeSoundService()
    session.sound_events = [SoundEvent.LAUNCH, SoundEvent.COLLISION]

    _dispatch_sound_events(session, sound_service)
    _dispatch_sound_events(session, sound_service)

    assert sound_service.played == [SoundEvent.LAUNCH, SoundEvent.COLLISION]
    assert session.pull_sound_events() == []


def test_noop_sound_service_accepts_any_event() -> None:
    NoOpSoundService().play(SoundEvent.BRICK_BREAK)


def test_sound_can_be_disabled_by_environment(monkeypatch) -> None:
    monkeypatch.setenv("ARKANOID_SOUND", "0")

    assert not sound_enabled()
