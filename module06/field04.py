from dataclasses import dataclass, field


@dataclass(order=True)  # 启用排序
class Student:
    score: int
    # name: str = field
    name: str = field(compare=False)  # 排序时只看分数，不看名字

s1 = Student(90, "Alice")
s2 = Student(90, "Bob")
print(s1 == s2)  # True  ← 分数相同就认为相等
print(s1 < s2)   # False ← 不会因为名字字母顺序影响排序

