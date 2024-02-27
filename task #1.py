class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.item_list_of_list = 0
        self.item_one_line_list = 0
        return self

    def __next__(self):
        if len(self.list_of_list) < self.item_list_of_list + 1:
            raise StopIteration

        self.item = self.list_of_list[self.item_list_of_list][self.item_one_line_list]
        self.item_one_line_list += 1
        if self.item_one_line_list == len(self.list_of_list[self.item_list_of_list]):
            self.item_one_line_list = 0
            self.item_list_of_list += 1
        return self.item


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()