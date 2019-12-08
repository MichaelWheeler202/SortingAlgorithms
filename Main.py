
import SortingAlgorithms as Sort
import random


my_list = []
time_to_sort = 0.0

for i in range(10):
    my_list.append(random.randint(-50, 50))

print(my_list)

my_list, time_to_sort = Sort.counting_sort(my_list)

print(time_to_sort)
print(my_list)



