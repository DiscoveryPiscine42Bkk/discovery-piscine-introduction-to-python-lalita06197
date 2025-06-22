#!/usr/bin/python3
print("Enter a number")
number = int(input())
for mul in range(0,13):
    print("{0} * {1} = {2}". format(number, mul, (number * mul)))
