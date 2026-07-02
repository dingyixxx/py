import time
import functools

# 定义一个“切面”：日志和性能监控
# 装饰器，高阶函数
def log_and_time(func):
    print("我在定义函数了...")
    @functools.wraps(func)  # 保留原函数的元信息（如函数名、文档字符串）
    def wrapper(*args, **kwargs):
        # 【前置通知 Before】
        print(f"[LOG] 正在执行函数: {func.__name__}")
        start_time = time.time()

        # 执行原始函数（目标对象）
        result = func(*args, **kwargs)

        # 【后置通知 After】
        end_time = time.time()
        print(f"[LOG] 函数 {func.__name__} 执行完毕，耗时: {end_time - start_time:.4f}秒")

        return result

    print(wrapper.__dict__)
    return wrapper

# --- 业务逻辑 ---

@log_and_time  # 使用装饰器，相当于 apply_aspect(business_logic)
def business_logic(n):
    """一个模拟的耗时业务操作"""
    time.sleep(0.5)
    return sum(i for i in range(n))

# --- 调用 ---
if __name__ == "__main__":
    pass
    # result = business_logic(1000000)
    # print(f"计算结果: {result}")
    # [LOG]
    # 正在执行函数: business_logic
    # [LOG]
    # 函数
    # business_logic
    # 执行完毕，耗时: 0.5200
    # 秒
    # 计算结果: 499999500000