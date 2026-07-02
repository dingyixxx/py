class Animal:
    def __new__(cls):
        print(f"1. Animal.__new__ 被调用, cls={cls}")
        instance = super().__new__(cls)
        print(f"2. object.__new__ 返回了 {type(instance)} 实例")
        return instance

    def __init__(self):
        self.species = "动物"
        print(f"3. Animal.__init__ 被调用, self={self}")


class Dog(Animal):
    def __new__(cls):
        print(f"A. Dog.__new__ 被调用, cls={cls}")
        instance = super().__new__(cls)
        print(f"B. super().__new__ 返回了 {type(instance)} 实例")
        return instance

    def __init__(self):
        self.breed = "狗"
        print(f"C. Dog.__init__ 被调用, self={self}")


print("=== 开始创建 Dog 实例 ===\n")
dog = Dog()
print(f"\n最终对象: {dog.__dict__}, 类型: {type(dog)}")

# 输出：
# === 开始创建 Dog 实例 ===
#
# A. Dog.__new__ 被调用, cls=<class '__main__.Dog'>
# 1. Animal.__new__ 被调用, cls=<class '__main__.Dog'>
# 2. object.__new__ 返回了 <class '__main__.Dog'> 实例
# B. super().__new__ 返回了 <class '__main__.Dog'> 实例
# C. Dog.__init__ 被调用, self=<__main__.Dog object at 0x...>
#
# 最终对象: <__main__.Dog object at 0x...>, 类型: <class '__main__.Dog'>

#
# Python 查找 __init__ 时，从对象的实际类型（Dog）开始向上查找
# 找到 Dog.__init__ 后就停止查找，不会继续调用父类的 __init__
# 这与 __new__ 不同，__new__ 需要我们手动调用 super().__new__() 才会触发父类
