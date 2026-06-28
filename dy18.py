# 数据容器
# 列表list 元素有序 可以重复 可以修改 反向索引
# 字符串str
# 元组tuple
# 集合set
# 字典dict

subS=[1,True,"HHH"]
s=[54,15,75,108,23,78,75,None,True,"Hello",3.1415926,subS]
print(type(s))
# for i, e in enumerate(s):
#     print(f"s[i-12]-{s[i-12]}-type-{type(s[i-12])}")
#
# s.remove(75) 删除第一个值为xx的元素
# s.remove("Hello")

# del subS[0]
# del  s[1]
#
# for e in s:
#     print(e,end=" ")


# sub2=s[-11::3]
#
# for e in sub2:
#     print(e)

# s.append("最后一个元素")
# s.insert(1,"下标1之前insert")
# s.reverse()
a=s.pop(4)
print(a)
# s.sort() '<' not supported between instances of 'NoneType' and 'int'
# for e in s:
#     print(e)

# sub3=s[-11:4:2]
# for e in sub3:
#     print(e)

# for i, e in enumerate(s):
#     print(f"s[i-11]-{s[i-11]}-type-{type(s[i-11])}")

#
# sSort=[2,5.12,333,"a","Hello",True]
# for e in sSort:
#     print(e)