"""
www
"""



aa=1
"""
www
"""
# 定义变量
# a: int = 695
# score: float = 98.5
# hobby: str = "Python"
# flag: bool = True
# pic: None = None
#
# names: list[str] = ["A", "C", "E"]
# phones: set[str] = {"13309091111", "15209109121"}
# options: dict[str, int] = {"count": 0, "total": 0}
# goods: tuple[str, int, int] = ("手机", 5999, 1)

# 变量定义 - 未指定类型注解
# 类型注解
a = 596
score = 98.5
hobby = "Python"
flag = True
pic = None

names = ["A", "C", "E"]
phones = {"13309091111", "15209101902", "18809019201",3.14}
options = {"count": 2, "total": 10}
goods = ("手机", 6999, 1)
phones.add(True)#即使没有写类型注解，也会自动推断出类型的
phones.add(4)

# python是动态类型语言，添加的类型注解只是提示，并不是强制约束


# 变量定义 - 指定类型注解
a2: int = 596
score2: float = 98.5
hobby2: str = "Python"
flag2: bool = True
pic2: None = None

names2: list[str|int] = ["A", "C", "E"]
phones2: set[str] = {"13309091111", "15209101902", "18809019201"}
options2: dict[str, int] = {"count": 2, "total": 10}
goods2: tuple[str, int, int] = ("手机", 6999, 1)

names2.append("33")
names2.append(3.14)