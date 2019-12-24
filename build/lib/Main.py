
import SortingAlgorithms as Sort
import random




def main():

    # configurations
    number_of_elements = 100
    minimum = 0
    maximum = 100

    unsorted_list = []
    time_to_sort = 0.0

    for i in range(number_of_elements):
        unsorted_list.append(random.randint(minimum, maximum))

    print("Number of elements:  ", number_of_elements)
    print("Minimum: ", minimum)
    print("Maximum: ", maximum)

    sorted_list, time_to_sort = Sort.insertion_sort(unsorted_list)
    print("Insertion Sort Needed: ", time_to_sort, " Seconds")

    sorted_list, time_to_sort = Sort.merge_sort(unsorted_list)
    print("Merge Sort Needed:     ", time_to_sort, " Seconds")

    sorted_list, time_to_sort = Sort.counting_sort(unsorted_list)
    print("Counting Sort Needed:  ", time_to_sort, " Seconds")


main()



