from dataclasses import field, dataclass
#
#
# @dataclass
# class User:
#     name: str
#     age: int = 0  # 普通默认值
#     email: str = field(default="no@email.com")  # 用 field 声明
#
#     # 两者效果一样，但 field() 可以和其他参数组合使用


@dataclass
class Product:
    name: str
    price: float
    discount_price: float = field(init=False)  # 不在 __init__ 中出现

    def __post_init__(self):
        """初始化后自动调用"""
        self.discount_price = self.price * 0.8


p = Product("手机", 5000)
print(p.discount_price)  # 4000.0 ← 自动计算
