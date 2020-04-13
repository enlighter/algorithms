from timeit import default_timer as timer
import random
from utils.insertionsort import insertion_sort
from utils.mergesort import merge_sort
from utils.quicksort import quick_sort

test_list = random.sample(range(10000), 1000)
start = timer()
for _ in range(10000):
    _ = insertion_sort(test_list)
end = timer()
insertion_sort_asc_time = (end - start)/10000
start = timer()
for _ in range(10000):
    merge_sort(test_list)
end = timer()
merge_sort_top_down_asc_time = (end - start)/10000
start = timer()
for _ in range(10000):
    merge_sort(test_list, 'bottom_up')
end = timer()
merge_sort_bottom_up_asc_time = (end - start)/10000
start = timer()
for _ in range(10000):
    quick_sort(test_list)
end = timer()
quick_sort_asc_time = (end - start)/10000
print("Asc. sort avg. times, insertion sort: {}, merge sort top down: {}, merge sort bottom up: {},"
      " quick sort: {}".format(insertion_sort_asc_time, merge_sort_top_down_asc_time,
                               merge_sort_bottom_up_asc_time, quick_sort_asc_time))
start = timer()
for _ in range(10000):
    _ = insertion_sort(test_list, True)
end = timer()
insertion_sort_desc_time = (end - start)/10000
start = timer()
for _ in range(10000):
    merge_sort(test_list, 'top_down', True)
end = timer()
merge_sort_top_down_desc_time = (end - start)/10000
start = timer()
for _ in range(10000):
    merge_sort(test_list, 'bottom_up', True)
end = timer()
merge_sort_bottom_up_desc_time = (end - start)/10000
start = timer()
for _ in range(10000):
    quick_sort(test_list, True)
end = timer()
quick_sort_desc_time = (end - start)/10000
print("Desc. sort avg. times, insertion sort: {}, merge sort top down: {}, merge sort bottom up: {},"
      " quick sort: {}".format(insertion_sort_desc_time, merge_sort_top_down_desc_time,
                               merge_sort_bottom_up_desc_time, quick_sort_desc_time))
