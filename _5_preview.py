#### List
#########
# generate a list if fruits
# fruits = ["apple", "banana", "cherry"]

# print the first value
#print(fruits[0])

# print the last value
#print(fruits[-1])

# print the first two elements
#print(fruits[0:2])

# print the last two elements
#print(fruits[-2:])


#### For Loops
##########
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#   print(fruit)
# 
# for x in [1,2,3,4,5,6,7,8,9]:
#     print("The current value of x is:", x)
#     if x > 4:
#         print("x is bigger than 4")



#### Date
##########
from datetime import date
from datetime import datetime
import time

# today = date.today()
# print("Today's date:", today)

# now = datetime.now() 
# print("now =", now)
# for x in range(0, 10):
#     time.sleep(1)
#     now = datetime.now() 
#     print("now is", now)


#### Functions
##############

# def add_two_numers(a, b):
#     result = a + b
#     print(result)
# 
# add_two_numers(3, 3)
# add_two_numers(3, 6)
# add_two_numers(3, 12)
# add_two_numers(14, 3)


def print_current_time():
    today = date.today()
    print("Today's date:", today)

print_current_time()

from random import random

for x in range(0, 9):
    x = random()
    x = round(x, 2)
    print(x)

# hello test commit