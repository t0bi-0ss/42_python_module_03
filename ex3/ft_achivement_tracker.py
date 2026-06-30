import random

"""Module for a players achievement system"""


def gen_player_achievements(
        all_achievements: bool = False
        ) -> set[str]:
    """Generate a random set of achievements for a player"""
    achievements = {
        'Crafting Genius',
        'Strategist',
        'World Savior',
        'Speed Runner',
        'Survivor',
        'Master Explorer',
        'Treasure Hunter',
        'Unstoppable',
        'First Steps',
        'Collector Supreme',
        'Untouchable',
        'Sharp Mind',
        'Boss Slayer'
    }
    if all_achievements:
        return achievements
    random_num_of_achievements = random.randint(1, len(achievements))
    random_selection = random.sample(
        list(achievements),
        random_num_of_achievements
    )
    return set(random_selection)


def common_achievements(*achievements_sets: set[str]) -> set[str]:
    """Find common achievements among passed sets"""
    if not achievements_sets:
        return set()
    return set.intersection(*achievements_sets)


def unique_achievement(
        target_set: set[str],
        *rest_of_sets: set[str]
        ) -> set[str]:
    """Find unique achivement in target_set compared to
    all other passed sets"""
    if (
        not target_set or not rest_of_sets
    ):
        return set()
    for a_set in rest_of_sets:
        target_set.difference_update(a_set)
    return target_set


def missing_achievements(
        target_set: set[str],
        achievemets_set: set[str]
        ) -> set[str]:
    """Finds missing achivements in target_set
    considering achievements_set"""
    if (
        not target_set
        or not achievemets_set
    ):
        return set()
    return achievemets_set.difference(target_set)


if __name__ == "__main__":
    players = ["Alice", "Bob", "Charlie", "Dylan"]
    players_achievements = {
        name: gen_player_achievements() for name in players
        }
    print("=== Achievements Tracker System ===\n")
    for name, achievements in players_achievements.items():
        print(f"Player {name}: ", end="")
        print(achievements)
