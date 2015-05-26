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

def multiply(num1=0, num2=0):
	operand1 = str(num1)
	operand2 = str(num2)
	len1 = len(operand1)
	len2 = len(operand2)
	#debug
	print("%s of length %d" %(operand1,len1))
	print("%s of length %d" %(operand2,len2))

	if len1 <= len2:
		# operand1 is the shorter string
		result,left_over = _common_iteration_multiplication(operand1, operand2)
	else:
		# operand2 is the shorter string
		result,left_over = _common_iteration_multiplication(operand2, operand1)

	for c in operand1[::-1]:
		print(c)

def _common_iteration_multiplication(operand1, operand2):
	pass

multiply(123, 4567)