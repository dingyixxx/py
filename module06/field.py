from dataclasses import dataclass, field
from typing import List


# ❌ 错误写法：可变对象作为默认值会导致所有实例共享同一个 list
# @dataclass
# class BadLibrary:
#     books: List[str] = []  # 危险！所有实例共用一个列表
#
# lib1 = BadLibrary()
# lib2 = BadLibrary()
# lib1.books.append("Python")
# print(lib2.books)  # ['Python'] ← 被污染了！

# ✅ 正确写法：用 default_factory 每次创建新对象
@dataclass
class GoodLibrary:
    books: List[str] = field(default_factory=list)

lib1 = GoodLibrary()
lib2 = GoodLibrary()
lib1.books.append("Python")
print(lib2.books)  # [] ← 独立干净
