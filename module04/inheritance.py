# encapsulate,cohesion,decouple,inheritance,polymorphism

"""
类的继承演示 - 汽车类体系
========================
本文件展示了Python中类的定义、继承关系
包含：父类Car和两个子类FuelCar、ElectricCar
"""


# ==================== 父类：Car ====================
class Car:
    """
    汽车基类（父类）

    属性：
        color (str): 颜色
        brand (str): 品牌
        model (str): 型号

    方法：
        start(): 启动汽车
        stop(): 停止汽车
        run(): 行驶汽车
    """

    def __init__(self, c_color, c_brand, c_model):
        """
        初始化方法（构造函数）

        参数：
            c_color (str): 汽车颜色
            c_brand (str): 汽车品牌
            c_model (str): 汽车型号
        """
        self.color = c_color  # 实例属性：颜色
        self.brand = c_brand  # 实例属性：品牌
        self.model = c_model  # 实例属性：型号

    def start(self):
        """
        启动汽车

        输出格式：品牌 型号 正在启动...
        """
        print(f'{self.brand} {self.model} 正在启动...')

    def stop(self):
        """
        停止汽车

        输出格式：品牌 型号 停止行驶...
        """
        print(f'{self.brand} {self.model} 停止行驶...')

    def run(self):
        """
        行驶汽车

        输出格式：品牌 型号 正在行驶...
        """
        print(f'{self.brand} {self.model} 正在行驶...')


# ==================== 子类1：FuelCar（燃油车）====================
class FuelCar(Car):
    """
    燃油车类（继承自Car）

    特点：
        - 继承父类Car的所有属性和方法
        - 可以添加燃油车特有的属性和方法
        - 目前使用pass占位，表示暂时不添加新功能
    """
    pass


# ==================== 子类2：ElectricCar（电动车）====================
class ElectricCar(Car):
    """
    电动车类（继承自Car）

    特点：
        - 继承父类Car的所有属性和方法
        - 可以添加电动车特有的属性和方法（如电池容量、充电方法等）
        - 目前使用pass占位，表示暂时不添加新功能
    """
    pass


# ==================== 测试代码 ====================
if __name__ == '__main__':
    """
    程序入口
    演示各类的实例化和方法调用
    """

    print("=" * 50)
    print("1. 创建父类Car实例")
    print("=" * 50)
    car = Car("红色", "丰田", "卡罗拉")
    print(f"颜色：{car.color}")
    print(f"品牌：{car.brand}")
    print(f"型号：{car.model}")
    car.start()
    car.run()
    car.stop()

    print("\n" + "=" * 50)
    print("2. 创建子类FuelCar实例（继承自Car）")
    print("=" * 50)
    fuel_car = FuelCar("蓝色", "大众", "帕萨特")
    print(f"颜色：{fuel_car.color}")
    print(f"品牌：{fuel_car.brand}")
    print(f"型号：{fuel_car.model}")
    fuel_car.start()
    fuel_car.run()
    fuel_car.stop()

    print("\n" + "=" * 50)
    print("3. 创建子类ElectricCar实例（继承自Car）")
    print("=" * 50)
    electric_car = ElectricCar("白色", "特斯拉", "Model 3")
    print(f"颜色：{electric_car.color}")
    print(f"品牌：{electric_car.brand}")
    print(f"型号：{electric_car.model}")
    electric_car.start()
    electric_car.run()
    electric_car.stop()

    print("\n" + "=" * 50)
    print("继承关系验证")
    print("=" * 50)
    print(f"FuelCar是Car的子类吗？ {issubclass(FuelCar, Car)}")
    print(f"ElectricCar是Car的子类吗？ {issubclass(ElectricCar, Car)}")
    print(f"fuel_car是Car的实例吗？ {isinstance(fuel_car, Car)}")
    print(f"electric_car是Car的实例吗？ {isinstance(electric_car, Car)}")

# 私有方法，双下划线开头
# shift+回车，新起一行
# 魔法方法，双下划线开头，双下划线结尾

# 子类继承父类，会将父类公共的属性和方法继承下来（不含私有）
