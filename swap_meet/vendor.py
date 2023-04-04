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
