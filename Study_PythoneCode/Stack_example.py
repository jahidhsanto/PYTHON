books = []
books.append("Learn C")
books.append("Learn C++")
books.append("Learn Java")
print(books)

books.pop()
print("Now the top book is: ", books[-1])   # [-1] is for last item

books.pop()
print("Now the top book is: ", books[-1])   # [-1] is for last item

books.pop()
if not books:
    print("No books left")