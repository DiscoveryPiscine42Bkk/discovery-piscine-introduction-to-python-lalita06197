#!/usr/bin/python3
import array
ori_array = [2,8, 9, 48, 8, 22, -12, 2]
new_array = []
for number in ori_array:
    if number + 2 > 5:
        new_array.append(number + 2)
print(ori_array)
print(new_array)