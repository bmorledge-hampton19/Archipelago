### A collection of enums for standardizing names across the Bitty Buddies Archipelago.
from enum import IntEnum, StrEnum


class Buddy(IntEnum):
    BUD = 0
    BIFF = 1
    BENSON = 2
    BRIE = 3
    BAZZ = 4


class RegionName(StrEnum):
    MENU = "Menu"


class LocationName(StrEnum):
    TRASH_DASH_1 = "Trash Dash Goal Score 1"
    TRASH_DASH_2 = "Trash Dash Goal Score 2"
    TRASH_DASH_3 = "Trash Dash Goal Score 3"
    TRASH_DASH_4 = "Trash Dash Goal Score 4"
    TRASH_DASH_5 = "Trash Dash Goal Score 5"

    HAVE_AT_THEE_1 = "Have At Thee Goal Score 1"
    HAVE_AT_THEE_2 = "Have At Thee Goal Score 2"
    HAVE_AT_THEE_3 = "Have At Thee Goal Score 3"
    HAVE_AT_THEE_4 = "Have At Thee Goal Score 4"
    HAVE_AT_THEE_5 = "Have At Thee Goal Score 5"

    TREATMENT_TO_GO_1 = "Treatment To-Go Goal Score 1"
    TREATMENT_TO_GO_2 = "Treatment To-Go Goal Score 2"
    TREATMENT_TO_GO_3 = "Treatment To-Go Goal Score 3"
    TREATMENT_TO_GO_4 = "Treatment To-Go Goal Score 4"
    TREATMENT_TO_GO_5 = "Treatment To-Go Goal Score 5"

    ACROBIRD_1 = "Acrobird Goal Score 1"
    ACROBIRD_2 = "Acrobird Goal Score 2"
    ACROBIRD_3 = "Acrobird Goal Score 3"
    ACROBIRD_4 = "Acrobird Goal Score 4"
    ACROBIRD_5 = "Acrobird Goal Score 5"

    BAZZS_BIG_DAY_1 = "Bazz's Big Day Goal Score 1"
    BAZZS_BIG_DAY_2 = "Bazz's Big Day Goal Score 2"
    BAZZS_BIG_DAY_3 = "Bazz's Big Day Goal Score 3"
    BAZZS_BIG_DAY_4 = "Bazz's Big Day Goal Score 4"
    BAZZS_BIG_DAY_5 = "Bazz's Big Day Goal Score 5"

    ALL_BUDDIES_LEVEL_1 = "1st Goal Score Achieved in All Cartridges"
    ALL_BUDDIES_LEVEL_2 = "2nd Goal Score Achieved in All Cartridges"
    ALL_BUDDIES_LEVEL_3 = "3rd Goal Score Achieved in All Cartridges"
    ALL_BUDDIES_LEVEL_4 = "4th Goal Score Achieved in All Cartridges"

    MEAN_MUGGING = "Bud Silly Check (Mean Mugging)"
    HEAVYWEIGHT_CHAMPION = "Biff Silly Check (Heavyweight Champion)"
    FRICTIONLESS_FRUIT = "Benson Silly Check (Frictionless Fruit)"
    NEGATIVE_JING = "Brie Silly Check (Negative Jing)"
    ZERO_STAR_REVIEW = "Bazz Silly Check (0-star Review)"

    FAST_PHARMA = "Bud Skill Check (Fast Pharma)"
    PARRY_KING = "Biff Skill Check (Parry King)"
    MIRACLE_CURE = "Benson Skill Check (Miracle Cure)"
    HIGH_FLYER = "Brie Skill Check (High Flyer)"
    SHARPSHOOTER = "Bazz Skill Check (Sharpshooter)"

    FRIENDSHIP_STASH_1 = "Power of Friendship Stash 1"
    FRIENDSHIP_STASH_2 = "Power of Friendship Stash 2"
    FRIENDSHIP_STASH_3 = "Power of Friendship Stash 3"
    FRIENDSHIP_STASH_4 = "Power of Friendship Stash 4"
    FRIENDSHIP_STASH_5 = "Power of Friendship Stash 5"
    FRIENDSHIP_STASH_6 = "Power of Friendship Stash 6"
    FRIENDSHIP_STASH_7 = "Power of Friendship Stash 7"
    FRIENDSHIP_STASH_8 = "Power of Friendship Stash 8"
    FRIENDSHIP_STASH_9 = "Power of Friendship Stash 9"
    FRIENDSHIP_STASH_10 = "Power of Friendship Stash 10"
    FRIENDSHIP_STASH_11 = "Power of Friendship Stash 11"
    FRIENDSHIP_STASH_12 = "Power of Friendship Stash 12"
    FRIENDSHIP_STASH_13 = "Power of Friendship Stash 13"
    FRIENDSHIP_STASH_14 = "Power of Friendship Stash 14"
    FRIENDSHIP_STASH_15 = "Power of Friendship Stash 15"
    FRIENDSHIP_STASH_16 = "Power of Friendship Stash 16"
    FRIENDSHIP_STASH_17 = "Power of Friendship Stash 17"
    FRIENDSHIP_STASH_18 = "Power of Friendship Stash 18"
    FRIENDSHIP_STASH_19 = "Power of Friendship Stash 19"
    FRIENDSHIP_STASH_20 = "Power of Friendship Stash 20"

    def is_friendship_stash_name(self) -> bool:
        """
        Prefer this function over directly checking for inclusion in the FRIENDSHIP_STASH_NAMES list,
        as it should be much faster than iterating over every friendship stash name.
        """
        return self.startswith("Power of Friendship Stash")


