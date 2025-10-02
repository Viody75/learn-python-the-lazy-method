# Contoh lengkap OOP di Python
from abc import ABC, abstractmethod

# 1. Class & Object
class Animal:
    def __init__(self, name):  # Constructor
        self.name = name  # Attribute
    def speak(self):  # Method
        print(f"{self.name} makes a sound.")

# 2. Inheritance
class Dog(Animal):
    def speak(self):  # Polymorphism: override method
        print(f"{self.name} says: Woof!")

class Cat(Animal):
    def speak(self):  # Polymorphism: override method
        print(f"{self.name} says: Meow!")

# 3. Encapsulation
class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # Private attribute

    is_a = 'Human'

    def get_age(self):
        return self.__age
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive!")
    
    def info(self):
        print(f"{self.name} is {self.__age} years old {self.is_a}.")

# 4. Abstraction
class Vehicle(ABC):  # Abstract Base Class
    @abstractmethod
    def drive(self):
        pass

class Car(Vehicle):
    def drive(self):
        print("Car is driving.")

class Bike(Vehicle):
    def drive(self):
        print("Bike is driving.")

# 5. Usage Example
if __name__ == "__main__":
    # Object instantiation
    a = Animal("Generic Animal")
    d = Dog("Buddy")
    c = Cat("Kitty")
    a.speak()  # Output: Generic Animal makes a sound.
    d.speak()  # Output: Buddy says: Woof!
    c.speak()  # Output: Kitty says: Meow!

    # Encapsulation
    p = Person("Alice", 30)
    print(f"{p.name}'s age:", p.get_age())
    p.set_age(-5)  # Invalid
    p.set_age(35)  # Valid
    print(f"{p.name}'s new age:", p.get_age())
    p.info()

    # Abstraction & Polymorphism
    vehicles = [Car(), Bike()]
    for v in vehicles:
        v.drive()  # Output: Car is driving. Bike is driving.

# Penjelasan:
# - Class: template untuk membuat objek
# - Object: instance dari class
# - Attribute: data yang dimiliki objek
# - Method: fungsi yang dimiliki objek
# - Inheritance: pewarisan sifat dari class induk ke anak
# - Encapsulation: membatasi akses data (private/protected)
# - Polymorphism: method yang sama, perilaku berbeda
# - Abstraction: class/fungsi yang hanya sebagai blueprint