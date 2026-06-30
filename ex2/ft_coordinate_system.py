import math


def get_player_pos() -> tuple[int, ...]:
    """Takes coordinates of a player's position validating the input data"""
    while True:
        coordinates = input("Enter new coordinates"
                            + " as floats in format 'x,y,z': ")
        if not coordinates.count(','):
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
    
