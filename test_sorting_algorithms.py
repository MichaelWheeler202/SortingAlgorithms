import SortingAlgorithms as Sort

test_list_1 = [5, 3, 6, 1, 2, 4]
sorted_list_1 = [1, 2, 3, 4, 5, 6]

test_list_2 = [1]
sorted_list_2 = [1]

test_list_3 = [7, -1, 3, -2, 9, 0]
sorted_list_3 = [-2, -1, 0, 3, 7, 9]


def test_insertion_sort():
    assert Sort.insertion_sort(test_list_1)[0] == sorted_list_1
    assert Sort.insertion_sort(test_list_2)[0] == sorted_list_2
    assert Sort.insertion_sort(test_list_3)[0] == sorted_list_3

def test_merge_sort():
    assert Sort.merge_sort(test_list_1)[0] == sorted_list_1
    assert Sort.merge_sort(test_list_2)[0] == sorted_list_2
    assert Sort.merge_sort(test_list_3)[0] == sorted_list_3


def test_counting_sort():
    assert Sort.counting_sort(test_list_1)[0] == sorted_list_1
    assert Sort.counting_sort(test_list_2)[0] == sorted_list_2
    assert Sort.counting_sort(test_list_3)[0] == sorted_list_3
