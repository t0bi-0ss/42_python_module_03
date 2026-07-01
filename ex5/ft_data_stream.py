import random

import typing

"""Module to generate events"""


def gen_event():
    names_list: list[str] = ["bob", "alice", "dylan", "charlie"]
    actions_list: list[str] = [
        "run", "eat", "grab", "sleep", "move", "climb", "swim", "release"
        ]
    yield (random.choice(names_list), random.choice(actions_list))


