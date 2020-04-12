'''
 	__author__: "Sushovan Mandal"
    __license__: "MIT license"
    __email__: "mandal.sushovan92@gmail.com"
    __site__: www.github.com/enlighter
'''

from random import randrange


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


if __name__ == "__main__":
	test_list = [5, 1, 3, 9, 4, 7, 12, 6, 15, 87, 2, 99, 45, 8, 5]
	# print(randomized_quicksort)
	sort = RandomizedQuickSort(test_list)
	print(sort.sorted)
