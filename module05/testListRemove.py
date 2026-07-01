from module05.book import Book

books=[Book("1001","水浒传","施耐庵",100),
       Book("2002","西游记","吴承恩",5),
       Book("3003","三国演义","罗贯中",120),
       Book("4004","红楼梦","曹雪芹",80)]

book1=books[0]
# bookToBeRemoved=Book(book1.book_id,book1.title,book1.author,book1.total_num)
bookToBeRemoved=Book(book1.book_id,"水浒后转","施主",88)
books.remove(bookToBeRemoved)
print(books)