from abc import ABC, abstractmethod


class Database(ABC):
    # 必须实现的抽象方法
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def query(self, sql):
        pass

    # 可选实现的抽象方法（有默认实现，但子类仍必须显式重写）
    @abstractmethod
    def get_timeout(self) -> int:
        return 30

    # 普通方法（子类可选择性重写）
    def get_connection_string(self) -> str:
        return "default_connection_string"


class MySQL(Database):
    def connect(self):
        print("Connecting to MySQL...")

    def query(self, sql):
        print(f"Querying: {sql}")

    # 必须重写所有 @abstractmethod 标记的方法
    def get_timeout(self) -> int:
        return super().get_timeout()  # 使用父类默认值 30


class PostgreSQL(Database):
    def connect(self):
        print("Connecting to PostgreSQL...")

    def query(self, sql):
        print(f"Querying: {sql}")

    def get_timeout(self) -> int:
        return 60  # 自定义值

    def get_connection_string(self) -> str:
        return "postgresql://localhost:5432"  # 重写普通方法


# 都可以实例化
mysql = MySQL()
print(mysql.get_timeout())  # 输出: 30

postgres = PostgreSQL()
print(postgres.get_timeout())  # 输出: 60
print(postgres.get_connection_string())  # 输出: postgresql://localhost:5432
