class Book:
    # constructor
    def __init__(self, name) -> None:
        self.name2 = name

    #toString
    def __repr__(self) -> str:
        return repr(self.name2)

#instances
book2 = Book("John")
book3 = Book("Mike")

print(book2)
print(book3)