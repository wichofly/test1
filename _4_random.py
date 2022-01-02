from random import random

guess = input("Enter 'b' for bigger or 's' for small if you think the number is bigger/smaller: ")

# generate some random numbers
x = random()
x = round(x, 2)
print(x)
if guess != "b" or guess != "s":
    print("sorry, false type")
# print "You lost" or "You win"
if x > 0.5 and guess == "b": 
    print ("you won, the number is greater than 0.5")
if x < 0.5 and guess == "s":
    print ("you won, the number is smaller than 0.5")

if x < 0.5 and guess == "b": 
    print ("you lost, the number is smaller than 0.5")
if x > 0.5 and guess == "s":
    print ("you lost, the number is bigger than 0.5")

#
# if guess == "b":
#   print ("you won")