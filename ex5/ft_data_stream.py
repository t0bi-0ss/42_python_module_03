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
    if n <= 0:
        print("Number of events can't be 0 or negative")
        return
    for i in range(0, n):
        print(
            f"Event {i}: ", end=""
        )
        event_display(next(gen_event()))


def event_list_builder(n: int) -> tuple[str, str]:
    """Builds a list of n event tuples"""
    if n <= 0:
        print("Number of event tuples can't be 0 or negative")
    event_list = [
        next(gen_event()) for i in range(0, n)
    ]
    print(
        f"\nBuilt list of {n} events:",
        event_list
    )
    return event_list


def event_consumer(n: int, event_tuple_list: list[tuple[str, str]]) -> None:
    """Consumes n events from event_tuple_list"""
    if n <= 0:
        print("\nNumber of events to consume can't be 0 or negative")
        return None
    if not event_tuple_list:
        print("\nNo event to consume: event_tuple_list is already empty")
        return None
    print(
        "\nGot event from list:",
        next(consume_event(event_tuple_list)),
        "\nRemains in list:",
        event_tuple_list
    )
    if n-1 > 0:
        event_consumer(n-1, event_tuple_list)


def main() -> None:
    print("=== Game Data Stream Processor ===\n")

    print_n_events(1000)

    print("\n----> Build list <----")
    event_tuples_list: list[tuple[str, str]] = event_list_builder(10)

    print("\n----> Start consuming events <----")
    event_consumer(12, event_tuples_list)


if __name__ == "__main__":
    main()
