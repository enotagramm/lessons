import unittest


def merge_sort(array, left_indx, right_indx):
    if left_indx >= right_indx:
        return

    middle = (left_indx + right_indx) // 2
    merge_sort(array, left_indx, middle)
    merge_sort(array, middle+1, right_indx)
    merge(array, left_indx, right_indx, middle)


def merge(array, left_indx, right_indx, middle):
    left_copy = array[left_indx:middle+1]
    right_copy = array[middle+1:right_indx+1]

    left_copy_indx = 0
    right_copy_indx = 0
    sorted_indx = left_indx

    while left_copy_indx < len(left_copy) and right_copy_indx < len(right_copy):
        if left_copy[left_copy_indx] <= right_copy[right_copy_indx]:
            array[sorted_indx] = left_copy[left_copy_indx]
            left_copy_indx = left_copy_indx + 1
        else:
            array[sorted_indx] = right_copy[right_copy_indx]
            right_copy_indx = right_copy_indx + 1

        sorted_indx = sorted_indx + 1

    while left_copy_indx < len(left_copy):
        array[sorted_indx] = left_copy[left_copy_indx]
        left_copy_indx = left_copy_indx + 1
        sorted_indx = sorted_indx + 1

    while right_copy_indx < len(right_copy):
        array[sorted_indx] = right_copy[right_copy_indx]
        right_copy_indx = right_copy_indx + 1
        sorted_indx = sorted_indx + 1


array = [33, 42, 9, 37, 8, 47, 5, 29, 49, 31, 4, 48, 16, 22, 26]
merge_sort(array, 0, len(array)-1)
print(array)


class TestMerge(unittest.TestCase):
    test_array = [33, 42, 9, 37, 8, 47, 5, 29, 49, 31, 4, 48, 16, 22, 26]

    def test_sorted(self):
        sort_default = sorted(self.test_array)
        self.assertEqual(sort_default, array)

    def test_not_sorted(self):
        self.assertNotEqual(self.test_array, array)

    def test_quantity(self):
        self.assertCountEqual(self.test_array, array)
