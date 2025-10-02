class Person:
    def __init__(self, name="John Doe", age=0):
        self.name = name
        self.__age = age  # Private attribute
    
    def __str__(self):
        return f"Person(Name: {self.name}, Age: {self.__age})"
    
    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            print("Age cannot be negative.")
    
    is_a = 'Human'

    size = 'Normal'
    
    def print_size(self):
        print(self.size)
    
    def info(self):
        print(f"Name: {self.name}, Age: {self.__age}")
