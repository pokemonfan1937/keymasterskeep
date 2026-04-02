from __future__ import annotations

import functools
from typing import List, Dict, Set

from dataclasses import dataclass

from Options import Toggle, OptionSet

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms

@dataclass
class TokyoXanaduArchipelagoOptions:
    tx_include_srank: IncludeDungeonSRank
    tx_include_side: IncludeSideStory
    tx_include_after: IncludeAfterStory
    tx_include_ngplus: IncludeNGPlus
    tx_include_goa: IncludeGateofAvalon
    tx_include_mishy: IncludeMishy
    tx_include_fishing: IncludeExplosiveFishing
    tx_include_skate: IncludeSkateboarding

class TokyoXanaduGame(Game):
    name = "Tokyo Xanadu"
    platform = KeymastersKeepGamePlatforms.VITA

    platforms_other = [
        KeymastersKeepGamePlatforms.PS4,
        KeymastersKeepGamePlatforms.PS5,
        KeymastersKeepGamePlatforms.PC,
        KeymastersKeepGamePlatforms.SW,
        KeymastersKeepGamePlatforms.SW2,
    ]

    is_adult_only_or_unrated = False

    options_cls = TokyoXanaduArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return list()

    def game_objective_templates(self) -> List [GameObjectiveTemplate]:
        game_objective_templates = []

        if self.include_srank:
            game_objective_templates.append(
                GameObjectiveTemplate(
                    label = "Complete DUNGEON with an S rank using CHARACTERS",
                    data = {
                        "CHARACTER": (self.characters, 3),
                        "DUNGEON": (self.dungeons, 1),
                    },
                    is_time_consuming = False,
                    is_difficult = False,
                    weight = 24,
                )
            )
        if self.include_goa:
            game_objective_templates.append(
                GameObjectiveTemplate(
                    label = "Win against OPPONENT in Gate of Avalon",
                    data = {
                        "OPPONENT": (self.avalonopponents, 1),
                    },
                    is_time_consuming = False,
                    is_difficult = False,
                    weight = 24,
                )
            ),
        if self.include_mishy:
            game_objective_templates.append(
                GameObjectiveTemplate(
                    label = "Win Mishy Panic on DIFFICULTY difficulty and with RANK rank",
                    data = {
                        "DIFFICULTY": (self.mishydifficulty, 1),
                        "RANK": (self.mishyranks, 1),
                    },
                    is_time_consuming = False,
                    is_difficult = False,
                    weight = 24,
                ),
            )
        if self.include_fishing:
            game_objective_templates.append(
                GameObjectiveTemplate(
                    label = "Catch FISH in Explosive Fishing",
                    data = {
                        "FISH": (self.explosivefishingfish, 1),
                    },
                    is_time_consuming = False,
                    is_difficult = False,
                    weight = 24,
                ),
            )
        if self.include_skate:
            game_objective_templates.append(
                GameObjectiveTemplate(
                    label = "Complete SKATECOURSE",
                    data = {
                        "SKATECOURSE": (self.skatecourses, 1),
                    },
                    is_time_consuming = False,
                    is_difficult = False,
                    weight = 24,
                ),
            )
        return game_objective_templates
    
    @functools.cached_property
    def dungeons_base(self) -> List[str]:
        return [
            "Ruins of Abstraction",
            "Amber Labyrinth",
            "Moonlit Garden",
            "Viridian Labyrinth",
            "Corridor of Souls",
            "Second Spirit Barrier",
            "Ruins of Recollection",
            "Cave of the Fallen Dragon",
            "Azure Ruins",
            "Garden of Reflection",
            "Temple of Evil Mist",
            "Scarlet Labyrinth",
            "Birdcage Corridor",
            "Witch's Briar Castle",
            "Sacred Land of Eternity",
            "Ruin of Fading Melodies",
            "Corridor of the Sky",
            "Temple of Twilight",
            "Fourth Spirit Barrier",
            "Palace of the Winged God",
            "Cave of Divine Flame",
            "Golden Dusk Ruins",
            "Garden of Drozen Trees",
            "Purgatory of Molten Blood",
            "Fortress of False Gods - First",
            "Fortress of False Gods - Last",
            "Pillar of [Darkness]",
            "Pillar of [Eternity]",
            "Pillar of [Refinement]",
            "Box - Road of Interstice",
            "Box - Road of Division",
            "Box - Road of Rebirth",
            "Box - Road of Infinity",
            "Box - Final Corridor",
            "The Castle of the Holy Chalice",
            "Palace of Light",
            "Cave of the Ancient Gods",
        ]

    @functools.cached_property
    def dungeons_side(self) -> List[str]:
        return [
            "Abandoned Path",
            "Amber Road",
            "Scarlet Battlefield",
            "Garden of Stagnant Water",
            "Diseased Ruins",
            "Ruined Castle of Darkness",
            "Palace of the Luminous Sky",
    ]

    @functools.cached_property
    def dungeons_after(self) -> List[str]:
        return [
            "Boundary of Exhaustion",
            "Boundary of Tears",
            "Boundary of Death"
    ]

    @functools.cached_property
    def dungeons_ngplus(self) -> List[str]:
        return [
            "Seventh Spirit Barrier",
            "Sacred Land of Time",
            "Fortress of Light",
            "Prison of the Murky Depths",
            "The Temple of the Boundary",
            "The Pillar of [Oblivion]",
    ]

    @functools.cached_property
    def characters_base(self) -> List[str]:
        return [
            "Kou",
            "Asuka",
            "Sora",
            "Yuuki",
            "Shio",
            "Mitsuki",
            "Rion",
            "Gorou",
    ]

    @functools.cached_property
    def characters_after(self) -> List[str]:
        return [
            "Ryouta",
            "Jun",
    ]

    @staticmethod
    def explosivefishingfish() -> List[str]:
        return [
            "Salmon",
            "Eel",
            "Noble Carp",
            "Gladiator",
            "Queen Crab",
            "Invisible Crayfish",
            "Giant Swordtail",
            "Pale Salamander",
            "Catfish",
            "Gold Salmon",
            "Arch Tyrant",
    ]

    @staticmethod
    def avalonopponents() -> List[str]:
        return [
            "Azusa",
            "Mayu",
            "Jun",
            "Erika",
            "Saburo",
            "Akane",
            "Akihiro",
            "Sadie",
            "Reika",
            "Seijyuurou",
            "Towa",
    ]
    
    @staticmethod
    def mishydifficulty() -> List[str]:
        return [
            "Easy",
            "Normal",
            "Hard",
    ]

    @staticmethod
    def mishyranks() -> List[str]:
        return [
            "S",
            "Perfect",
    ]

    @staticmethod
    def skatecourses() -> List[str]:
        return [
            "Course A: Beginner",
            "Course A: Intermediate",
            "Course A: Advanced",
            "Course B: Beginner",
            "Course B: Intermediate",
            "Course B: Advanced",
    ]

    @property
    def include_srank(self) -> bool: 
        return bool(self.archipelago_options.tx_include_srank.value)
    
    @property
    def include_side(self) -> bool: 
        return bool(self.archipelago_options.tx_include_side.value)
    
    @property
    def include_after(self) -> bool: 
        return bool(self.archipelago_options.tx_include_after.value)
    
    @property
    def include_ngplus(self) -> bool: 
        return bool(self.archipelago_options.tx_include_ngplus.value)
    
    @property
    def include_goa(self) -> bool: 
        return bool(self.archipelago_options.tx_include_goa.value)
    
    @property
    def include_mishy(self) -> bool: 
        return bool(self.archipelago_options.tx_include_mishy.value)
    
    @property
    def include_fishing(self) -> bool: 
        return bool(self.archipelago_options.tx_include_fishing.value)
    
    @property
    def include_skate(self) -> bool: 
        return bool(self.archipelago_options.tx_include_skate.value)
    
    def dungeons(self) -> List[str]:
        levels: List[str] = self.dungeons_base[:]
        if self.include_side:
            levels.extend(self.dungeons_side[:])
        if self.include_after:
            levels.extend(self.dungeons_after[:])
        if self.include_ngplus:
            levels.extend(self.dungeons_ngplus[:])
        return sorted(levels)

    def characters(self) -> List[str]:
        levels: List[str] = self.characters_base[:]
        if self.include_after:
            levels.extend(self.characters_after[:])

        return sorted(levels)
    
