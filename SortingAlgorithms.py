
import time


def insertion_sort(list_to_sort):

    start_time = time.clock()

    for i in range(1, len(list_to_sort)):  # 0 starts as organized, this is the index of our value to insert
        for j in range(i, 0, -1):   # iterate through sorted list, swapping until we hit an element less than
                                    # or equal to the element at position i

            if list_to_sort[j] < list_to_sort[j-1]:  # if prev value is less swippity swappity
                temp = list_to_sort[j-1]
                list_to_sort[j-1] = list_to_sort[j]
                list_to_sort[j] = temp

            else: # done swapping
                break

    end_time = time.clock()

    time_to_sort = end_time - start_time

    return list_to_sort, round(time_to_sort, 6)


def merger(sorted_list_a, sorted_list_b):

    sorted_list = []

    list_a_len = len(sorted_list_a)
    list_b_len = len(sorted_list_b)

    a_index = 0
    b_index = 0

    while a_index < list_a_len or b_index < list_b_len:
        if a_index == list_a_len:
            sorted_list.append(sorted_list_b[b_index])
            b_index = b_index + 1

        elif b_index == list_b_len:
            sorted_list.append(sorted_list_a[a_index])
            a_index = a_index + 1

        else:
            if sorted_list_a[a_index] < sorted_list_b[b_index]:
                sorted_list.append(sorted_list_a[a_index])
                a_index = a_index + 1

            else:
                sorted_list.append(sorted_list_b[b_index])
                b_index = b_index + 1

    return sorted_list


def merge_sorting(list_to_sort):

    if len(list_to_sort) > 1: # if our list size is above 1

        mid_point = None

        if len(list_to_sort) % 2 == 0:  # even amount of elements
            mid_point = int(len(list_to_sort) / 2)  # go to index of first half
        else:  # odd number of elements
            mid_point = int((len(list_to_sort) - 1) / 2)  # go to index of first half

        sorted_list_a = merge_sorting(list_to_sort[:mid_point])
        sorted_list_b = merge_sorting(list_to_sort[mid_point:])

        sorted_list = merger(sorted_list_a, sorted_list_b)

        return sorted_list

    else:

        return list_to_sort


def merge_sort(list_to_sort):

    start_time = time.clock()

    list_to_sort = merge_sorting(list_to_sort)

    end_time = time.clock()

    time_to_sort = end_time - start_time

    return list_to_sort, round(time_to_sort, 6)


def counting_sort(list_to_sort):

    start_time = time.clock()

    # Start by finding larges number in absolute value
    maximum = max(list_to_sort) # O(n)

    minimum = min(list_to_sort) # O(n)

    new_list = []

    counting_dict = {}

    for elem in list_to_sort:
        if elem not in counting_dict:
            counting_dict[elem] = 1
        else:
            counting_dict[elem] = counting_dict[elem] + 1

    for i in range(minimum, maximum+1):
        if i in counting_dict:
            for j in range(counting_dict[i]):
                new_list.append(i)


    end_time = time.clock()

    time_to_sort = end_time - start_time

    return new_list, round(time_to_sort, 6)



























