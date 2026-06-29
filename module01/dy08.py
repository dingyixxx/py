# while True:
#     year = int(input("请输入年份："))
#     print(f"您输入的年份是{year}")
#
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("整百-闰")
#         else:
#             print("整百-不闰...")
#     else:
#         if year % 4 == 0:
#             print("非整百-闰")
#         else:
#             print("非整百-不闰...") #else也要缩进

"""
多行注释
-
三引号
"""
"""
while True:
    num=int(input("请输入数字num："))
    if num>0:
        print("正数")
    elif num==0:
        print("0")
    else:
        print("负数")
    print("positive" if num>0 else "negative")
"""
#
# if 1==12:
#     pass
# else:
#     print("else")


a = int(input("请输入第一个边的边长："))
b = int(input("请输入第二个边的边长："))
c = int(input("请输入第三个边的边长："))

# 2. 判断三角形的类型 - pass 是一个空语句，起到一个语法占位的作用
if a + b > c and a + c > b and b + c > a: # 条件成立，构成三角形
    if a == b and b == c:
        print(f"{a} {b} {c} 这三个边长构成等边三角形 ~")
    elif a == b or b == c or a == c:
        print(f"{a} {b} {c} 这三个边长构成等腰三角形 ~")
    else:
        print(f"{a} {b} {c} 这三个边长构成普通三角形 ~")
else:
    print(f"{a} {b} {c} 这三个边长不能构成三角形 !!!")
