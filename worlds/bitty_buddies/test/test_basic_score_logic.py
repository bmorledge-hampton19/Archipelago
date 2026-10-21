from .bases import BittyBuddiesTestBase
from ..options import CartridgeGoalScores, LogicDifficulty
from ..names import ItemName, LocationName, LEVEL_UP_NAMES, EventName

class TestBasicScoreLogic(BittyBuddiesTestBase):
    """Tests the basic logic for the goal score checks (which are most of the checks in the game.)"""

    # Normal difficulty
    options = {
        "cartridge_goal_scores": CartridgeGoalScores.option_regular,
        "logic_difficulty": LogicDifficulty.option_normal,
        "final_goal_score": 999,
        "randomize_buddy_power": True
    }


    def test_initial_items(self) -> None:

        with self.subTest("Test checks that the initial buddy has been collected."):
            self.assertTrue(any(
                self.multiworld.state.has(level_up_name, self.player) for level_up_name in LEVEL_UP_NAMES
            ))

        with self.subTest("Test checks that the initial buddy power has been collected."):
            self.assertTrue(self.multiworld.state.has(ItemName.BUDDY_POWER, self.player))


    def test_adding_buddies(self) -> None:

        with self.subTest("Test the starting checks for Bud"):
            # Remove the random starting buddy.
            for level_up_name in LEVEL_UP_NAMES: self.remove_by_name(level_up_name)


            # Add in Bud!
            self.multiworld.state.collect(self.world.create_item(ItemName.BUD_LEVEL_UP), True)

            # The first checks should be available in all cartridges except Have At Thee.
            self.assertTrue(all([
                self.can_reach_location(LocationName.TRASH_DASH_1),
                self.can_reach_location(LocationName.TREATMENT_TO_GO_1),
                self.can_reach_location(LocationName.ACROBIRD_1),
                self.can_reach_location(LocationName.BAZZS_BIG_DAY_1),
            ]))
            self.assertFalse(self.can_reach_location(LocationName.HAVE_AT_THEE_1))

            # Consequently, the first "buddy power" check should also be inaccessible.
            self.assertFalse(self.can_reach_location(LocationName.ALL_BUDDIES_LEVEL_1))

        with self.subTest("Add in Bazz and check that all of the first checks are now accessible"):
            self.multiworld.state.collect(self.world.create_item(ItemName.BAZZ_LEVEL_UP), True)
            self.assertTrue(all([
                self.can_reach_location(LocationName.TRASH_DASH_1),
                self.can_reach_location(LocationName.HAVE_AT_THEE_1),
                self.can_reach_location(LocationName.TREATMENT_TO_GO_1),
                self.can_reach_location(LocationName.ACROBIRD_1),
                self.can_reach_location(LocationName.BAZZS_BIG_DAY_1),
                self.can_reach_location(LocationName.ALL_BUDDIES_LEVEL_1)
            ]))

        with self.subTest(
            "Check that increasing buddy power allows Bud and Bazz to collect a check that was" \
            "inaccessible to either buddy on their own."
        ):
            self.assertFalse(self.can_reach_location(LocationName.ACROBIRD_2))
            self.multiworld.state.collect(self.world.create_item(ItemName.BUDDY_POWER), True)
            self.assertTrue(self.can_reach_location(LocationName.ACROBIRD_2))


    def test_buddy_levels(self) -> None:

        with self.subTest("Test the starting checks for Biff"):
            # Remove the random starting buddy.
            for level_up_name in LEVEL_UP_NAMES: self.remove_by_name(level_up_name)

            # Add in Biff!
            self.multiworld.state.collect(self.world.create_item(ItemName.BIFF_LEVEL_UP), True)

            # The first checks should be available in all cartridges except Acrobird.
            self.assertTrue(all([
                self.can_reach_location(LocationName.TRASH_DASH_1),
                self.can_reach_location(LocationName.HAVE_AT_THEE_1),
                self.can_reach_location(LocationName.TREATMENT_TO_GO_1),
                self.can_reach_location(LocationName.BAZZS_BIG_DAY_1),
            ]))
            self.assertFalse(self.can_reach_location(LocationName.ACROBIRD_1))

        with self.subTest("Level up Biff and check the 2nd goal score locations for his optimal games."):
            # Ensure that the level 2 checks for Biff's optimal games aren't already accessible.
            self.assertFalse(self.can_reach_location(LocationName.TRASH_DASH_2))
            self.assertFalse(self.can_reach_location(LocationName.BAZZS_BIG_DAY_2))

            # Level up Biff!
            self.multiworld.state.collect(self.world.create_item(ItemName.BIFF_LEVEL_UP), True)

            # Now the checks should be accessible!
            self.assertTrue(self.can_reach_location(LocationName.TRASH_DASH_2))
            self.assertTrue(self.can_reach_location(LocationName.BAZZS_BIG_DAY_2))

        with self.subTest("Check accessibility for the victory condition"):
            # The victory condition is inaccessible without all the buddies.
            self.assertFalse(self.can_reach_location(EventName.VICTORY))

            # Even with maxed buddies and 4 out of 5 of the buddy power, it's still inaccessible!
            for _ in range(5):
                self.multiworld.state.collect(self.world.create_item(ItemName.BUD_LEVEL_UP), True)
                self.multiworld.state.collect(self.world.create_item(ItemName.BIFF_LEVEL_UP), True)
                self.multiworld.state.collect(self.world.create_item(ItemName.BENSON_LEVEL_UP), True)
                self.multiworld.state.collect(self.world.create_item(ItemName.BRIE_LEVEL_UP), True)
                self.multiworld.state.collect(self.world.create_item(ItemName.BAZZ_LEVEL_UP), True)
            for _ in range(3):
                self.multiworld.state.collect(self.world.create_item(ItemName.BUDDY_POWER), True)
            self.assertFalse(self.can_reach_location(EventName.VICTORY))

            # Maxing out buddy power finally makes it accessible.
            self.multiworld.state.collect(self.world.create_item(ItemName.BUDDY_POWER), True)
            self.assertTrue(self.can_reach_location(EventName.VICTORY))


    def test_bonus_score(self) -> None:

        with self.subTest("Test the starting checks for Biff"):
            # Remove the random starting buddy.
            for level_up_name in LEVEL_UP_NAMES: self.remove_by_name(level_up_name)

            # Add in Benson!
            self.multiworld.state.collect(self.world.create_item(ItemName.BENSON_LEVEL_UP), True)

            # The first checks should be available in all cartridges except Acrobird.
            self.assertTrue(all([
                self.can_reach_location(LocationName.TRASH_DASH_1),
                self.can_reach_location(LocationName.HAVE_AT_THEE_1),
                self.can_reach_location(LocationName.TREATMENT_TO_GO_1),
                self.can_reach_location(LocationName.BAZZS_BIG_DAY_1),
            ]))
            self.assertFalse(self.can_reach_location(LocationName.ACROBIRD_1))

        with self.subTest("Add in some bonus score so that the first Acrobird check is now collectible"):
            self.multiworld.state.collect(self.world.create_item(ItemName.ACROBIRD_SCORE), True)
            self.assertTrue(self.can_reach_location(LocationName.ACROBIRD_1))

        with self.subTest("Add in additional bonus score without additional buddy power"):
            # We need 97 bonus points to hit the 100-point goal.
            # 10 more bonus score checks gives us 11 in total, which should give:
            # 10 (5*2) points from the first two bonuses + 90 (10*9) points from the other 9 = 100 points.
            for _ in range(10):
                self.multiworld.state.collect(self.world.create_item(ItemName.ACROBIRD_SCORE), True)

            # Now, *in theory* we have enough bonus points for all the Acrobird goal scores.
            # However, in practice nothing above the second goal score is in logic until we have more buddy power.
            # (This is the "soft logic" that helps prevent the fill algorithm from placing buddy power too late
            # due to an excess of bonus score items still waiting to be placed.)
            self.assertTrue(self.can_reach_location(LocationName.ACROBIRD_2))
            self.assertFalse(self.can_reach_location(LocationName.ACROBIRD_3))
            self.assertFalse(self.can_reach_location(LocationName.ACROBIRD_4))
            self.assertFalse(self.can_reach_location(LocationName.ACROBIRD_5))

        with self.subTest("Add in buddy power to until all Acrobird locations are accessible."):
            # Adding in one more buddy power makes the 3rd and 4th goal scores available (but not the 5th).
            self.multiworld.state.collect(self.world.create_item(ItemName.BUDDY_POWER), True)
            self.assertTrue(self.can_reach_location(LocationName.ACROBIRD_3))
            self.assertTrue(self.can_reach_location(LocationName.ACROBIRD_4))
            self.assertFalse(self.can_reach_location(LocationName.ACROBIRD_5))

            # And adding in another buddy power (for 3 total) makes all the Acrobird goal scores accessible!
            self.multiworld.state.collect(self.world.create_item(ItemName.BUDDY_POWER), True)
            self.assertTrue(self.can_reach_location(LocationName.ACROBIRD_5))
