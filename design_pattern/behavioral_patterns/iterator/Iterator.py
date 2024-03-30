"""
This is a code example with wrong approach.
We created this code intentionally to demonstrate iterator concept in the next part
"""

class CustomList:
    def __init__(self):
        self._items = []

    def add_item(self, item):
        self._items.append(item)

    def get_items(self):
        return self._items

# Client code
if __name__ == "__main__":
    custom_list = CustomList()
    custom_list.add_item(1)
    custom_list.add_item(2)
    custom_list.add_item(3)

    for item in custom_list.get_items():
        print(item)



"""
This is a code example with right approach. 
we used iterator concept in this code to implement custom iterator for iterate over items
"""


class CustomListIterator:
    def __init__(self, custom_list):
        self._custom_list = custom_list
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._custom_list):
            item = self._custom_list[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration

class CustomList:
    def __init__(self):
        self._items = []

    def add_item(self, item):
        self._items.append(item)

    def __iter__(self):
        return CustomListIterator(self._items)

# Client code
if __name__ == "__main__":
    custom_list = CustomList()
    custom_list.add_item(1)
    custom_list.add_item(2)
    custom_list.add_item(3)

    for item in custom_list:
        print(item)
