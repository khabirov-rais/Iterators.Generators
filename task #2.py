import types


def flat_generator(list_of_lists):

    item_one_line_list = 0
    item_list_of_list = 0

    while len(list_of_lists) > item_list_of_list:

        item = list_of_lists[item_list_of_list][item_one_line_list]
        item_one_line_list += 1

        if item_one_line_list >= len(list_of_lists[item_list_of_list]):
            item_one_line_list = 0
            item_list_of_list += 1

        yield item


def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()