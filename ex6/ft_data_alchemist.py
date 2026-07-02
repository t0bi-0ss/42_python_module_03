import random

"""Module for Data alchemy"""


def capitalized_list_builder(original_list: list[str]) -> list[str]:
    """Builds a list from original_list with all it's strings capitalized"""
    if not original_list:
        print("List must not be empty")
        return []
    for s in original_list:
        try:
            s.capitalize()
        except ValueError as msg:
            print(
                "Error: original_list must be list[str] only\n",
                msg
            )
            return []
    return [name.capitalize() for name in original_list]


def only_capitalized_list_builder(original_list: list[str]) -> list[str]:
    """Builds a list from original_list
    with all it's strings that are already capitalized"""
    if not original_list:
        print("List must not be empty")
        return []
    for s in original_list:
        try:
            s.capitalize()
        except ValueError as msg:
            print(
                "Error: original_list must be list[str] only\n",
                msg
            )
            return []
    return [name for name in original_list if name == name.capitalize()]


def players_dict_builder(
        player_names: list[str], range_max: int, range_min: int = 0
        ) -> dict[str, int]:
    """Builds a dict from player_names with random scores"""
    if not player_names:
        print("List must not be empty")
        return {}
    try:
        range_max + 1
        range_min + 1
    except TypeError as msg:
        print("Error: range_max and range_min must be ints:", msg)
        return {}
    if range_max <= 0:
        print("Range max and min can't be 0 or negative")
        return {}
    if range_max <= range_min:
        print("Range max must be grater than range_min")
        return {}
    for s in player_names:
        try:
            s + "abc"
        except TypeError as msg:
            print(
                "Error: player_names must be list[str] only:",
                msg
            )
            return {}
    return {name: random.randint(range_min, range_max)
            for name in player_names}


def high_scores_builder(
        score_dict: dict[str, int], average: int
        ) -> dict[str, int]:
    """Builds a dict from score_dict with keys that correspond to values
    greater than average"""
    if not score_dict:
        return {}
    try:
        average + 1
    except TypeError as msg:
        print(
            "Error: average must be an int:", msg
        )
        return {}
    for key in score_dict.keys():
        try:
            key + "abc"
        except ValueError as msg:
            print(
                "Error: all keys in score_dict must be strings:", msg
            )
            return {}
    for value in score_dict.values():
        try:
            value + 1
        except TypeError as msg:
            print(
                "Error: all values in score_dict must be ints:", msg
            )
            return {}
    return {key: value for key, value in score_dict.items() if value > average}


def main() -> None:

    names_list = [
        'Alice', 'bob', 'Charlie', 'dylan',
        'Emma', 'Gregory', 'john', 'kevin', 'Liam'
        ]

    print("=== Game Data Alchemist ===\n")
    print(
        "Initial list of players:",
        names_list,
        "\n"
    )

    capitalized_list = capitalized_list_builder(names_list)
    print(
        "New list with all names capitalized:",
        capitalized_list,
        "\n"
    )

    only_capitalized_list = only_capitalized_list_builder(names_list)
    print(
        "New list of capitalized names only:",
        only_capitalized_list,
        "\n"
    )

    score_dict = players_dict_builder(capitalized_list, 1000)
    print(
        "Score dict:",
        score_dict,
        "\n"
    )

    score_average = sum(score_dict.values()) / len(score_dict)
    print(
        f"Score average is {score_average:.2f}\n"
    )

    high_scores = high_scores_builder(score_dict, score_average)
    print(
        "High scores:",
        high_scores
    )


if __name__ == "__main__":
    main()
