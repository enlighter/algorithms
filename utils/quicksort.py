'''
 	__author__: "Sushovan Mandal"
    __license__: "MIT license"
    __email__: "mandal.sushovan92@gmail.com"
    __site__: www.github.com/enlighter
'''

from random import randrange
import time


class QuickSort:
	'''
	This is a non-instantiable base class

	This quicksort class sorts the
	entire list 'to_sort', if you want
	to sort a part of the list then pass
	list[start:end+1] as the parameter
	list to be sorted
	'''
	def __init__(self, to_sort):
		self.sorted = to_sort
		self.last_pos = len(self.sorted) - 1

	def _process(self, lo, hi):
		pass

	def _partition(self, lo, hi):
		pivot = self.sorted[lo]
		# debug:
		# print("pivot = %d" %pivot)
		greater_than_pivot_start = lo + 1

		for read in range(lo + 1, hi + 1):
			# debug:
			# print("reading %d"%read)
			if self.sorted[read] <= pivot:
				# debug:
				# print("%d < %d" %(self.sorted[read], pivot))

				if read != greater_than_pivot_start:
					# this condition is imposed to avoid redundant swaps
					self.sorted[greater_than_pivot_start], self.sorted[read] = self.sorted[read], self.sorted[greater_than_pivot_start]
					# debug:
					# print(self.sorted)
				greater_than_pivot_start += 1

		# debug:
		# print("after processing: ",self.sorted)
		self.sorted[lo], self.sorted[greater_than_pivot_start - 1] = self.sorted[greater_than_pivot_start - 1], self.sorted[lo]
		# debug:
		# print("after correcting pivot position: ",self.sorted)

		# greater_than_pivot-1 is the position of the pivot
		# element by now
		return greater_than_pivot_start-1

	def __repr__(self):
		return "Class<QuickSort>"

	def __str__(self):
		return self.__repr__()


class RandomizedQuickSort(QuickSort):
	# Todo: optimization for when there is repitition of elements
	def __init__(self, to_sort):
		QuickSort.__init__(self, to_sort)
		if self.last_pos >= 1:
			self._process(0, self.last_pos)

	def _process(self, lo, hi):
		if lo == hi:
			# debug:
			# print("returning without any processing")
			pass
		else:
			pivot = randrange(lo, hi + 1)
			self.sorted[lo], self.sorted[pivot] = self.sorted[pivot], self.sorted[lo]
			pivot = self._partition(lo, hi)
			if pivot > lo:
				self._process(lo, pivot - 1)
			if pivot < hi:
				self._process(pivot + 1, hi)

	def __repr__(self):
		return "Class<RandomizedQuickSort>"

	def __str__(self):
		return self.__repr__()


def quick_sort(array, lo, hi):
	# print('array[{}:{}]'.format(lo, hi))
	if lo < hi:
		p = partition(array, lo, hi)
		# print('partition at', p)
		quick_sort(array, lo, p)
		quick_sort(array, p + 1, hi)


def partition(array, lo, hi):
	# print(array[lo:hi+1])
	mid = (lo + hi) // 2
	# pivot = array[mid]
	# Optimization: choose the median of lo, mid and hi as pivot
	if array[mid] < array[lo]:
		array[lo], array[mid] = array[mid], array[lo]
	if array[hi] < array[lo]:
		array[lo], array[hi] = array[hi], array[lo]
	if array[mid] < array[hi]:
		array[mid], array[hi] = array[hi], array[mid]
	pivot = array[hi]
	# print('pivot:', pivot)

	i, j = lo - 1, hi + 1
	while True:
		while True:
			i += 1
			# print('i:', i)
			if array[i] >= pivot:
				break
		while True:
			j -= 1
			# print('j:', j)
			if array[j] <= pivot:
				break
		if i >= j:
			return j
		# print('swapping', i, j)
		array[i], array[j] = array[j], array[i]
		# print(array[lo:hi+1])


if __name__ == "__main__":
	# test_list = [5, 1, 3, 9, 4, 7, 12, 6, 15, 87, 2, 99, 45, 8, 5]
	test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 15, 45, 87, 99]
	# print(randomized_quicksort)
	# sort = RandomizedQuickSort(test_list)
	# print(sort.sorted)
	quick_sort(test_list, 0, len(test_list) - 1)
	print(test_list)
