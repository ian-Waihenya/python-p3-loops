#!/usr/bin/env python3

def happy_new_year():
   
    countdown = 10
    
    while countdown >= 1:
        print(countdown)
        countdown -= 1
    
    print("Happy New Year!")

happy_new_year()


def square_integers(nums):
    squared_nums = []
    for num in nums:
        squared_nums.append(num ** 2)
    return squared_nums

input_list = [1, 2, 3, 4, 5]
squared_list = square_integers(input_list)
print(squared_list)  

def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

fizzbuzz()
