"""
函数调用链演示
=============
本文件展示了函数之间的嵌套调用关系
"""


def fun1():
    """
    第一个函数
    功能：打印信息并调用fun2()
    """
    print("fun1 ... running ...")
    fun2()  # 调用fun2函数


def fun2():
    """
    第二个函数
    功能：打印信息并调用fun3()
    """
    print("fun2 ... running ...")
    fun3()  # 调用fun3函数


def fun3():
    """
    第三个函数
    功能：打印信息并访问全局变量my_color

    注意：这里会触发NameError，因为my_color未定义
    """
    print("fun3 ... running ...")
    print(my_color)  # NameError: name 'my_color' is not defined


# 程序入口
if __name__ == '__main__':
    """
    主程序入口
    执行流程：fun1() -> fun2() -> fun3() -> 报错(NameError)
    """
    try:
     fun1()
     if 1>1:
         print("1>1")
    except Exception as a:
        print(a)
