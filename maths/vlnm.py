''' Very Large Number Multiplicator
	based on "Vedic Mathematics"

	__author__: Suhovan Mandal
	__license__: "MIT license"
	__email__: mandal.sushovan92@gmail.com
	__site__: www.github.com/enlighter
'''

import sys

### Pre-processing python version check ###
req_version = (3,4)
cur_version = sys.version_info

if cur_version < req_version:
	print("Your Python interpreter is too old. Please consider upgrading.")
	exit()
############################################

from time import process_time

def _listize_number_(num):
	'''
	converts an integer into a list
	containing the digits of the integer
	in reverse order
	'''
	return_list = []
	while not num == 0:
		return_list.append(num%10)
		num = int(num/10)
	return return_list

def multiply(num1=0, num2=0):
	if (not isinstance(num1, int)) or (not isinstance(num2,int)):
		raise ValueError("this function only works on integers")

	start_time = process_time()
	operand1 = str(num1)
	operand2 = str(num2)
	len1 = len(operand1)
	len2 = len(operand2)
	#debug
	print("%s of length %d" %(operand1,len1))
	print("%s of length %d" %(operand2,len2))

	num1_list = _listize_number_(num1)
	num2_list = _listize_number_(num2)
	print(num1_list)
	print(num2_list)

	if len1 <= len2:
		# operand1 is the shorter string
		result,left_over = _common_iteration_multiplication(operand1, operand2)
	else:
		# operand2 is the shorter string
		result,left_over = _common_iteration_multiplication(operand2, operand1)

	for c in operand1[::-1]:
		print(c)

	elapsed_time = process_time() - start_time
	print("elapsed time = %f",elapsed_time)

def _common_iteration_multiplication(operand1, operand2):
	pass
	return 0,0

multiply(123, 4567)