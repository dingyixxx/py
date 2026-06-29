# str="helloWorld"
# # print(str[-5::2])
# # print(str[-5:-1:2])
# print(str[-1:-5:-2])
#
# num=[e for e in range(1, 20)]
# print(num[-1: -8: -3]) #正向索引 负向索引 步长可以为正数也可以为负数

s="findYouyou_findYouyou_findYouyou_findYouyou_findYouyouf"
print(s.index("_"))
print(s.rfind("_findYouyou_f"))

print(s.find("_findYouyou_f"))
print(s.count("ou"))
print(s.upper())
print(s.lower())
print(s.split("_"))
print(s.strip("f"))
print(s.replace("Youyou", "123456789"))
print(s.startswith("fin"))
print(s)#原始字符串不可变