class MethodInterceptor:
    """一个描述符，用于拦截方法调用"""

    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        print(f"instance.__dict__是：{instance.__dict__}")
        print(f"owner.__dict__是：{owner.__dict__}")
        # 返回一个绑定的方法，这个方法包装了原始逻辑
        def wrapper(*args, **kwargs):
            # 【环绕通知 Around】
            print(f"[拦截器] 正在调用方法: {self.func.__name__}")
            print(f"[拦截器] 传入参数: {args[1:]}")  # args[0] 是 self
            result = self.func(instance, *args, **kwargs)
            print(f"[拦截器] 方法返回: {result}")
            return result
        return wrapper


class UserService:
    @MethodInterceptor
    def get_user(self, user_id):
        # 模拟数据库查询
        return f"User-{user_id}"



# AOP 的两种实现方式（装饰器 vs 描述符），它们的核心区别在于“拦截的维度”和“触发的时机”。
# 为了让你更清晰地理解，我们从以下三个核心维度进行梳理：
# 1. 拦截的维度：动作 vs 属性
# 装饰器（Decorators）：主要拦截的是“动作（行为）”。它关注的是函数或方法被调用的那个瞬间。它像是一个包装纸，把整个函数的执行过程（执行前、执行中、执行后）包起来。
# 描述符（Descriptors）：主要拦截的是“属性（数据）”。它关注的是类属性被访问（读/写/删）的那个瞬间。它像是一个智能保险箱，你每次打开箱子拿东西或放东西时，它都会介入。
# 2. 触发的时机：定义时 vs 运行时
# 装饰器：在代码加载（定义）阶段就生效了。当你写下 @log_and_time 时，Python 解释器会立刻执行这个装饰器函数，把原函数替换成包装后的新函数。
# 描述符：在代码运行（访问）阶段才生效。只有当你真正去执行 obj.method() 或 obj.attr 时，描述符协议中的 __get__ 等方法才会被触发。
# 3. 在 AOP 中的典型应用场景
# 装饰器：适合做全局性的逻辑织入。比如：记录整个函数的执行时间、验证用户权限、捕获整个方法的异常、缓存函数的返回值等。
# 描述符：适合做细粒度的参数/状态控制。比如：在方法被调用前，自动校验传入的参数类型；或者在读取属性时，动态计算并返回结果（懒加载）。

# --- 调用 ---
if __name__ == "__main__":
    pass
    # service = UserService()
    # print(service.get_user)
    # user = service.get_user(101)
    # print(f"获取到: {user}")