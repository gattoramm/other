# Student(college, year, degree) IS A Person(name, address)

class Person:
    def __init__(self, name) -> None:
        self.name = name
    
    def __repr__(self) -> str:
        return repr((self.name))


class Student(Person):
    def __init__(self, name, college_name) -> None:
        super().__init__(name)
        self.college_name = college_name

    def __repr__(self) -> str:
        return repr((super().__repr__(), self.college_name))

person = Person('John')

student = Student('John', 'MIT')

print(person)
print(student)