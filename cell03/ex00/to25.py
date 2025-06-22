#!/usr/bin/python3
print("Enter the number less than 25")
number = int(input("type a number: "))
x = 26
while number <= x:
    print ("Inside the loop, my variable is", number)
    number += 1
    if number == x:
        break
if number > x:
    print("Error")