import uuid

class Item:
    id = None

    def __init__(self, new_id=uuid.uuid4().int):
        self.id = new_id

    def get_category(self) -> str:
        return str(self.__class__.__name__)

