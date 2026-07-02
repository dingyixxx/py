def transactional(func):
    """模拟一个事务装饰器"""
    def wrapper(*args, **kwargs):
        print(f"  [事务] 开启事务... (方法: {func.__name__})")
        try:
            result = func(*args, **kwargs)
            print(f"  [事务] 提交事务。")
            return result
        except Exception as e:
            print(f"  [事务] 发生异常，回滚事务！错误: {e}")
            raise
    return wrapper

class TransactionMeta(type):
    """元类：自动为类中所有方法添加 @transactional 装饰器"""
    def __new__(cls, name, bases, attrs): #饿汉
        for attr_name, attr_value in attrs.items():
            # 过滤掉特殊方法和私有方法
            if callable(attr_value) and not attr_name.startswith("_"):
                print(f"元类正在为方法 '{attr_name}' 织入事务切面...")
                attrs[attr_name] = transactional(attr_value)
        return super().__new__(cls, name, bases, attrs)

class OrderService(metaclass=TransactionMeta):
    def create_order(self, order_id):
        print(f"    正在创建订单: {order_id}")
        # 模拟一个异常
        # raise ValueError("库存不足")

    def pay_order(self, order_id):
        print(f"    正在支付订单: {order_id}")

# --- 调用 ---
if __name__ == "__main__":
    service = OrderService()
    service.create_order("ORD-001")
    print("-" * 20)
    service.pay_order("ORD-001")