"""
继承特性测试 - 公共属性 vs 私有属性
=================================
验证：子类会继承父类的公共属性和方法，但不会继承私有属性和方法
"""


class Parent:
    """
    父类

    包含：
        - 公共属性：public_attr
        - 私有属性：__private_attr（双下划线开头）
        - 公共方法：public_method()
        - 私有方法：__private_method()（双下划线开头）
    """

    def __init__(self):
        # 公共属性（可以被子类访问和继承）
        self.public_attr = "我是公共属性"

        # 私有属性（不能被子类直接访问和继承）
        self.__private_attr = "我是私有属性"

    def public_method(self):
        """公共方法（可以被子类继承）"""
        print("Parent.public_method() 被调用")
        return "公共方法的返回值"

    def __private_method(self):
        """私有方法（不能被子类直接继承）"""
        print("Parent.__private_method() 被调用")
        return "私有方法的返回值"

    def show_private_attr(self):
        """
        父类内部访问私有属性的方法

        说明：虽然子类不能直接访问私有属性，
        但可以通过父类的公共方法间接访问
        """
        print(f"通过父类方法访问私有属性：{self.__private_attr}")
        return self.__private_attr


# ==================== 子类 ====================
class Child(Parent):
    """
    子类

    继承了Parent类的所有公共属性和方法
    但不继承私有属性和方法
    """

    def child_method(self):
        """子类自己的方法"""
        print("\n【Child.child_method()】测试继承情况：")

        # ✅ 可以访问父类的公共属性
        print(f"✓ 访问父类公共属性：{self.public_attr}")

        # ✅ 可以调用父类的公共方法
        result = self.public_method()
        print(f"✓ 调用父类公共方法成功，返回值：{result}")

        # ❌ 尝试访问父类的私有属性（会报错）
        try:
            print(self.__private_attr)  # AttributeError
        except AttributeError as e:
            print(f"✗ 无法直接访问父类私有属性：{e}")

        # ❌ 尝试调用父类的私有方法（会报错）
        try:
            self.__private_method()  # AttributeError
        except AttributeError as e:
            print(f"✗ 无法直接调用父类私有方法：{e}")

        # ✅ 可以通过父类的公共方法间接访问私有属性
        private_value = self.show_private_attr()
        print(f"✓ 通过父类公共方法间接访问私有属性：{private_value}")


# ==================== 测试代码 ====================
if __name__ == '__main__':
    print("=" * 60)
    print("测试1：创建父类实例，测试公共和私有成员")
    print("=" * 60)
    parent = Parent()
    print(f"公共属性：{parent.public_attr}")
    print(f"调用公共方法：{parent.public_method()}")
    print(f"通过方法访问私有属性：{parent.show_private_attr()}")

    # 尝试直接访问私有属性（会报错）
    try:
        print(parent.__private_attr)
    except AttributeError as e:
        print(f"❌ 外部无法直接访问私有属性：{e}")

    # 尝试直接调用私有方法（会报错）
    try:
        parent.__private_method()
    except AttributeError as e:
        print(f" 外部无法直接调用私有方法：{e}")

    print("\n" + "=" * 60)
    print("测试2：创建子类实例，测试继承情况")
    print("=" * 60)
    child = Child()

    # 测试公共成员的继承
    print(f"\n✓ 子类继承了父类公共属性：{child.public_attr}")
    print(f"✓ 子类可以调用父类公共方法：", end="")
    child.public_method()

    # 测试私有成员的继承
    print("\n尝试访问父类私有属性：")
    try:
        print(child.__private_attr)
    except AttributeError as e:
        print(f"❌ 子类无法直接访问父类私有属性：{e}")

    print("\n尝试调用父类私有方法：")
    try:
        child.__private_method()
    except AttributeError as e:
        print(f"❌ 子类无法直接调用父类私有方法：{e}")

    # 调用子类的测试方法
    child.child_method()

    print("\n" + "=" * 60)
    print("测试3：查看对象的属性字典")
    print("=" * 60)
    print(f"\n父类实例的属性：{parent.__dict__}")
    print(f"子类实例的属性：{child.__dict__}")

    print("\n" + "=" * 60)
    print("总结")
