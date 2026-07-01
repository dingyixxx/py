class Car:
    """汽车基类"""

    def __init__(self, brand, model, color, owner):
        self.brand = brand  # 品牌(公有属性)
        self.model = model  # 型号(公有属性)
        self.color = color  # 颜色(公有属性)
        self.__owner = owner  # 拥有者(私有属性)
        self.__is_running = False  # 运行状态(私有属性)

    def start(self):
        """启动车辆"""
        if not self.__is_running:
            self.__is_running = True
            print(f'🚗 {self.brand} {self.model} 正在启动...')
        else:
            print(f'⚠️ {self.brand} {self.model} 已经在运行中！')

    def run(self):
        """行驶"""
        if self.__is_running:
            print(f'👤 {self.get_owner()} : {self.brand} {self.model} 正在行驶...')
        else:
            print(f' {self.brand} {self.model} 未启动，无法行驶！')

    def stop(self):
        """停止车辆"""
        if self.__is_running:
            self.__is_running = False
            print(f'🛑 {self.brand} {self.model} 已停止行驶...')
        else:
            print(f'⚠️ {self.brand} {self.model} 本来就是停止的！')

    def get_owner(self):
        """获取脱敏后的车主信息"""
        return self.__owner[0:1] + "**"

    def get_full_owner(self):
        """获取完整车主信息（内部使用）"""
        return self.__owner

    def status(self):
        """显示车辆状态"""
        state = "运行中" if self.__is_running else "已停止"
        print(f"📊 [{self.brand} {self.model}] 颜色:{self.color} 车主:{self.get_owner()} 状态:{state}")


# ========== 燃油车 ==========
class FuelCar(Car):
    """燃油汽车"""

    def __init__(self, brand, model, color, owner, fuel_type="汽油"):
        super().__init__(brand, model, color, owner)  # 调用父类构造函数
        self.fuel_type = fuel_type  # 燃油类型
        self.fuel_level = 100  # 油量百分比

    def charge(self):
        """加油"""
        self.fuel_level = 100
        print(f'⛽ {self.brand} {self.model} 正在加{self.fuel_type}... 油量已加满！')

    def status(self):
        """重写状态显示，增加油量信息"""
        super().status()
        print(f"    油量: {self.fuel_level}% ({self.fuel_type})")


# ========== 电动车 ==========
class ElectricCar(Car):
    """电动汽车"""

    def __init__(self, brand, model, color, owner, battery_capacity=100):
        super().__init__(brand, model, color, owner)  # 调用父类构造函数
        self.battery_capacity = battery_capacity  # 电池容量
        self.battery_level = battery_capacity  # 当前电量

    def charge(self):
        """充电"""
        self.battery_level = self.battery_capacity
        print(f'🔌 {self.brand} {self.model} 正在充电... 电量已充满！')

    def status(self):
        """重写状态显示，增加电量信息"""
        # super().status()
        Car.status(self)
        print(f"   🔋 电量: {self.battery_level}/{self.battery_capacity} kWh")
    def __str__(self):
        return f"{self.brand} {self.model} {self.color} {self.fuel_type}"


# ========== 测试 ==========
if __name__ == '__main__':
    print("=" * 40)
    print("🚘 燃油车测试")
    print("=" * 40)
    c1 = FuelCar(brand="BMW", model="X5", color="黑色", owner="张三", fuel_type="95号汽油")
    c1.status()
    c1.start()
    c1.run()
    c1.charge()
    c1.stop()

    print("\n" + "=" * 40)
    print("⚡ 电动车测试")
    print("=" * 40)
    c2 = ElectricCar(brand="特斯拉", model="Model Y", color="白色", owner="李四", battery_capacity=80)
    c2.status()
    c2.start()
    c2.run()
    c2.charge()
    c2.stop()

    print("\n" + "=" * 40)
    print("🔒 私有属性测试")
    print("=" * 40)
    print(f"车主(脱敏): {c1.get_owner()}")
    print(f"车主(完整): {c1.get_full_owner()}")
    # print(c1.__owner)  # ❌ 这会报错！
