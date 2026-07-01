# 书籍类
class Book:
    def __init__(self, book_id, title, author, total_num):
        self.book_id = book_id  # 书籍编号
        self.title = title  # 书籍标题
        self.author = author  # 作者
        self.total_num = total_num  # 总数量
        self.__available_num = total_num  # 可用数量（私有属性）



    def __eq__(self, other):
        # return self.book_id == other.book_id
        print(self)
        print(self.__dict__)
        print(other)
        print(other.__dict__)
        return False

    def borrow_book(self):  # 借阅书籍
        if self.__available_num > 0:
            self.__available_num -= 1
            return True
        return False

    def return_book(self):  # 归还书籍
        self.__available_num += 1

    def get_available_num(self):  # 获取可用数量
        return self.__available_num
    def __repr__(self):
        return f"Book [book_id={self.book_id}, title={self.title}, author={self.author}, total_num={self.total_num}, available_num={self.__available_num}]"

    def __str__(self):
        return f"Book [book_id={self.book_id}, title={self.title}, author={self.author}, total_num={self.total_num}, available_num={self.__available_num}]"
"""
print(book)：直接打印单个对象时，调用 __str__()
print(dict)：打印包含对象的字典/列表时，调用 __repr__()
"""