class IncludeDungeonSRank(Toggle):
    """
    Determines whether dungeon S Rank objectives are included
    """
    display_name = "Include Dungeon S Rank Objectives"
    default = True

class IncludeSideStory(Toggle):
    """
    Determines whether eX+ exclusive Side Story dungeons are included
    """
    display_name = "Include Side Story"

class IncludeAfterStory(Toggle):
    """
    Determines whether eX+ exclusive After Story characters and dungeons are included
    """
    display_name = "Include After Story"

class IncludeNGPlus(Toggle):
    """
    Determines whether eX+ exclusive NG+ dungeons are included
    """
    display_name = "Include NG+"

class IncludeGateofAvalon(Toggle):
    """
    Determines whether Gate of Avalon objectives are included
    """
    display_name = "Include Gate of Avalon Objectives"

class IncludeMishy(Toggle):
    """
    Determines whether Mishy Panic objectives are included
    """
    display_name = "Include Mishy Panic Objectives"

class IncludeExplosiveFishing(Toggle):
    """
    Determines whether Explosive Fishing objectives are included
    """
    display_name = "Include Explosive Fishing Objectives"

class IncludeSkateboarding(Toggle):
    """
    Determines whether Skateboarding objectives are included
    """
    display_name = "Include Skateboarding Objectives"

