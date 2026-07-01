# 在python中,一个子类可以继承多个父类，多继承
# MRO 方法解析顺序 __mro__
# 华为智驾
from car01 import Car


class HuaweiAiDriving:
    """华为AI智能驾驶"""

    def __init__(self, version="V1.0"):
        self.version = version

    def run(self):
        print(f'使用华为AI智能驾驶系统{self.version}正在行驶...')



# 问界汽车
# class WenJieCar( HuaweiAiDriving,Car):
#     pass# 问界汽车
class WenJieCar(Car, HuaweiAiDriving):
    pass

    def __init__(self, brand, model, color, owner,  version="V2.2"):
        Car.__init__(self,brand, model, color, owner)
        HuaweiAiDriving.__init__(self,version)
    def run(self):
        Car.run(self)
        HuaweiAiDriving.run(self)
        print("wenjie car is running...")



# MRO: Method Resolution Order (方法解析顺序)
if __name__ == '__main__':
    c = WenJieCar(brand="BMW", model="X5", color="黑色", owner="张三")
    print(c.__dict__)
    print(WenJieCar.__mro__)#优先级,从高到底 (<class '__main__.WenJieCar'>, <class 'car01.Car'>, <class '__main__.HuaweiAiDriving'>, <class 'object'>)
    print(WenJieCar.mro())
    c.start()
    c.run()
