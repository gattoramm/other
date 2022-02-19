class Book:
    # constructor
    def __init__(self, name, copies) -> None:
        self.name2 = name
        self.copies2 = copies

    #toString
    def __repr__(self) -> str:
        return repr((self.name2, self.copies2))

#instances
book2 = Book('John', 200)
book3 = Book('Mike', 15)

print(book2)
print(book3)