def book_info(title, author, year):
    print(f"Title: {title}, Author: {author}, Year: {year}")

title = input("Enter book title: ")
author = input("Enter author name: ")
year = int(input("Enter publication year: "))

book_info(title=title, author=author, year=year)
