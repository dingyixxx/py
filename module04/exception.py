"""
Python 常见异常类型演示
========================
本文件展示了5种常见的Python异常及其出现场景
"""


# ==================== 1. NameError (名称错误) ====================
print("=" * 50)
print("1. NameError 演示")
print("=" * 50)

try:
    # res = 1/0   # TypeError: can only concatenate str to str
   print("abc".aa)
except TypeError as e:
    print(f"捕获到TypeError: {e}")
except ZeroDivisionError as e:
    print(f"捕获到ZeroDivisionError: {e}")
except AttributeError as e:
    print(f"捕获到AttributeError: {e}")
except Exception as e:
    print(f"捕获到Exception: {e}")

try:
    result = "年龄："   # TypeError: can only concatenate str to str
except TypeError as e:
    print(f"捕获到TypeError: {e}")
finally:
    print("finally...11")

# 场景1：变量未定义就使用
try:
    print(undefined_variable)  # NameError: name 'undefined_variable' is not defined
except NameError as e: #如果想输出错误信息，就用as关键字
    print(f"捕获到NameError: {e}")

# 场景2：函数名拼写错误
def say_hello():
    """打招呼函数"""
    print("Hello!")

try:
    say_helo()  # NameError: name 'say_helo' is not defined (拼写错误)
except NameError as e:
    print(f"捕获到NameError: {e}")

# 场景3：访问不存在的局部变量
def test_scope():
    try:
        print(local_var)  # NameError: local_var 未定义
    except NameError as e:
        print(f"捕获到NameError: {e}")

test_scope()


# ==================== 2. TypeError (类型错误) ====================
print("\n" + "=" * 50)
print("2. TypeError 演示")
print("=" * 50)

# 场景1：不同类型相加
try:
    result = "年龄：" + 25  # TypeError: can only concatenate str to str
except TypeError as e:
    print(f"捕获到TypeError: {e}")
finally:
    print("finally...")

# 场景2：调用不可调用的对象（如刚才的模块问题）
my_list = [1, 2, 3]
try:
    my_list()  # TypeError: 'list' object is not callable
except TypeError as e:
    print(f"捕获到TypeError: {e}")

# 场景3：函数参数数量不匹配
def greet(name):
    """问候函数"""
    print(f"Hello, {name}")

try:
    greet()  # TypeError: missing 1 required positional argument
except TypeError as e:
    print(f"捕获到TypeError: {e}")

# 场景4：对非可迭代对象进行迭代
try:
    for i in 123:  # TypeError: 'int' object is not iterable
        print(i)
except TypeError as e:
    print(f"捕获到TypeError: {e}")


# ==================== 3. IndexError (索引错误) ====================
print("\n" + "=" * 50)
print("3. IndexError 演示")
print("=" * 50)

# 场景1：索引超出范围
my_list = [10, 20, 30]
try:
    print(my_list[3])  # IndexError: list index out of range (有效索引是0,1,2)
except IndexError as e:
    print(f"捕获到IndexError: {e}")

# 场景2：访问空列表
empty_list = []
try:
    print(empty_list[0])  # IndexError: list index out of range
except IndexError as e:
    print(f"捕获到IndexError: {e}")

# 场景3：负数索引超出范围
try:
    print(my_list[-4])  # IndexError: list index out of range (有效负索引是-1,-2,-3)
except IndexError as e:
    print(f"捕获到IndexError: {e}")


# ==================== 4. KeyError (键错误) ====================
print("\n" + "=" * 50)
print("4. KeyError 演示")
print("=" * 50)

# 场景1：访问字典中不存在的键
my_dict = {"name": "张三", "age": 25}
try:
    print(my_dict["address"])  # KeyError: 'address'
except KeyError as e:
    print(f"捕获到KeyError: {e}")

# 场景2：键名拼写错误
try:
    print(my_dict["naem"])  # KeyError: 'naem' (应该是"name")
except KeyError as e:
    print(f"捕获到KeyError: {e}")

# 场景3：访问空字典
empty_dict = {}
try:
    print(empty_dict["key"])  # KeyError: 'key'
except KeyError as e:
    print(f"捕获到KeyError: {e}")


# ==================== 5. ValueError (值错误) ====================
print("\n" + "=" * 50)
print("5. ValueError 演示")
print("=" * 50)

# 场景1：字符串转整数失败
try:
    number = int("abc")  # ValueError: invalid literal for int()
except ValueError as e:
    print(f"捕获到ValueError: {e}")

# 场景2：删除列表中不存在的元素
my_list = [1, 2, 3]
try:
    my_list.remove(5)  # ValueError: list.remove(x): x not in list
except ValueError as e:
    print(f"捕获到ValueError: {e}")

# 场景3：数学运算中的无效值
import math
try:
    result = math.sqrt(-1)  # ValueError: math domain error
except ValueError as e:
    print(f"捕获到ValueError: {e}")

# 场景4：解包时元素数量不匹配
try:
    a, b, c = [1, 2]  # ValueError: not enough values to unpack
except ValueError as e:
    print(f"捕获到ValueError: {e}")


# ==================== 异常对比总结 ====================
print("\n" + "=" * 50)
print("异常类型对比总结")
print("=" * 50)
summary = """
| 异常类型      | 核心原因           | 一句话记忆                    |
|--------------|-------------------|------------------------------|
| NameError    | 名字没定义         | "你是谁？我不认识这个变量/函数"   |
| TypeError    | 类型不对           | "这个操作不适合这种数据类型"       |
| IndexError   | 索引越界           | "这个位置不存在"                |
| KeyError     | 键不存在           | "字典里没有这个键"              |
| ValueError   | 值不合适           | "类型对了，但值不对"            |
"""
print(summary)

print("\n所有异常演示完成！")
