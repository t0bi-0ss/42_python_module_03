import random

"""Module for a players achievement system"""


def gen_player_achievements(all_achievements: bool = False) -> set[str]:
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
    if not achievements_sets:
        return set()
    return set.intersection(*achievements_sets)


def unique_achievement(
        target_set: set[str],
        *rest_of_sets: set[str]
        ) -> set[str]:
    if (
        not target_set or not rest_of_sets
    ):
        return set()
    for a_set in rest_of_sets:
        target_set.difference_update(a_set)
    return target_set


if __name__ == "__main__":
    print(gen_player_achievements())
