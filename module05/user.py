class User:
    def __init__(self, name):
        self._name = name  # 下划线开头表示内部私有属性

    @property
    def name(self):
        """Getter: 类似 Lombok @Getter 将方法转换为只读属性，调用时不需要加括号 Pythonic 方式"""
        return self._name

    @name.setter
    def name(self, value):
        """Setter: 类似 Lombok @Setter 允许在赋值时执行自定义逻辑（如验证、转换） Pythonic 方式"""
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value

# 使用示例
user = User("Alice")
print(user.name)  # 自动调用 getter
user.name = "Bob" # 自动调用 setter

print(user.__dict__)