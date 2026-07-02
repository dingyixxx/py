from dataclasses import dataclass, field


@dataclass
class Animal:
    name: str
    legs: int = 4

@dataclass
class Dog(Animal):
    legs: int = field(default=4, init=False)  # 先声明有默认值的
    breed: str  =""


dog = Dog("旺财", "金毛")
print(dog)  # Dog(name='旺财', legs=4, breed='金毛')
