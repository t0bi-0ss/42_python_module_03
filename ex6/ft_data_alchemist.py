import random

"""Module for Data alchemy"""


def capitalized_list_builder(original_list: list[str]) -> list[str]:
    """Builds a list from original_list with all it's strings capitalized"""
    if not original_list:
        print("List must not be empty")
        return None
    for s in original_list:
        try:
            s.capitalize()
        except ValueError as msg:
            print(
                "Error: original_list must be list[str] only\n",
                msg
            )
            return None
    return [name.capitalize() for name in original_list]


def only_capitalized_list_builder(original_list: list[str]) -> list[str]:
    """Builds a list from original_list
    with all it's strings that are already capitalized"""
    if not original_list:
        print("List must not be empty")
        return None
    for s in original_list:
        try:
            s.capitalize()
        except ValueError as msg:
            print(
                "Error: original_list must be list[str] only\n",
                msg
            )
            return None
    return [name for name in original_list if name == name.capitalize()]


def players_dict_builder(
        player_names: list[str], range_max: int, range_min: int = 0
        ) -> dict[str, int]:
    """Builds a dict from player_names with random scores"""
    if not player_names:
        print("List must not be empty")
        return None
    try:
        range_max + 1
        range_min + 1
    except TypeError as msg:
        print("Error: range_max and range_min must be ints:", msg)
        return None
    if range_max <= 0:
        print("Range max and min can't be 0 or negative")
        return
    for s in player_names:
        try:
            s.capitalize()
        except ValueError as msg:
            print(
                "Error: player_names must be list[str] only:",
                msg
            )
            return None
    return {name: random.randint(0, range_max) for name in player_names}


def greater_dict_builder()
