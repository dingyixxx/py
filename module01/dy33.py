# sub="aeiouAEIOU"
#
# def count_aeiou(str111):
#     num=0
#     for letter in str111:
#         if letter in sub:
#             num+=1
#
#     return  num
#
#
# print(count_aeiou("akjsdsiuAEds"))




# # 全局变量 ：在函数外部 或 函数的内部都是可以访问的 ;
# num = 100
#
#
# # 定义函数
# def circle_area(r):  # 1个形参
#     # 局部变量：只能在函数内部使用
#     pi = 3.14
#     area = pi * r * r
#
#     # global num
#     num = 10000
#     print("num = ", num)  # 10000
#
#     return area
#
#
# # 调用函数
# c_area = circle_area(10)
# print(c_area)
#
# print("num = ", num)  # 100


# 调试开关
debug_mode = False

def enable_debug_mode():
    global debug_mode
    debug_mode = True
    print("调试模式已开启")

def disable_debug_mode():
    global debug_mode
    debug_mode = False
    print("调试模式已关闭")

