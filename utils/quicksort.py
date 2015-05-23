'''
 	__author__: "Sushovan Mandal"
    __license__: "MIT license"
    __email__: "mandal.sushovan92@gmail.com"
    __site__: www.github.com/enlighter
'''

from random import randrange


class quicksort(object):
	'''
	This is a non-instantiable base class

	This quicksort class sorts the
	entire list 'to_sort', if you want
	to sort a part of the list then pass
	list[start:end+1] as the parameter
	list to be sorted
	'''
	def __init__(self, to_sort):
		if not type(to_sort) == list:
			raise ValueError("'to_sort' needs to be a 'list' type object")
		else:
			for n in to_sort:
				if not type(n) == int:
					raise ValueError("This class only sorts 'int' type objects")
		self.sorted = to_sort
		self.last_pos = len(self.sorted) - 1
		# Todo: in sub-class:-
		# if self.last_pos > 0:
		# 	self._process_(0, self.last_pos)

	def _process_(self, beg, end):
		pass

	def _partition_(self, beg, end):
		pivot = self.sorted[beg]
		# debug:
		# print("pivot = %d" %pivot)
		greater_than_pivot_start = beg + 1

		for read in range(beg+1, end+1):
			#debug:
			# print("reading %d"%read)
			if (self.sorted[read] <= pivot):
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
		self.sorted[beg], self.sorted[greater_than_pivot_start-1] = self.sorted[greater_than_pivot_start-1], self.sorted[beg]
		# debug:
		# print("after correcting pivot position: ",self.sorted)

		# greater_than_pivot-1 is the position of the pivot
		# element by now
		return greater_than_pivot_start-1

	def __repr__(self):
		return "quicksort.quicksort([])"

	def __str__(self):
		return "Class<quicksort>"

class randomized_quicksort(quicksort):
	# Todo: optimization for when there is repitition of elements
	def __init__(self, to_sort):
		quicksort.__init__(self,to_sort)
		self._process_(0, self.last_pos)

	def _process_(self, beg, end):
		if beg == end:
			# debug:
			# print("returning without any processing")
			pass
		else:
			pivot = randrange(beg,end+1)
			self.sorted[beg], self.sorted[pivot] = self.sorted[pivot],self.sorted[beg]
			pivot = self._partition_(beg,end)
			if pivot > beg:
				self._process_(beg, pivot-1)
			if pivot < end:
				self._process_(pivot+1, end)

	def __repr__(self):
		return "quicksort.randomized_quicksort([])"

	def __str__(self):
		return "Class<randomized_quicksort>"



if __name__ == "__main__":
	to_sort = [5,1,3,9,4,7,12,6,15,87,2,99,45,8,5]
	# print(randomized_quicksort)
	sort = randomized_quicksort(to_sort)
	print(sort.sorted)