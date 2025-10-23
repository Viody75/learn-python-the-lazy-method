# ===============================================
# SOAL 2: Recursive & Algorithm Complexity
# ===============================================

# Fungsi rekursif untuk menghitung FPB dua bilangan
def fpb(a, b):
    if b == 0:
        return a
    return fpb(b, a % b)

# Fungsi rekursif untuk menghitung FPB dari seluruh elemen list
def fpb_list(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        first = numbers[0]
        rest = numbers[1:]
        return fpb(first, fpb_list(rest))

# --- Contoh Pengujian ---
data1 = [5, 10]
data2 = [9, 6, 12, 18]
data3 = [15, 25, 35, 10]

print("=== (a) Hasil Pengujian FPB Rekursif ===")
print(f"{data1} -> FPB = {fpb_list(data1)}")
print(f"{data2} -> FPB = {fpb_list(data2)}")
print(f"{data3} -> FPB = {fpb_list(data3)}")
