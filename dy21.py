# fruits = ["apple", "banana", "cherry"]
#
# # 解包
# fruit1, fruit2, fruit3 = fruits
# print(fruit2)  # 输出: banana

numbers = [1, 2, 3, 4, 5]
print(numbers.index(3))

# 将第一个值赋给 a，剩下的所有值打包成列表赋给 rest
a, *rest = numbers
print(a)    # 输出: 1
print(rest) # 输出: [2, 3, 4, 5]

# 也可以放在中间或前面
first, *middle, last = numbers
print(middle) # 输出: [2, 3, 4]