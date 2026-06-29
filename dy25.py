# 元组一旦定义完成，不可修改
# 元组可以重复，元组有序
# 定义元组
# t1=(5,3,4,12,99,886,5,5)
# for e in t1:
#     print(e)
#
# # t1[0]="e" #TypeError: 'tuple' object does not support item assignment
# #
# # t2=()
# # t3=tuple()#定义空元组 它剖
#
# print(t1.count(5))
# print(t1.index(5))
# print(type(t1))
# print(t1[0])
# print(t1[-1])
# print(t1[-1:-4:-2])
# print(t1[-1:-6:-2])
#
# t4=(1,2,3)
# print(t4[0:1:1])

x = (1)
print(x)        # 输出: 1
print(type(x))  # 输出: <class 'int'>  ← 是整数，不是元组！

y = (1,)
print(y)        # 输出: (1,)
print(type(y))  # 输出: <class 'tuple'>  ← 这才是元组

z=()
print(z)
print(type(z))

# 定义元组，组包
t1=5,7,9,1
print(t1)
print(type(t1))

a,*b,c=t1 #扩展解包，和列表是一样的
print(a)
print(b)
print(type(b)) #解包之后为list，而不是tuple
print(c)
