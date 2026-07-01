from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        return "Some sound"  # 默认实现

class Dog(Animal):
    def speak(self):
        # 可以选择调用父类的默认实现
        return super().speak() + " Woof!"

class Cat(Animal):
    def speak(self):
        # 也可以完全重写
        return "Meow!"

#  这仍然会报错，因为 speak 是抽象方法
try:
    animal = Animal()
except TypeError as e:
    print(e)
    # 输出: Can't instantiate abstract class Animal with abstract methods speak

# ✅ 可以实例化
dog = Dog()
print(dog.speak())  # 输出: Some sound Woof!

cat = Cat()
print(cat.speak())  # 输出: Meow!
