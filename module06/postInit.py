from dataclasses import dataclass, field


@dataclass
class Rectangle:
    width: float
    height: float
    area: float = field(init=False)

    def __post_init__(self):
        """在 __init__ 执行完后自动调用"""
        if self.width <= 0 or self.height <= 0:
            raise ValueError("宽高必须大于0")
        self.area = self.width * self.height

#
# rect = Rectangle(10, 5)
# print(rect.area)  # 50.0

rect2 = Rectangle(-1, 5)  # ❌ ValueError: 宽高必须大于0
print(rect2.area)  # 50.0
