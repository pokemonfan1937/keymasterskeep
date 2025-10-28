from __future__ import annotations

import functools
from typing import List, Dict, Set

from dataclasses import dataclass

from Options import Toggle, OptionSet

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms

@dataclass
class PP20ArchipelagoOptions:
    puyopuyo20th_include_challenge_battles: IncludeChallengeBattles

class PuyoPuyo20thAnniversaryGame(Game):
    name = "Puyo Puyo 20th Anniversary"
    platform = KeymastersKeepGamePlatforms.NDS

    platforms_other = [
        KeymastersKeepGamePlatforms._3DS,
        KeymastersKeepGamePlatforms.WII,
        KeymastersKeepGamePlatforms.PSP,
    ]

    is_adult_only_or_unrated = False

    options_cls = PP20ArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return list()

    def game_objective_templates(self) -> List [GameObjectiveTemplate]:
        game_objective_templates = [
            GameObjectiveTemplate(
                label = "Complete STORY on at least Hard difficulty with at least RANK rank choosing RULESET",
                data = {
                    "STORY": (self.stories, 1),
                    "RANK": (self.easyranks, 1),
                    "RULESET": (self.easyrulesets, 1)
                },
                is_time_consuming = False,
                is_difficult = True,
                weight = 24,
            ),
            GameObjectiveTemplate(
                label = "Complete STORY on at least DIFFICULTY difficulty with at least RANK rank choosing random ruleset",
                data = {
                    "STORY": (self.stories, 1),
                    "DIFFICULTY": (self.easydifficulties, 1),
                    "RANK": (self.easyranks, 1)
                },
                is_time_consuming = False,
                is_difficult = True,
                weight = 24,
            ),
            GameObjectiveTemplate(
                label = "Complete STORY on at least DIFFICULTY difficulty with at least S rank choosing RULESET ruleset",
                data = {
                    "STORY": (self.stories, 1),
                    "DIFFICULTY": (self.easydifficulties, 1),
                    "RULESET": (self.easyrulesets, 1)
                },
                is_time_consuming = False,
                is_difficult = True,
                weight = 24,
            ),
            GameObjectiveTemplate(
                label = "Complete STORY on at least DIFFICULTY difficulty with at least RANK rank choosing RULESET",
                data = {
                    "STORY": (self.stories, 1),
                    "DIFFICULTY": (self.easydifficulties, 1),
                    "RANK": (self.easyranks, 1),
                    "RULESET": (self.easyrulesets, 1)
                },
                is_time_consuming = False,
                is_difficult = False,
                weight = 244,
            ),
        ]
        if self.include_challenge_battles:
            game_objective_templates.append(
                GameObjectiveTemplate(
                    label = "Complete the CHALLENGEBATTLE",
                    data = {
                        "CHALLENGEBATTLE": (self.challenge_battles, 1)
                    },
                    is_time_consuming = False,
                    is_difficult = True,
                    weight = 24,
                )
            )
        
            
        return game_objective_templates
    
    @property
    def include_challenge_battles(self) -> bool: 
        return bool(self.archipelago_options.puyopuyo20th_include_challenge_battles.value)
    
    @staticmethod
    def challenge_battles() -> List[str]:
        return [
            "Puyo Puyo Challenge",
            "Puyo Puyo 2 Challenge",
            "Puyo SUN Challenge",
            "Puyo Fever Challenge",
            "Mission Puyo Challenge",
        ]
    
    @staticmethod
    def stories() -> List[str]:
        return [
            "Arle's Story",
            "Amitie's Story",
            "Draco's Story",
            "Lidelle's Story",
            "Ringo's Story",
            "Maguro's Story",
            "Schezo's Story",
            "Risukuma's Story",
            "Ecolo's Story",  
            "Klug's Story", 
            "Sig's Story", 
            "Yu & Rei's Story", 
            "Suketoudara's Story", 
            "Dongurigaeru's Story", 
            "Satan(Dark Prince)'s Story", 
            "Carbuncle's Story", 
            "Ms. Accord's Story", 
            "Ocean Prince's Story", 
            "Onion Pixie's Story", 
            "Witch's Story", 
            "Rulue's Story",
            "Lemres's Story",
            "Feli's Story",
            "The Final Story",
        ]
    
    @staticmethod
    def easydifficulties() -> List[str]:
        return [
            "Very Easy",
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
    
    @staticmethod
    def easyrulesets() -> List[str]:
        return [
            "Puyo Puyo ruleset",
            "Puyo Puyo 2 ruleset",
            "any ruleset",
        ]
    
class IncludeChallengeBattles(Toggle):
    """
    Determines whether Challenge Battles (accessed through School > Challenge > Challenge Battles) are included
    """
    display_name = "Include Challenge Battles"
