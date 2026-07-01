import sys

"""
A module to organize an inventory of items
"""


class RedundantItem(Exception):
    """A basic error for redundant items"""

    def __init__(self, item_name: str) -> None:
        self.message: str = f"Redundant item '{item_name}' - discarding"
        super().__init__(self.message)

    def __str__(self) -> str:
        return f"{self.message}"


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
        item_list: list[str, int] = item.split(":")


if __name__ == "__main__":
    main()
