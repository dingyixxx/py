def my_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def say_hello():
    pass

# 查看函数的名字和内存地址
print(f"函数名: {say_hello.__name__}")
print(f"函数对象: {say_hello}")

# 虽然你定义的是 say_hello，但在加载阶段被装饰器处理后，它现在在内存中实际上已经是 wrapper 函数了。这就是“在定义阶段就把原函数替换了”的铁证。