from __future__ import annotations

import functools
from typing import List, Dict, Set

from dataclasses import dataclass

from Options import Toggle, OptionSet

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms

@dataclass
class PP15ArchipelagoOptions:
    pass
    
class PuyoPuyo15thAnniversaryGame(Game):
    name = "Puyo Puyo 15th Anniversary"
    platform = KeymastersKeepGamePlatforms.NDS

    platforms_other = [
        KeymastersKeepGamePlatforms.PS2,
        KeymastersKeepGamePlatforms.WII,
        KeymastersKeepGamePlatforms.PSP,
    ]

    is_adult_only_or_unrated = False

    options_cls = PP15ArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return list()

    def game_objective_templates(self) -> List [GameObjectiveTemplate]:
        game_objective_templates = [
            GameObjectiveTemplate(
                label = "Complete STORY on at least Hard difficulty with at least RANK rank",
                data = {
                    "STORY": (self.stories, 1),
                    "RANK": (self.easyranks, 1),
                },
                is_time_consuming = False,
                is_difficult = True,
                weight = 24,
            ),
            GameObjectiveTemplate(
                label = "Complete STORY on at least DIFFICULTY difficulty with at least S rank",
                data = {
                    "STORY": (self.stories, 1),
                    "DIFFICULTY": (self.easydifficulties, 1),
                },
                is_time_consuming = False,
                is_difficult = True,
                weight = 24,
            ),
            GameObjectiveTemplate(
                label = "Complete STORY on at least DIFFICULTY difficulty with at least RANK rank",
                data = {
                    "STORY": (self.stories, 1),
                    "DIFFICULTY": (self.easydifficulties, 1),
                    "RANK": (self.easyranks, 1),
                },
                is_time_consuming = False,
                is_difficult = False,
                weight = 244,
            ),
        ]
        return game_objective_templates
    
    @staticmethod
    def stories() -> List[str]:
        return [
            "Amitie's Story",
            "Ocean Prince's Story",
            "Feli's Story",
            "Klug's Story",
            "Dongurigaeru's Story",
            "Arle's Story",
            "Yu & Rei's Story",
            "Sig's Story",
            "Akuma's Story",  
            "Nasu Grave's Story", 
            "Baldanders's Story", 
            "Raffina(Raffine)'s Story", 
            "Onion Pixie(Onion Pixy)'s Story", 
            "Ms. Accord's Story", 
            "Lidelle(Rider)'s Story", 
            "Suketoudara's Story", 
            "Schezo's Story", 
            "Zoh Daimaoh's Story", 
            "Oshare Bones's Story", 
            "Lemres's Story", 
            "Rulue's Story",
            "Satan(Dark Prince)'s Story",
        ]
    
    @staticmethod
    def easydifficulties() -> List[str]:
        return [
            "Easy",
            "Normal",
        ]
    
    @staticmethod
    def easyranks() -> List[str]:
        return [
            "C",
            "B",
            "A",
        ]

