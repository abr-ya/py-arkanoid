from __future__ import annotations

from enum import Enum


class SoundEvent(Enum):
    LAUNCH = "launch"
    COLLISION = "collision"
    BRICK_BREAK = "brick_break"
    POWER_UP_PICKUP = "power_up_pickup"
    LEVEL_COMPLETE = "level_complete"
