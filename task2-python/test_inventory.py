import pytest
from inventory import Inventory


def test_add_new_item():
    inv = Inventory()
    inv.add_item("apple", 10, 0.50)
    assert len(inv) == 1


def test_add_existing_item_increases_quantity():
    inv = Inventory()
    inv.add_item("apple", 10, 0.50)
    inv.add_item("apple", 5, 0.50)
    assert inv.get_item("apple")["quantity"] == 15


def test_get_total_value():
    inv = Inventory()
    inv.add_item("apple", 10, 0.50)
    inv.add_item("banana", 4, 0.30)
    assert inv.get_total_value() == pytest.approx(6.20)
