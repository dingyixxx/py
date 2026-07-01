from ctypes import pythonapi


class Car:
    pass

# 最简单的面向对象，空结构
car=Car()
car.brand="BMW"
car.name="x5"
car.price=500000
print(car)
print(car.__dict__) #会将对象中的所有属性以字典的形式输出出来，目前学过__name__,__all__,__dict__
# 不推荐动态地为对象添加属性，类是模板（具有相同方法或者属性）
# 定义在类的外面，叫函数
# 定义在类的里面，叫方法

class Task:
    def __init__(self,name,frequency,type):
        self.name=name
        self.frequency=frequency
        self.type=type

task=Task("数据同步任务",12,"系统")
print(task.__dict__)

class Person:
    legsNo=2 #类属性，是所有实例对象共享的
    armsNo=2
    age=0
    age1=0
    def __init__(self,name,sex,age,province,idNo,hobbies=["打篮球","徒步"]):
        self.name=name
        self.sex=sex
        self.age=age
        self.province=province
        self.hobbies=hobbies
        self.__idNo=idNo
    def introducing(self):
        print(f"你好，我叫{self.name},我今年{self.age}岁了，我来自于{self.province},我是一个{self.sex}的")
    def like(self,otherHobbies):
        """
        声明了自己的爱好
        :param otherHobbies: 其他爱好
        :return:
        """
        print(f"我的爱好是{[*self.hobbies,*otherHobbies]}")
        return [*self.hobbies,*otherHobbies]

    def getRelations1(self, *args, **kwargs):
        return self.__getRelations(self, *args, **kwargs)
    def __getRelations(self,*args,**kwargs):
        print(f"{args}--{kwargs}")
        print(type(args))
        print(type(kwargs))
        return args,kwargs
    def __str__(self):
        return f"类似于java里的toString方法，打印出{self.name}-{self.sex}-{self.age}-{self.hobbies}-{self.province}-{self.age1}-{self.legsNo}-{self.armsNo}"
    def __eq__(self, other):
        return self.__idNo==other.__idNo
    def __lt__(self, other):
        return self.age<other.age

person=Person("王大锤","女",35,"辽宁","211103199106201528")
print(person.__dict__)
# 定义的时候，需要指定self，调用的时候不需要传入
person.introducing()
print(person.like(["其他爱好1", "其他爱好2"]))
# print(person.getRelations1("大姐", "二姐", "三姐", "五妹妹", father="老丁", mother="秀玲", baby="馋馋"))
print(person._Person__getRelations("大姐", "二姐", "三姐", "五妹妹", father="老丁", mother="秀玲", baby="馋馋"))
# __init__,__eq__,__str__,__lt__魔法方法（双下划线开头，双下划线结尾）
print(person)#打印的时候，会调用__str__魔法方法
person2=Person("lilian","男",34,"山东","211103199106201528")
print(person2 == person)
print(person2 < person)
Person.age1=999
print(person._Person__idNo)#用这种方式，也可以调用私有方法__
print(person2)
print(Person.age1)
# __lt__,__le__,__gt__,__ge__支持比较两个对象的大小less than,less than or equal,greater than,greater than or equal

# 实例属性（对象，self.后面的那些属性） 和 类属性（所有人都有两条腿和两条胳膊，不定义在self上，类似于java的static）
# 通过实例查找属性时，会先查找实例属性，实例属性不存在时，再查找类属性
# python语言，一定要注意缩进，不要不缩进，也不要缩进太多了


