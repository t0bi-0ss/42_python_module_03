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
    """Generator that consumes an event from a list and yields it"""
    if not event_tuples_list:
        return None
    yield event_tuples_list.pop(random.randint(0, len(event_tuples_list) - 1))


def print_n_events(n: int) -> None:
    """Print n number of events"""
    for i in range(0, n):
        print(
            f"Event {i}: ", end=""
        )
        event_display(next(gen_event()))


def main() -> None:
    print("=== Game Data Stream Processor ===\n")

    print_n_events(1000)

    event_tuples_list: list[tuple[str, str]] = [
        next(gen_event()) for i in range(0, 10)
        ]
    print(
        "\nBuilt list of 10 events:",
        event_tuples_list
    )

    for i in range(0, 12):
        if event_tuples_list:
            print(
                "Got event from list:",
                next(consume_event(event_tuples_list)),
                "\nRemains in list:",
                event_tuples_list
            )
        else:
            print("No event to consume: empty list")


if __name__ == "__main__":
    main()
