class Inventory:
    """A simple inventory management system."""

    def __init__(self):
        self._items = {}

    def add_item(self, name: str, quantity: int, price: float) -> None:
        """Add a new item or increase the quantity of an existing one."""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        if price < 0:
            raise ValueError("Price cannot be negative")
        if name in self._items:
            self._items[name]["quantity"] += quantity
        else:
            self._items[name] = {"quantity": quantity, "price": price}

    def remove_item(self, name: str) -> None:
        """Remove an item from the inventory entirely."""
        if name not in self._items:
            raise KeyError(f"Item '{name}' not found in inventory")
        del self._items[name]

    def update_quantity(self, name: str, quantity: int) -> None:
        """Set the quantity of an existing item."""
        if name not in self._items:
            raise KeyError(f"Item '{name}' not found in inventory")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self._items[name]["quantity"] = quantity

    def get_item(self, name: str) -> dict:
        """Return a copy of the item record for the given name."""
        if name not in self._items:
            raise KeyError(f"Item '{name}' not found in inventory")
        return self._items[name].copy()

    def apply_discount(self, name: str, discount_percent: float) -> None:
        """Reduce the price of an item by the given percentage (0–100)."""
        if name not in self._items:
            raise KeyError(f"Item '{name}' not found in inventory")
        if not 0 <= discount_percent <= 100:
            raise ValueError("Discount must be between 0 and 100")
        self._items[name]["price"] *= 1 - discount_percent / 100

    def get_total_value(self) -> float:
        """Return the total value of all items (quantity × price)."""
        return sum(item["quantity"] * item["price"] for item in self._items.values())

    def get_low_stock_items(self, threshold: int = 5) -> list:
        """Return names of items whose quantity is at or below the threshold."""
        return [name for name, item in self._items.items() if item["quantity"] <= threshold]

    def clear(self) -> None:
        """Remove all items from the inventory."""
        self._items.clear()

    def __len__(self) -> int:
        return len(self._items)
