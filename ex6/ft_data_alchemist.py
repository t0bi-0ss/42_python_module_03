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


def players_dict_builder(player_names: list[str]) -> dict[str, int]:
    
