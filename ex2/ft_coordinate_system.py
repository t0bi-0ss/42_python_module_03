import math


def no_consecutive_commas(string: str) -> int:
    if string.count(",,"):
        return 0
    return 1


def has_right_syntax(string: str) -> int:
    if not no_consecutive_commas(string):
        return 0
    commas_found = string.count(',')
    if commas_found:
        words_count = len(string.split(','))
    else:
        words_count = len(string.split(' '))
    return (commas_found == (words_count - 1))


def get_player_pos() -> tuple[int, ...]:
    while True:
        coordinates = input("Enter new coordinates"
                            + " as floats in format 'x,y,z': ")
        if not has_right_syntax(coordinates):
            print("Invalid syntax")
            continue
        try:
            1 / len(coordinates.split())
            i = 0
            coordinates = coordinates.split(",")
            while i < len(coordinates):
                coordinates[i] = float(coordinates[i])
                i += 1
            break
        except ZeroDivisionError:
            print("Error: No coordinates were passed")
        except ValueError:
            print(
                f"Error on parameter '{coordinates[i]}': "
                "could not convert string to float: "
                + f"'{coordinates[i]}'")
    if (len(coordinates)) < 3:
        print("Error: less than 3 coordinates were passed")
        coordinates = get_player_pos()
    elif len(coordinates) > 3:
        print("Error: more than 3 coordinates were passed")
        coordinates = get_player_pos()
    return tuple(coordinates)


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    coordinates = get_player_pos()
    print("Got a first tuple: ", end="")
    print(coordinates)
    print(
        "It includes: "
        + f"X={coordinates[0]}, "
        + f"Y={coordinates[1]}, "
        + f"Z={coordinates[2]}"
    )
    distance_to_center = math.sqrt(
        coordinates[0] ** 2 + coordinates[1] ** 2 + coordinates[2] ** 2
    )
    print("Distance to center: " + f"{distance_to_center:.4f}")
