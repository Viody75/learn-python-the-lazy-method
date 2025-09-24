class fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def add(self, other):
        new_numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        new_denominator = self.denominator * other.denominator
        return fraction(new_numerator, new_denominator)

    def subtract(self, other):
        new_numerator = (self.numerator * other.denominator) - (other.numerator * self.denominator)
        new_denominator = self.denominator * other.denominator
        return fraction(new_numerator, new_denominator)

    def multiply(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return fraction(new_numerator, new_denominator)

    def divide(self, other):
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return fraction(new_numerator, new_denominator)

    def display(self):
        print(f"{self.numerator}/{self.denominator}")

# Contoh penggunaan:
f1 = fraction(1, 2)
f2 = fraction(3, 4) 

result_add = f1.add(f2)
result_sub = f1.subtract(f2)
result_mul = f1.multiply(f2)
result_div = f1.divide(f2)  

print("Tambah: ", end="")
result_add.display()
print("Kurang: ", end="")
result_sub.display()
print("Kali: ", end="")
result_mul.display()
print("Bagi: ", end="")
result_div.display()