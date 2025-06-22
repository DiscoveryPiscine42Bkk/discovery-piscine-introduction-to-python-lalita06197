#!/usr/bin/python3
n1 = int(input("type a number: "))
n2 = int(input("type a number: "))
result = n1 * n2
print(f"{n1} X {n2} = {result}")
if result > 0:
    print("The result is positive")
if result < 0:
    print("The result is negative")
if result == 0:
    print("The result is positive and negative")