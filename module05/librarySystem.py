# 图书馆管理系统
import json

from module05.book import Book
from module05.member import Member, VIPMember, NormalMember


class LibrarySystem:
    def __init__(self):
        self.books = {}  # 书籍列表 --> {"A1001": Book对象, "A1002": ...}
        self.members = {}  # 会员列表 --> {"N001": Member对象, "N002": ...}
        self.current_member: Member | None = None  # 当前登录会员

        # 加载数据（书籍、会员）
        self.load_books_data()
        self.load_members_data()

    def load_books_data(self):
        # 加载 databooks.json 中的数据
        with open("books.json", "r", encoding="utf-8") as f:
            books_data = json.load(f)

        for book in books_data:
            self.books[book['编号']] = Book(book['编号'], book['标题'], book['作者'], book['总数'])

        print("加载书籍数据成功！")
        print(self.books)

    def load_members_data(self):
        with open("members.json", "r", encoding="utf-8") as f:
            members_data = json.load(f)

        for member in members_data:
            if member['卡号'].startswith('N'):
                self.members[member['卡号']] = NormalMember(
                    member['卡号'],
                    member['姓名'],
                    member['密码']
                )
            elif member['卡号'].startswith('V'):
                self.members[member['卡号']] = VIPMember(
                    member['卡号'],
                    member['姓名'],
                    member['密码'],
                    member['会员等级']
                )

        print("加载会员数据成功！")
        print(self.members)

    def login(self):  # 登录
        while True:
            print("【登录】")
            member_id = input("请输入会员卡号：")
            password = input("请输入会员密码：")

            # 判断会员卡号是否存在
            if member_id not in self.members:
                print("登录失败，会员卡号不存在！")
                continue

            # 判断密码是否正确
            member = self.members[member_id]
            if member.get_password() == password:
                print("登录成功！")
                print(f"欢迎你，{member.name}！")
                self.current_member = member
                return True
            else:
                print("登录失败，密码错误！")
                continue

    def run(self):
        if self.login():
            while True:
                print("\n1. 借阅图书")
                print("2. 归还图书")
                print("3. 查看借阅")
                print("4. 退出系统")

                choice = input("请选择操作(1-4)：")

                match choice:
                    case "1":
                        self.borrow_book()
                    case "2":
                        self.return_book()
                    case "3":
                        self.show_borrowed_books()
                    case "4":
                        print("退出系统，Bye Bye ~")
                        break
                    case _:
                        print("无效的选项，请重新选择！")

    def borrow_book(self):  # 借阅图书
        # 1. 展示出当前图书馆的图书列表
        for book in self.books.values():
            print(f"编号: {book.book_id}, 标题: {book.title}, 作者: {book.author}, "
                  f"总数: {book.total_num}, 可用: {book.get_available_num()}")

        # 2. 获取用户输入的图书编号，执行借书操作
        book_id = input("请输入要借阅的图书编号：")

        if book_id not in self.books:
            print("借阅失败，图书编号不存在！")
            return

        self.current_member.borrow_book(self.books[book_id])

    def show_borrowed_books(self):
        print("【已经借阅的图书列表：】")
        for book in self.current_member.get_borrowed_books():
            print(f"编号: {book.book_id}, 标题: {book.title}")

    def return_book(self):
        # 1. 展示出当前会员的借阅列表
        borrowed_books = self.current_member.get_borrowed_books()
        print("【已经借阅的图书列表：】")
        for book in borrowed_books:
            print(f"编号: {book.book_id}, 标题: {book.title}")

        # 2. 获取用户输入的图书编号，执行还书操作
        book_id = input("请输入要归还的图书编号：")

        if book_id not in self.books:
            print("还书失败，图书编号不存在！")
            return

        self.current_member.return_book(self.books[book_id])


if __name__=="__main__":
    ls=LibrarySystem()
    ls.run()
