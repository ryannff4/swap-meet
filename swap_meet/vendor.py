class Vendor:
    inventory = []

    def __init__(self, inventory=[]):
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        try:
            self.inventory.remove(item)
            return item
        except ValueError:
            return False

    def get_by_id(self, item_id: int):
        for item in self.inventory:
            if item.id == item_id:
                return item
        return None

    def swap_items(self, other_vendor, my_item, their_item) -> bool:
        if self.get_by_id(my_item.id) is None or other_vendor.get_by_id(their_item.id) is None:
            return False
        other_vendor.add(self.remove(my_item))
        self.add(other_vendor.remove(their_item))
        return True

    def swap_first_item(self, other_vendor):
        if len(self.inventory) == 0 or len(other_vendor.inventory) == 0:
            return False
        self_first_item = self.inventory.pop(0)
        other_first_item = other_vendor.inventory.pop(0)
        self.add(other_first_item)
        other_vendor.add(self_first_item)
        return True
