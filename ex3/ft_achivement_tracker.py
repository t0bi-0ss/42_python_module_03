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
    return set(
            sample(
                list(achievements),
                random.randint(
                    1, achievements.len()
                    )
                )
            )


