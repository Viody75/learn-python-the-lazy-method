print("=== Iteration with FOR ===")

buah = ["apel", "mangga", "pisang"]

# Iterasi langsung
for b in buah:
    print("Buah:", b)

# Iterasi pakai index
for i in range(len(buah)):
    print(f"Index {i} berisi {buah[i]}")

print("\n=== Iteration with WHILE ===")

count = 0
while count < 3:
    print("Hitungan:", count)
    count += 1

print("\n=== Iteration Dictionary ===")

mahasiswa = {"nama": "Budi", "umur": 21, "jurusan": "Informatika"}

for key, value in mahasiswa.items():
    print(f"{key} → {value}")

print("\n=== List Comprehension ===")

# Buat list kuadrat dari 1–5
kuadrat = [x**2 for x in range(1, 6)]
print("Kuadrat:", kuadrat)

# Filter hanya angka genap
genap = [x for x in range(10) if x % 2 == 0]
print("Genap:", genap)
