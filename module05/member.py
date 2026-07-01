# 会员类
from module05.book import Book
from abc import ABC,abstractmethod


class Member(ABC):
    def __init__(self, member_id, name, password):
        self.member_id = member_id  # 会员卡号
        self.name = name  # 会员姓名
        self.__password = password  # 会员密码（私有属性）
        self.__borrowed_books = []  # 借阅书籍列表（私有属性）

    def borrow_book(self, book: Book):  # 借阅书籍
        # 判断当前会员借阅数量是否达到最大限制
        if len(self.__borrowed_books) >= self.get_max_books():
            print("借阅失败，您的借阅数量已达到最大限制！")
            return False

        # 判断书籍是否可借阅
        if book.borrow_book():
            self.__borrowed_books.append(book)
            print(f"{self.name} 已成功借阅图书 {book.title}")
            return True
        else:
            print(f"借阅失败，图书 {book.title} 已被借完！")
            return False

    def return_book(self, book: Book):  # 归还书籍
        # 判断当前会员是否借阅了该书籍
        if book in self.__borrowed_books:
            # 还书
            book.return_book()
            self.__borrowed_books.remove(book)
            print(f"{self.name} 已成功归还图书 {book.title}")
        else:
            print(f"归还失败，您没有借阅图书 {book.title}")

    # 获取会员最大借阅数量（需要在子类中实现）
    @abstractmethod
    def get_max_books(self) -> int:
        # print("get_max_books-父类")
        return  11 #只要有抽象方法，抽象类就不能被实例化
        # pass

    def get_password(self):
        return self.__password

    def get_borrowed_books(self):
        return self.__borrowed_books



# 普通会员类
class NormalMember(Member):
    # pass
    def get_max_books(self) -> int:
        return 3
    def __repr__(self):
        return f"NormalMember({self.member_id}, {self.name}, {self.get_password()}, {self.get_borrowed_books()})"


# VIP会员类
class VIPMember(Member):
    def __init__(self, member_id, name, password, vip_level):
        super().__init__(member_id, name, password)
        self.vip_level = vip_level  # 会员等级

    def get_max_books(self) -> int:
        return 6 + self.vip_level
    def __repr__(self):
        return f"VIPMember({self.member_id}, {self.name}, {self.get_password()}, {self.vip_level}, {self.get_borrowed_books()})"


# 抽象类，只能被继承，不能被实例化。作用就是规定子类必须要实现哪些方式，强制子类必须遵守统一的代码规范。
# python中的抽象类，需要继承abc模块中的ABC类--->ABC：Abstract Base Class
# from abc import ABC,abstractmethod

# normalMember=NormalMember("N001","丁一","Mima910620!")
# # 子例必须实现抽象方法，否则连对象都创建不了...
# print(normalMember.__dict__)
# print(normalMember.get_max_books()) #TypeError: Can't instantiate abstract class NormalMember without an implementation for abstract method 'get_max_books'
# # 子类必须要实现所有的抽象方法


member=Member("N002","肖志博","754673XzbMima!") #TypeError: Can't instantiate abstract class Member without an implementation for abstract method 'get_max_books'
# #但是如果Member类继承了ABC（如果内部没有抽象方法的话），也可以直接被实例化
# # 如果抽象类内部，有抽象方法，则不能被实例化
# print(member.__dict__)
# print(member.get_max_books()) #TypeError: Can't instantiate abstract class Member without an implementation for abstract method 'get_max_books'
