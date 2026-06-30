import random

from random import sample

"""Module for a players achievement system"""


def gen_player_achievements(all_achievements: bool = False) -> set:
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
    random_selection = sample(
        list(achievements),
        random_num_of_achievements
    )
    return set(random_selection)


if __name__ == "__main__":
    print(gen_player_achievements())
