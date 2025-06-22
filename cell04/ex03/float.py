#!/usr/bin/python3
m1 = input("Give me a number: ")
num_f = float(m1)
x = num_f.is_integer()
if x == True:
    print("This number is an integer")
else:
    print("This number is a decimal")