'''
 	__author__: "Sushovan Mandal"
    __license__: "MIT license"
    __email__: "mandal.sushovan92@gmail.com"
'''

from random import randrange
from random import SystemRandom

def _digit_average(num,no_of_digits):
    average = 0
    for i in range(0,no_of_digits):
        digit = num%10
        num = num/10
        average = average + digit
    average = average/no_of_digits
    return average

def randrange_test():
    print("pseudo_random:")
    for i in range(0,10):
        num = randrange(1,11)
        print(num)

def sys_random_test():
    print("sys random:")
    no_of_digits = 3
    for i in range(0,10):
        sys_random = SystemRandom()
        num = sys_random.random()
        multiplicant = 10**no_of_digits
        num = int(num*multiplicant)
        print(_digit_average(num,no_of_digits))

randrange_test()
sys_random_test()