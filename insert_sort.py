import unittest


def insert_sort(data:list):
    if not data:
        return []
    else:
        return insert(data[0], insert_sort(data[1:]))


def insert(datum, data):
    if not data:
        return [datum]
    else:
        if datum <= data[0]:
            return [datum] + data
        else:
            return [data[0]] + insert(datum, data[1:])


class MyTestCase(unittest.TestCase):
    def test_sorting_empty_list(self):
        data = []
        self.assertEqual([], insert_sort(data))

    def test_sorting_sorted_list(self):
        data = [1,2,3]
        self.assertEqual(data, insert_sort(data))

    def test_sorting_one_item_list(self):
        data = [1]
        self.assertEqual(data, insert_sort(data))

    def test_sorting_reversed_sorted_list(self):
        data = [3,2,1]
        self.assertEqual([1,2,3], insert_sort(data))

    def test_sorting_sorted_negative_value_list(self):
        data = [-3,-2,-1]
        self.assertEqual(data, insert_sort(data))

    def test_sorting_reversed_sorted_negative_value_list(self):
        data = [-1,-2,-3]
        self.assertEqual([-3,-2,-1], insert_sort(data))

    def test_sorting_mixed_negative_positive_value_list(self):
        data = [-1,2,-3]
        self.assertEqual([-3,-1,2], insert_sort(data))


if __name__ == '__main__':
    unittest.main()