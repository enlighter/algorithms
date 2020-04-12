from timeit import default_timer as timer
from utils.bubblesort import bubble_sort
from utils.insertionsort import insertion_sort

test_list = [3, 6, 8, 24, 7, 11, 16]
start = timer()
for _ in range(10000):
    _ = bubble_sort(test_list)
end = timer()
bubble_sort_asc_time = (end - start)/10000
start = timer()
for _ in range(10000):
    _ = insertion_sort(test_list)
end = timer()
insertion_sort_asc_time = (end - start)/10000
print("Asc. sort avg. times, bubble sort: {}, insertion sort: {}".format(
    bubble_sort_asc_time, insertion_sort_asc_time))
start = timer()
for _ in range(10000):
    _ = bubble_sort(test_list, desc=True)
end = timer()
bubble_sort_desc_time = (end - start)/10000
start = timer()
for _ in range(10000):
    _ = insertion_sort(test_list, desc=True)
end = timer()
insertion_sort_desc_time = (end - start)/10000
print("Desc. sort avg. times, bubble sort: {}, insertion sort: {}".format(
    bubble_sort_desc_time, insertion_sort_desc_time))
