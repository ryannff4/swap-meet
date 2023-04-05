import uuid


class Item:
    id = None
    condition = 0
    # this should work, but for some reason generates the same UUID for multiple instantations, e.g. in unit test
    # def __init__(self, id=uuid.uuid4()):
    #     self.id = new_id.int

    def __init__(self, id = None, condition=0):
        if id is None:
            self.id = uuid.uuid4().int
        else:
            self.id = id

        self.condition = condition

    def get_category(self) -> str:
        return str(self.__class__.__name__)

    def __str__(self):
        return f'An object of type Item with id {self.id}.'

    def condition_description(self):
        condition_map = {0: 'Not usable.',
                         1: 'Badly damaged.',
                         2: 'Somewhat damaged.',
                         3: 'Used.',
                         4: 'Minor usage.',
                         5: 'Mint.'}

        return condition_map.get(self.condition)
