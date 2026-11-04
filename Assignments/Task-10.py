class Student:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}"


student1 = Student("Ana")
student2 = Student("Bo")

assert student1.greet() == "Hello, Ana"
assert student2.greet() == "Hello, Bo"