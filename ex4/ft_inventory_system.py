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


def main():
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


if __name__ == "__main__":
    main()
