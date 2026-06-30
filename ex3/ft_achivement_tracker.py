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
    random_selection = []
    i = 1
    for achievement in achievements:
        if i == random_num_of_achievements:
            break
        i += 1
        random_selection.append(achievement)
    return set(random_selection)


def common_achievements(
        players_achievements: dict[str, set[str]]
        ) -> set[str]:
    """Find common achievements among the sets in passed dict"""
    if not players_achievements:
        return set()
    return set.intersection(*players_achievements.values())


def unique_achievement(
        target_set: set[str],
        players_achievements: dict[str, set[str]]
        ) -> set[str]:
    """Find unique achivement in target_set compared to
    all other sets in passed dict"""
    if (
        not target_set or not players_achievements
    ):
        return set()
    target_set_copy = target_set
    for a_set in players_achievements.values():
        if a_set == target_set_copy:
            continue
        target_set_copy.difference_update(a_set)
    return target_set_copy


def missing_achievements(
        target_set: set[str],
        all_achievemets_set: set[str]
        ) -> set[str]:
    """Finds missing achivements in target_set
    considering achievements_set"""
    if (
        not target_set
        or not all_achievemets_set
    ):
        return set()
    return all_achievemets_set.difference(target_set)


def distinct_achievements(
        players_achievements: dict[str, set[str]]
        ) -> set[str]:
    """Returns all achivements among all players"""
    if (
        not players_achievements
    ):
        return set()
    return set.union(*players_achievements.values())


def print_players_achievements(
        players_achievements: dict[str, set[str]]
        ) -> None:
    if not players_achievements:
        return
    for name, achievements in players_achievements.items():
        print(f"Player {name}: ", end="")
        print(achievements)


if __name__ == "__main__":
    players = ["Alice", "Bob", "Charlie", "Dylan"]
    players_achievements = {
        name: gen_player_achievements() for name in players
        }
    print("=== Achievements Tracker System ===\n")
    print_players_achievements(players_achievements)
    print(
        "\nAll distinct achievements: ",
        distinct_achievements(players_achievements)
    )
    print(
        "\nCommon achievements: ",
        common_achievements(players_achievements)
    )
    print()
    for key, value in players_achievements.items():
        print(f"Only {key} has: ", end="")
        print(unique_achievement(value, players_achievements))
    print()
    all_achievements_set = gen_player_achievements(True)
    for key, value in players_achievements.items():
        print(f"{key}")
