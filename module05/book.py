# 书籍类
class Book:
    def __init__(self, book_id, title, author, total_num):
        self.book_id = book_id  # 书籍编号
        self.title = title  # 书籍标题
        self.author = author  # 作者
        self.total_num = total_num  # 总数量
        self.__available_num = total_num  # 可用数量（私有属性）

    def borrow_book(self):  # 借阅书籍
        if self.__available_num > 0:
            self.__available_num -= 1
            return True
        return False

    def return_book(self):  # 归还书籍
        self.__available_num += 1

    def get_available_num(self):  # 获取可用数量
        return self.__available_num
