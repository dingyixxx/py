print("1. 正在定义装饰器...")

def my_decorator(func):
    print(f"3. [装饰器内部] 正在包装函数: {func.__name__}")
    def wrapper(*args, **kwargs):
        print(f"5. [运行时] 正在执行 {func.__name__} 的前置逻辑")
        return func(*args, **kwargs)
    return wrapper

print("2. 正在定义被装饰的函数...")

@my_decorator
def say_hello():
    print("6. [运行时] Hello, World!")

print("4. 函数定义完毕，准备调用函数...")
# say_hello() 即使不调用函数，在函数定义阶段，就已经被织入了