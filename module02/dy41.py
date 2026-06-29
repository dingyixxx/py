from module01.dy35 import calc_data

print(calc_data(1,name="dy121"))

# 常量(不会发生变化的数据；常量的名称为全部大写)
PI = 3.1415926
NAME = "马☆海哥"

# 函数
def log_separator1():  # 1个用法
    print("-" * 30)  # "-"重复输出30次

def log_separator2():
    print("+" * 30)

def log_separator3():
    print("#" * 30)

def log_separator4():
    print("*" * 30)


# __name__d:python中内置变量,表示当前模块的名字(直接运行当前模块,__name__的值为"__main__",当该模块被导入时,名字就是这个
print(__name__)
if __name__=="__main__":
    # 测试函数
    log_separator1()  # 一旦导入模块,模块的代码就会执行
    PI = 2112
    print(PI)
    print("测试这个代码会不会执行呀///"*20)
