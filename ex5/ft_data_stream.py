import random

import typing

"""Module to generate events"""


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    """Generate a random event"""
    names_list: list[str] = ["bob", "alice", "dylan", "charlie"]
    actions_list: list[str] = [
        "run", "eat", "grab", "sleep", "move", "climb", "swim", "release"
        ]
    yield (random.choice(names_list), random.choice(actions_list))


def event_display(event_t: tuple[str, str]) -> None:
    """Display event"""
    print(
        f"Player {event_t[0]}",
        f"did action {event_t[1]}"
    )


def consume_event(
        event_tuples_list: list[tuple[str, str]]
        ) -> typing.Generator[tuple[str, str], None, None]:
    yield event_tuples_list.remove(random.choice(event_tuples_list))


def main() -> None:
    print("=== Game Data Stream Processor ===\n")
    for i in range(0, 1000):
        print(
            f"Event {i}: ", end=""
        )
        event_display(next(gen_event()))
    event_tuples_list: list[tuple[str, str]] = [
        next(gen_event()) for i in range(0, 10)
        ]
    print(
        "\nBuilt list of 10 events:",
        event_tuples_list
    )


if __name__ == "__main__":
    main()
