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
                label = "Win while collaborating with CHARACTER as ROLE",
                data = {
                    "CHARACTER": (self.characters, 1),
                    "ROLE": (self.roles, 1),
                },
                is_time_consuming = False,
                is_difficult = False,
                weight = 24,
            ),
            GameObjectiveTemplate(
                label = "Win as ROLE with PLAYERCOUNT1 Crew and 1 Gnosia",
                data = {
                    "ROLE": (self.humanroles1, 1),
                    "PLAYERCOUNT1": (self.playercount1, 1),
                },
                is_time_consuming = False,
                is_difficult = False,
                weight = 5,
            ),
            GameObjectiveTemplate(
                label = "Win as ROLE with PLAYERCOUNT1 Crew and 1 Gnosia",
                data = {
                    "ROLE": (self.gnosiaroles, 1),
                    "PLAYERCOUNT1": (self.playercount1, 1),
                },
                is_time_consuming = False,
                is_difficult = True,
                weight = 2,
            ),
            GameObjectiveTemplate(
                label = "Win as Bug with PLAYERCOUNT1 Crew and 1 Gnosia",
                data = {
                    "PLAYERCOUNT1": (self.playercount1, 1),
                },
                is_time_consuming = False,
                is_difficult = False,
                weight = 1,
            ),
            GameObjectiveTemplate(
                label = "Win as ROLE with PLAYERCOUNT2 Crew and 2 Gnosia",
                data = {
                    "ROLE": (self.humanroles, 1),
                    "PLAYERCOUNT2": (self.playercount2, 1),
                },
                is_time_consuming = False,
                is_difficult = False,
                weight = 5,
            ),
            GameObjectiveTemplate(
                label = "Win as ROLE with PLAYERCOUNT2 Crew and 2 Gnosia",
                data = {
                    "ROLE": (self.gnosiaroles, 1),
                    "PLAYERCOUNT2": (self.playercount2, 1),
                },
                is_time_consuming = False,
                is_difficult = True,
                weight = 2,
            ),
            GameObjectiveTemplate(
                label = "Win as Bug with PLAYERCOUNT2 Crew and 2 Gnosia",
                data = {
                    "PLAYERCOUNT2": (self.playercount2, 1),
                },
                is_time_consuming = False,
                is_difficult = False,
                weight = 1,
            ),
            GameObjectiveTemplate(
                label = "Win as ROLE with PLAYERCOUNT3 Crew and 3 Gnosia",
                data = {
                    "ROLE": (self.roles, 1),
                    "PLAYERCOUNT3": (self.playercount3, 1),
                },
                is_time_consuming = False,
                is_difficult = False,
                weight = 8,
            ),
            GameObjectiveTemplate(
                label = "Win as ROLE with PLAYERCOUNT4 Crew and 4 Gnosia",
                data = {
                    "ROLE": (self.roles, 1),
                    "PLAYERCOUNT4": (self.playercount4, 1),
                },
                is_time_consuming = False,
                is_difficult = False,
                weight = 8,
            ),
            GameObjectiveTemplate(
                label = "Win as ROLE with PLAYERCOUNT5 Crew and 5 Gnosia",
                data = {
                    "ROLE": (self.humanroles, 1),
                    "PLAYERCOUNT5": (self.playercount5, 1),
                },
                is_time_consuming = False,
                is_difficult = True,
                weight = 5,
            ),
            GameObjectiveTemplate(
                label = "Win as ROLE with PLAYERCOUNT5 Crew and 5 Gnosia",
                data = {
                    "ROLE": (self.gnosiaroles, 1),
                    "PLAYERCOUNT5": (self.playercount5, 1),
                },
                is_time_consuming = False,
                is_difficult = False,
                weight = 2,
            ),
            GameObjectiveTemplate(
                label = "Win as Bug with PLAYERCOUNT5 Crew and 5 Gnosia",
                data = {
                    "PLAYERCOUNT5": (self.playercount5, 1),
                },
                is_time_consuming = False,
                is_difficult = False,
                weight = 1,
            ),
            GameObjectiveTemplate(
                label = "Win as ROLE with PLAYERCOUNT6 Crew and 6 Gnosia",
                data = {
                    "ROLE": (self.humanroles, 1),
                    "PLAYERCOUNT6": (self.playercount6, 1),
                },
                is_time_consuming = False,
                is_difficult = True,
                weight = 5,
            ),
            GameObjectiveTemplate(
                label = "Win as ROLE with PLAYERCOUNT6 Crew and 6 Gnosia",
                data = {
                    "ROLE": (self.gnosiaroles, 1),
                    "PLAYERCOUNT6": (self.playercount6, 1),
                },
                is_time_consuming = False,
                is_difficult = False,
                weight = 2,
            ),
            GameObjectiveTemplate(
                label = "Win as Bug with PLAYERCOUNT6 Crew and 6 Gnosia",
                data = {
                    "PLAYERCOUNT6": (self.playercount6, 1),
                },
                is_time_consuming = False,
                is_difficult = False,
                weight = 1,
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
    def humanroles1() -> List[str]:
        return [
            "Crew",
            "Engineer",
            "Doctor",
            "Guardian Angel",
        ]
    
    @staticmethod
    def humanroles() -> List[str]:
        return [
            "Crew",
            "Engineer",
            "Doctor",
            "Guardian Angel",
            "Guard Duty"
        ]
    
    @staticmethod
    def gnosiaroles() -> List[str]:
        return [
            "Gnosia",
            "AC Follower",
        ]
    
    @staticmethod
    def roles() -> List[str]:
        return [
            "Crew",
            "Engineer",
            "Doctor",
            "Guardian Angel",
            "Guard Duty"
            "Bug",
            "Gnosia",
            "AC Follower",
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


