from __future__ import annotations

import os
from pathlib import Path
from typing import Protocol

import pygame

from arkanoid.core.events import SoundEvent
from arkanoid.resources import sounds_dir

SOUND_DISABLED_ENV = "ARKANOID_SOUND"
SOUND_FILES = {
    SoundEvent.LAUNCH: "launch.wav",
    SoundEvent.COLLISION: "collision.wav",
    SoundEvent.BRICK_BREAK: "brick_break.wav",
    SoundEvent.POWER_UP_PICKUP: "power_up_pickup.wav",
    SoundEvent.LEVEL_COMPLETE: "level_complete.wav",
}


class SoundService(Protocol):
    def play(self, event: SoundEvent) -> None:
        ...


class NoOpSoundService:
    def play(self, event: SoundEvent) -> None:
        return


class PygameSoundService:
    def __init__(self, sounds: dict[SoundEvent, pygame.mixer.Sound]) -> None:
        self._sounds = sounds

    @classmethod
    def create(cls, root: Path | None = None) -> SoundService:
        if not sound_enabled():
            return NoOpSoundService()

        try:
            if not pygame.mixer.get_init():
                pygame.mixer.init()
        except pygame.error:
            return NoOpSoundService()

        base_dir = root or sounds_dir()
        sounds: dict[SoundEvent, pygame.mixer.Sound] = {}
        for event, filename in SOUND_FILES.items():
            try:
                sounds[event] = pygame.mixer.Sound(str(base_dir / filename))
            except pygame.error:
                continue
        if not sounds:
            return NoOpSoundService()
        return cls(sounds)

    def play(self, event: SoundEvent) -> None:
        sound = self._sounds.get(event)
        if sound is None:
            return
        try:
            sound.play()
        except pygame.error:
            return


def sound_enabled() -> bool:
    return os.environ.get(SOUND_DISABLED_ENV, "").lower() not in {"0", "false", "off", "no"}
