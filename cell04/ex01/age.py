#!/usr/bin/python3
m1 = input("Please tell me your age: ")
age = int(m1)
print(f"you are currently {m1} years old")
age += 10
i = 1
while i <= 3:
    print(f"In {i * 10} years, you'll be {age} years old")
    age += 10
    i += 1