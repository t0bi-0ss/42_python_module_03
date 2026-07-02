import math
"""A module to take and store sets of three coordinates.
It can print them and calculate distances between the center or
 a different set of coordinates"""


def get_player_pos() -> tuple[float, ...]:
    """Takes coordinates of a player's position validating the input data"""
    coordinates_f = []
    while True:
        coordinates = input("Enter new coordinates"
                            + " as floats in format 'x,y,z': ")
        if not coordinates.count(','):
            print("Invalid syntax")
            continue
        try:
            1 / len(coordinates.split())
            i = 0
            coordinates_l = coordinates.split(",")
            while i < len(coordinates_l):
                coordinates_f.append(float(coordinates_l[i]))
                i += 1
        except ZeroDivisionError:
            print("Error: No coordinates were passed")
        except ValueError:
            print(
                f"Error on parameter '{coordinates_l[i]}': "
                "could not convert string to float: "
                + f"'{coordinates_l[i]}'")
            coordinates_f.clear()
        else:
            if len(coordinates_f) == 3:
                break
            if (len(coordinates_l)) < 3:
                print("Error: less than 3 coordinates were passed")
                coordinates_f.clear()
                continue
            elif len(coordinates_l) > 3:
                print("Error: more than 3 coordinates were passed")
                coordinates_f.clear()
                continue
    return tuple(coordinates_f)


def distance_to_center(coordinates: tuple[float, ...]) -> float:
    return (math.sqrt(
        coordinates[0] ** 2
        + coordinates[1] ** 2
        + coordinates[2] ** 2
    ))


def distance_between_coordinates(
        coordinates_1: tuple[float, ...],
        coordinates_2: tuple[float, ...]
        ) -> float:
    return math.sqrt(
        (coordinates_2[0] - coordinates_1[0]) ** 2
        + (coordinates_2[1] - coordinates_1[1]) ** 2
        + (coordinates_2[2] - coordinates_1[2]) ** 2
    )


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    coordinates_1 = get_player_pos()
    print("Got a first tuple: ", end="")
    print(coordinates_1)
    print(
        "It includes: "
        + f"X={coordinates_1[0]}, "
        + f"Y={coordinates_1[1]}, "
        + f"Z={coordinates_1[2]}"
    )
    distance_to_center_1 = distance_to_center(coordinates_1)
    print("Distance to center: " + f"{distance_to_center_1:.4f}\n")
    print("Get a second set of coordinates")
    coordinates_2 = get_player_pos()
    print(
        "Distance between the 2 sets of coordinates: ",
        end=""
    )
    print(f"{distance_between_coordinates(coordinates_1, coordinates_2):.4f}")
