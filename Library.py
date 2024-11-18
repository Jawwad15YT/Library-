class Library:
    global Books
    Books = []
    def __init__(self,title):
        self.title = title
    
    def AddBook(self,title):
        if title not in Books:
            print(f"   {title}Book successfully added!")
            Books.append(title)
        else:
            print("Error! Book already added!")

    def showBooks(self):
        for book in Books:
            print(book)

    def RemoveBook(self,title):
        if title in Books:
            Books.remove(title)
        else:
            print(f"{title} Book not available")
    def borrowBook(self,name,days,title):
        if title in Books:
            print(f"Book sucessfully borrowed by by  {name}  for  {days} ")
        else:
            print("Book not available")


lib = Library("Lin's Library")
lib.AddBook("Chronicles of Narnia ")
lib.AddBook("Chronicles of Narnia 2 ")
lib.AddBook("Chronicles of Narnia 3 ")
lib.AddBook("Chronicles of Narnia 4 ")
lib.AddBook("Chronicles of Narnia 5 ")
print("Available Books")
lib.showBooks
lib.RemoveBook("Chronicles of Narnia ")
lib.RemoveBook("Chronicles of Narnia 10 ")
print("Available Books:")
lib.showBooks()