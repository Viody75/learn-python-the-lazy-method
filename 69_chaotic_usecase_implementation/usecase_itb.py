# Tuliskan program yang menerima masukan 3 (tiga) buah integer, misalnya a, b, dan x,
# dan menuliskan ke layar bilangan pertama antara a dan b (a dan b termasuk) yang
# merupakan kelipatan (habis dibagi) x. Asumsikan a <= b.
# Contoh masukan: a = 10, b = 20, x = 4
# Tertulis di layar = 12

def calculate():

    a = int(input("Masukan a : "))
    b = int(input("Masukan b : "))
    x = int(input("Masukan x : "))

    new_data = []

    for el in range(a, b):
        if el % 2 != 0 and el % x == 0:
            new_data.append(el)

    print(new_data[:1])

calculate()