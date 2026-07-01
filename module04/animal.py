# 多态-鸭子类型
# 鸭子类型（Duck Typing）是指如果它走路像鸭子，叫起来叫鸭子，那么它就是鸭子
# 在鸭子类型中，我们关注的是对象的行为（它有什么方法），而不是对象的类型（它是什么类）。
class Duck:
    """鸭子类"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def swimming(self):
        """游泳方法"""
        print(f'{self.age} 岁的 {self.name} 正在游泳...')


class Dog:
    """狗类"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def swimming(self):
        """游泳方法"""
        print(f'{self.age} 岁的 {self.name} 正在游泳...')


class Pig:
    """猪类"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def swimming(self):
        """游泳方法"""
        print(f'{self.age} 岁的 {self.name} 正在游泳...')


def go_swimming(duck: Duck): #类型注解，只是为了提高代码的可读性，并不具备任何约束力
    """
    去游泳函数

    参数类型标注为 Duck，但实际上可以传入任何具有 swimming() 方法的对象
    这体现了 Python 的鸭子类型特性
    """
    duck.swimming()


# 测试代码
if __name__ == '__main__':
    go_swimming(Dog(name="旺财", age=4))
    go_swimming(Duck(name="唐老鸭", age=2))
    go_swimming(Pig(name="佩奇", age=1))