CARTRIDGE_GOAL_SCORE_NAMES: dict[Buddy, list[LocationName]] = {
    Buddy.BUD: [
        LocationName.TRASH_DASH_1, LocationName.TRASH_DASH_2, LocationName.TRASH_DASH_3,
        LocationName.TRASH_DASH_4, LocationName.TRASH_DASH_5
    ],
    Buddy.BIFF: [
        LocationName.HAVE_AT_THEE_1, LocationName.HAVE_AT_THEE_2, LocationName.HAVE_AT_THEE_3,
        LocationName.HAVE_AT_THEE_4, LocationName.HAVE_AT_THEE_5
    ],
    Buddy.BENSON: [
        LocationName.TREATMENT_TO_GO_1, LocationName.TREATMENT_TO_GO_2, LocationName.TREATMENT_TO_GO_3,
        LocationName.TREATMENT_TO_GO_4, LocationName.TREATMENT_TO_GO_5
    ],
    Buddy.BRIE: [
        LocationName.ACROBIRD_1, LocationName.ACROBIRD_2, LocationName.ACROBIRD_3,
        LocationName.ACROBIRD_4, LocationName.ACROBIRD_5
    ],
    Buddy.BAZZ: [
        LocationName.BAZZS_BIG_DAY_1, LocationName.BAZZS_BIG_DAY_2, LocationName.BAZZS_BIG_DAY_3,
        LocationName.BAZZS_BIG_DAY_4, LocationName.BAZZS_BIG_DAY_5
    ],
}

BUDDY_POWER_LOCATION_NAMES: list[LocationName] = [
    LocationName.ALL_BUDDIES_LEVEL_1, LocationName.ALL_BUDDIES_LEVEL_2,
    LocationName.ALL_BUDDIES_LEVEL_3, LocationName.ALL_BUDDIES_LEVEL_4
]

SILLY_CHECK_NAMES: list[LocationName] = [
    LocationName.MEAN_MUGGING, LocationName.HEAVYWEIGHT_CHAMPION, LocationName.FRICTIONLESS_FRUIT,
    LocationName.NEGATIVE_JING, LocationName.ZERO_STAR_REVIEW,
]

SKILL_CHECK_NAMES: list[LocationName] = [
    LocationName.FAST_PHARMA, LocationName.PARRY_KING, LocationName.MIRACLE_CURE,
    LocationName.HIGH_FLYER, LocationName.SHARPSHOOTER,
]

FRIENDSHIP_STASH_NAMES: list[LocationName] = [
    LocationName.FRIENDSHIP_STASH_1, LocationName.FRIENDSHIP_STASH_2, LocationName.FRIENDSHIP_STASH_3,
    LocationName.FRIENDSHIP_STASH_4, LocationName.FRIENDSHIP_STASH_5, LocationName.FRIENDSHIP_STASH_6,
    LocationName.FRIENDSHIP_STASH_7, LocationName.FRIENDSHIP_STASH_8, LocationName.FRIENDSHIP_STASH_9,
    LocationName.FRIENDSHIP_STASH_10, LocationName.FRIENDSHIP_STASH_11, LocationName.FRIENDSHIP_STASH_12,
    LocationName.FRIENDSHIP_STASH_13, LocationName.FRIENDSHIP_STASH_14, LocationName.FRIENDSHIP_STASH_15,
    LocationName.FRIENDSHIP_STASH_16, LocationName.FRIENDSHIP_STASH_17, LocationName.FRIENDSHIP_STASH_18,
    LocationName.FRIENDSHIP_STASH_19, LocationName.FRIENDSHIP_STASH_20,
]


class ItemName(StrEnum):
    BUD_LEVEL_UP = "Bud Level Up"
    BIFF_LEVEL_UP = "Biff Level Up"
    BENSON_LEVEL_UP = "Benson Level Up"
    BRIE_LEVEL_UP = "Brie Level Up"
    BAZZ_LEVEL_UP = "Bazz Level Up"

    BUDDY_POWER = "Buddy Power Up"

    TRASH_DASH_SCORE = "Trash Dash Bonus Points"
    HAVE_AT_THEE_SCORE = "Have At Thee Bonus Points"
    TREATMENT_TO_GO_SCORE = "Treatment To-Go Bonus Points"
    ACROBIRD_SCORE = "Acrobird Bonus Points"
    BAZZS_BIG_DAY_SCORE = "Bazz's Big Day Bonus Points"

LEVEL_UP_NAMES: list[ItemName] = [
    ItemName.BUD_LEVEL_UP, ItemName.BIFF_LEVEL_UP, ItemName.BENSON_LEVEL_UP,
    ItemName.BRIE_LEVEL_UP, ItemName.BAZZ_LEVEL_UP
]
BONUS_SCORE_NAMES: list[ItemName] = [
    ItemName.TRASH_DASH_SCORE, ItemName.HAVE_AT_THEE_SCORE, ItemName.TREATMENT_TO_GO_SCORE,
    ItemName.ACROBIRD_SCORE, ItemName.BAZZS_BIG_DAY_SCORE
]

FORBIDDEN_FRIENDSHIP_STASH_ITEM_NAMES: set[ItemName] = {
    ItemName.BUD_LEVEL_UP, ItemName.BIFF_LEVEL_UP, ItemName.BENSON_LEVEL_UP,
    ItemName.BRIE_LEVEL_UP, ItemName.BAZZ_LEVEL_UP, ItemName.BUDDY_POWER
}

class EventName(StrEnum):
    VICTORY = "Victory"
