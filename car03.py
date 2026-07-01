class Car:
    """汽车基类"""

    def __init__(self, brand, model, color, price, owner):
        self.brand = brand
        self.model = model
        self.color = color
        self.price = price
        self.owner = owner

    def charge(self):
        """补充燃料方法（基类）"""
        print('正在补充燃料...')


class FuelCar(Car):
    """燃油车类"""

    def charge(self):
        """重写父类方法：加油"""
        print('燃油汽车正在加油...')


class ElectricCar(Car):
    """电动车类"""

    def charge(self):
        """重写父类方法：充电"""
        print('电动汽车正在充电...')


# 函数注解
def handle_charge(car: Car):
    """
    处理补充燃料的函数

    参数类型为父类 Car，支持传入任意子类实例
    这体现了多态的核心思想
    """
    car.charge()


# 测试代码
if __name__ == '__main__':
    # 同一调用语句，传入对象不同，触发不同行为
    handle_charge(FuelCar("BMW", "X5", "白色", 500000, "张三"))
    handle_charge(ElectricCar("BYD", "汉", "白色", 250000, "张三"))
