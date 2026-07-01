import sys

"""
A module to organize an inventory of items
"""


class WrongItem(Exception):
    """A basic error for wrong items"""

    def __init__(self, message: str = "Unspecified WrongItem error") -> None:
        self.message: str = message
        super().__init__(self.message)

    def __str__(self) -> str:
        return f"{self.message}"


class RedundantItem(WrongItem):
    """WrongItem error for redundant items"""

    def __init__(self, item_name: str) -> None:
        if item_name:
            self.message: str = f"Redundant item '{item_name}' - discarding"
        else:
            self.message = None
        super().__init__(self.message)

    def __str__(self) -> str:
        return f"{self.message}"


class InvalidParameter(WrongItem):
    """WrongItem error for invalid parameters"""

    def __init__(self, parameter: str) -> None:
        if parameter:
            self.message: str = f"Error invalid parameter '{parameter}'"
        else:
            self.message = None
        super().__init__(self.message)

    def __str__(self) -> str:
        return f"{self.message}"


def is_redundant(item_name: str, items_dict: dict[str, int]) -> None:
    """Checks if item_name already exists in items_dict"""
    if item_name in items_dict:
        raise RedundantItem(item_name)


def is_invalid(parameter: str) -> None:
    """Checks if parameter's syntax is valid"""

    parameter_list = parameter.split(":")
    if len(parameter_list) != 2:
        raise InvalidParameter(parameter)


def main() -> None:
    """
    Organize inventory
    """
    print("=== Inventory System Analysis === \n")

    if len(sys.argv) < 2:
        print(
            "No items provided. Usage: python3 ft_inventory_system.py",
            " <item_name_1:quantity> <item_name_2:quantity> ...",
        )
        sys.exit()

    items_dict: dict[str, int] = {}

    for item in sys.argv[1:]:
        try:
            is_invalid(item)
            item_list: list[str | int] = item.split(":")
            is_redundant(item_list[0], items_dict)
            int(item_list[1])
        except (InvalidParameter, RedundantItem) as msg:
            print(msg)
        except ValueError as msg:
            print(
                f"Quantity error for '{item_list[0]}':",
                msg
                )
        else:
            items_dict[item_list[0]] = int(item_list[1])

    print(
        "Got inventory: ",
        items_dict
        )

    print("\nItem list: ", end="")
    items_list = [key for key in items_dict.keys()]
    print(items_list)

    total_quantity = 0
    for value in items_dict.values():
        total_quantity += value
    print(
        "\nTotal quantity of the",
        len(item_list),
        "items:",
        total_quantity
    )

    print()
    for key in items_dict.keys():
        print(
            f"Item {key} represents",
            f"{items_dict[key]/total_quantity*100:.1f}%"
        )

    max_key: str = ""
    max_quantity: int = 0
    min_key: str = ""
    min_quantity: float = float('inf')
    for key in items_dict.keys():
        if items_dict[key] > max_quantity:
            max_quantity = items_dict[key]
            max_key = key
        if items_dict[key] < min_quantity:
            min_quantity = items_dict[key]
            min_key = key
    print(
        "\nItem most abundant:",
        max_key,
        "with quantity",
        max_quantity
        )
    print(
        "\nItem least abundant:",
        min_key,
        "with quantity",
        min_quantity
    )

    items_dict.update({"magic_item": 1})
    print(
        "\nUpdated inventory",
        items_dict
    )


if __name__ == "__main__":
    main()
