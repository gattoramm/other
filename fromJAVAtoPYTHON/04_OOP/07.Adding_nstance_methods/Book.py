class Book:
    # constructor
    def __init__(self, name, copies) -> None:
        self.name2 = name
        self.copies2 = copies

    #toString
    def __repr__(self) -> str:
        return repr((self.name2, self.copies2))

    def increase_copies(self, how_much):
        self.copies2 += how_much

    def decrease_copies(self, how_much):
        self.copies2 -= how_much

#instances
book2 = Book('John', 200)
book2.increase_copies(50
)
book3 = Book('Mike', 15)
book3.decrease_copies(10)

print(book2)
print(book3)