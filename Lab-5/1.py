class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_info(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)

    def update_price(self, new_price):
        self.price = new_price

book1 = Book("Advanced Programming", "Saksham Dhakal", 1000)
book1.display_info()
book1.update_price(1050)
book1.display_info()
