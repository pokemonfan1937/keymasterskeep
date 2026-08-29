from __future__ import annotations

import functools
from typing import List, Dict, Set

from dataclasses import dataclass

from Options import Toggle, OptionSet

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms

@dataclass
class AegisRimArchipelagoOptions:
    pass

class AegisRimGame(Game):
    name = "13 Sentinels: Aegis Rim"
    platform = KeymastersKeepGamePlatforms.PS4

    platforms_other = [
        KeymastersKeepGamePlatforms.PS5,
        KeymastersKeepGamePlatforms.SW,
        KeymastersKeepGamePlatforms.SW2,
    ]

    is_adult_only_or_unrated = False

    options_cls = AegisRimArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return list()

    def game_objective_templates(self) -> List [GameObjectiveTemplate]:
        game_objective_templates = [
            GameObjectiveTemplate(
                label = "Complete AREA Battle NUMBER with an S rank",
                data = {
                    "AREA": (self.areas, 1),
                    "NUMBER": (self.number, 1),
                },
                is_time_consuming = False,
                is_difficult = False,
                weight = 24,
            ),
            GameObjectiveTemplate(
                    label = "Complete AREA Battle NUMBER fulfilling bonus objectives",
                    data = {
                        "AREA": (self.areas, 1),
                        "NUMBER": (self.number, 1),
                    },
                    is_time_consuming = False,
                    is_difficult = False,
                    weight = 24,
            ),
                GameObjectiveTemplate(
                    label = "Complete AREA Battle NUMBER with CHARACTERS",
                    data = {
                        "AREA": (self.areas, 1),
                        "NUMBER": (self.number, 1),
                        "CHARACTERS": (self.characters, 6),
                    },
                    is_time_consuming = False,
                    is_difficult = False,
                    weight = 24,
            ),
        ]
        return game_objective_templates
    
    @staticmethod
    def characters() -> List[str]:
        return [
            "Ogata",
            "Hijiyama",
            "Sekigahara",
            "Kurabe",
            "Fuyusaka",
            "Shinonome",
            "Minami",
            "Miura",
            "Kisaragi",
            "Yakushiji",
            "Takamiya",
            "Gouto",
            "Amiguchi",
    ]

    @staticmethod
    def areas() -> List[str]:
        return [
            "Ashitaba City",
            "Shibugaki City",
            "Himawari Ward",
    ]

    @staticmethod
    def number() -> List[int]:
        return list(range(1, 11, 1))

