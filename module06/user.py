# from dataclasses import dataclass
#
# @dataclass
# class User:
#     id: int
#     name: str
#     age: int
#
#
# u1 = User(1, "Alice", 18)
# u2 = User(1, "Alice", 18)
#
# print(u1)           # User(id=1, name='Alice', age=18)  ← 自动生成的 __repr__
# print(u1 == u2)     # True                               ← 自动生成的 __eq__


from dataclasses import dataclass, field
from typing import List

@dataclass
class Library:
    name: str
    books: List[str] = field(default_factory=list)  # 可变默认值必须用 factory
    max_books: int = 100                             # 普通默认值直接写

lib = Library("市图书馆")
lib.books.append("Python编程")
print(lib)  # Library(name='市图书馆', books=['Python编程'], max_books=100)
