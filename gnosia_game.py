from __future__ import annotations

import functools
from typing import List, Dict, Set

from dataclasses import dataclass

from Options import Toggle, OptionSet

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms

@dataclass
class GnosiaArchipelagoOptions:
    pass

class GnosiaGame(Game):
    name = "Gnosia"
    platform = KeymastersKeepGamePlatforms.PC

    platforms_other = [
        KeymastersKeepGamePlatforms.VITA,
        KeymastersKeepGamePlatforms.SW,
        KeymastersKeepGamePlatforms.PS4,
        KeymastersKeepGamePlatforms.PS5,
        KeymastersKeepGamePlatforms.XONE,
        KeymastersKeepGamePlatforms.XSX,
    ]

    is_adult_only_or_unrated = False

    options_cls = GnosiaArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return list()

    def game_objective_templates(self) -> List [GameObjectiveTemplate]:
        game_objective_templates = [
            GameObjectiveTemplate(
                label = "Win while collaborating with CHARACTER with PLAYERCOUNT1 Crew and 1 Gnosia",
                data = {
                    "CHARACTER": (self.characters, 1),
                    "PLAYERCOUNT1": (self.playercount1, 1),
                },
                is_time_consuming = False,
                is_difficult = False,
                weight = 4,
            ),
            GameObjectiveTemplate(
                label = "Win while collaborating with CHARACTER with PLAYERCOUNT2 Crew and 2 Gnosia",
                data = {
                    "CHARACTER": (self.characters, 1),
                    "PLAYERCOUNT2": (self.playercount2, 1),
                },
                is_time_consuming = False,
                is_difficult = False,
                weight = 4,
            ),
            GameObjectiveTemplate(
                label = "Win while collaborating with CHARACTER with PLAYERCOUNT3 Crew and 3 Gnosia",
                data = {
                    "CHARACTER": (self.characters, 1),
                    "PLAYERCOUNT3": (self.playercount3, 1),
                },
                is_time_consuming = False,
                is_difficult = False,
                weight = 4,
            ),
            GameObjectiveTemplate(
                label = "Win while collaborating with CHARACTER with PLAYERCOUNT4 Crew and 4 Gnosia",
                data = {
                    "CHARACTER": (self.characters, 1),
                    "PLAYERCOUNT1": (self.playercount4, 1),
                },
                is_time_consuming = False,
                is_difficult = False,
                weight = 4,
            ),
            GameObjectiveTemplate(
                label = "Win while collaborating with CHARACTER with PLAYERCOUNT5 Crew and 5 Gnosia",
                data = {
                    "CHARACTER": (self.characters, 1),
                    "PLAYERCOUNT5": (self.playercount1, 1),
                },
                is_time_consuming = False,
                is_difficult = False,
                weight = 4,
            ),
            GameObjectiveTemplate(
                label = "Win while collaborating with CHARACTER with PLAYERCOUNT6 Crew and 6 Gnosia",
                data = {
                    "CHARACTER": (self.characters, 1),
                    "PLAYERCOUNT6": (self.playercount6, 1),
                },
                is_time_consuming = False,
                is_difficult = False,
                weight = 4,
            ),
            GameObjectiveTemplate(
                label = "Win as ROLE with PLAYERCOUNT1 Crew and 1 Gnosia",
                data = {
                    "ROLE": (self.roles, 1),
                    "PLAYERCOUNT1": (self.playercount1, 1),
                },
                is_time_consuming = False,
                is_difficult = False,
                weight = 4,
            ),
            GameObjectiveTemplate(
                label = "Win as ROLE with PLAYERCOUNT2 Crew and 2 Gnosia",
                data = {
                    "ROLE": (self.roles, 1),
                    "PLAYERCOUNT2": (self.playercount2, 1),
                },
                is_time_consuming = False,
                is_difficult = False,
                weight = 4,
            ),
            GameObjectiveTemplate(
                label = "Win as ROLE with PLAYERCOUNT3 Crew and 3 Gnosia",
                data = {
                    "ROLE": (self.roles, 1),
                    "PLAYERCOUNT3": (self.playercount3, 1),
                },
                is_time_consuming = False,
                is_difficult = False,
                weight = 4,
            ),
            GameObjectiveTemplate(
                label = "Win as ROLE with PLAYERCOUNT4 Crew and 4 Gnosia",
                data = {
                    "ROLE": (self.roles, 1),
                    "PLAYERCOUNT1": (self.playercount4, 1),
                },
                is_time_consuming = False,
                is_difficult = False,
                weight = 4,
            ),
            GameObjectiveTemplate(
                label = "Win as ROLE with PLAYERCOUNT5 Crew and 5 Gnosia",
                data = {
                    "ROLE": (self.roles, 1),
                    "PLAYERCOUNT5": (self.playercount1, 1),
                },
                is_time_consuming = False,
                is_difficult = False,
                weight = 4,
            ),
            GameObjectiveTemplate(
                label = "Win as ROLE with PLAYERCOUNT6 Crew and 6 Gnosia",
                data = {
                    "ROLE": (self.roles, 1),
                    "PLAYERCOUNT6": (self.playercount6, 1),
                },
                is_time_consuming = False,
                is_difficult = False,
                weight = 4,
            ),
            GameObjectiveTemplate(
                label = "Win with Random Settings",
                data = {
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
            "Setsu",
            "Gina",
            "SQ",
            "Raqio",
            "Stella",
            "Shigemichi",
            "Chipie",
            "Comet",
            "Jonas",  
            "Kukrushka", 
            "Otome", 
            "Sha-Ming", 
            "Remnan", 
            "Yuriko", 
        ]
    
    @staticmethod
    def roles() -> List[str]:
        return [
            "Crew",
            "Gnosia",
            "Engineer",
            "Doctor",
            "Guardian Angel",
            "Guard Duty",
            "AC Follower",
            "Bug",
        ]
    
    @staticmethod
    def playercount1() -> List[int]:
        return list(range(5, 16))
    
    @staticmethod
    def playercount2() -> List[int]:
        return list(range(7, 16))
    
    @staticmethod
    def playercount3() -> List[int]:
        return list(range(9, 16))
    
    @staticmethod
    def playercount4() -> List[int]:
        return list(range(11, 16))
    
    @staticmethod
    def playercount5() -> List[int]:
        return list(range(13, 16))
    
    @staticmethod
    def playercount6() -> List[int]:
        return list(range(15, 16))
