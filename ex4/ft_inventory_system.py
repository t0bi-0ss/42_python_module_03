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



def 
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
        item_list: list[str | int] = item.split(":")


if __name__ == "__main__":
    main()
