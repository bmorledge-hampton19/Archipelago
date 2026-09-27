from .bases import BittyBuddiesTestBase
from ..options import CartridgeGoalScores, LogicDifficulty
from ..names import ItemName, LocationName, FRIENDSHIP_STASH_NAMES

class TestFriendshipStashDisabled(BittyBuddiesTestBase):
    """Make sure the friendship stash locations are excluded when the option is disabled."""

    # Normal difficulty with no friendship stash
    options = {
        "cartridge_goal_scores": CartridgeGoalScores.option_regular,
        "logic_difficulty": LogicDifficulty.option_normal,
        "final_goal_score": 999,
        "randomize_buddy_power": True,
        "power_of_friendship_stash": 0
    }

    def test_friendship_stash_disabled(self) -> None:
        for location in FRIENDSHIP_STASH_NAMES:
            self.assertRaises(KeyError, self.world.get_location, location)


class TestFriendshipStashPartiallyEnabled(BittyBuddiesTestBase):
    """Make sure the friendship stash locations are conditionally excluded/included."""

    # Normal difficulty with half the friendship stash enabled
    options = {
        "cartridge_goal_scores": CartridgeGoalScores.option_regular,
        "logic_difficulty": LogicDifficulty.option_normal,
        "final_goal_score": 999,
        "randomize_buddy_power": True,
        "power_of_friendship_stash": 15
    }

    def test_friendship_stash_partially_enabled(self) -> None:
        for i in range(1,21):
            location = FRIENDSHIP_STASH_NAMES[i-1]
            if i <= self.options["power_of_friendship_stash"]:
                try: self.world.get_location(location)
                except KeyError: self.fail()
            else:
                self.assertRaises(KeyError, self.world.get_location, location)


class TestFriendshipStashEnabled(BittyBuddiesTestBase):
    """Make sure the friendship stash locations are present and reachable when enabled."""

    # Normal difficulty with full friendship stash
    options = {
        "cartridge_goal_scores": CartridgeGoalScores.option_regular,
        "logic_difficulty": LogicDifficulty.option_normal,
        "final_goal_score": 999,
        "randomize_buddy_power": True,
        "power_of_friendship_stash": 20
    }

    def test_friendship_stash_enabled(self) -> None:
        for location in FRIENDSHIP_STASH_NAMES:
            try: self.world.get_location(location)
            except KeyError: self.fail()

    def test_friendship_stash_accessibility(self) -> None:

        with self.subTest("Test friendship stash accessibility for initial items, which cannot goal."):
            for location in FRIENDSHIP_STASH_NAMES:
                self.assertFalse(self.can_reach_location(location))

        with self.subTest("Give all buddy levels up and buddy power. The locations should now be accessible."):
            for _ in range(5):
                self.multiworld.state.collect(self.world.create_item(ItemName.BUD_LEVEL_UP), True)
                self.multiworld.state.collect(self.world.create_item(ItemName.BIFF_LEVEL_UP), True)
                self.multiworld.state.collect(self.world.create_item(ItemName.BENSON_LEVEL_UP), True)
                self.multiworld.state.collect(self.world.create_item(ItemName.BRIE_LEVEL_UP), True)
                self.multiworld.state.collect(self.world.create_item(ItemName.BAZZ_LEVEL_UP), True)
                self.multiworld.state.collect(self.world.create_item(ItemName.BUDDY_POWER), True)
            for location in FRIENDSHIP_STASH_NAMES:
                self.assertTrue(self.can_reach_location(location))
