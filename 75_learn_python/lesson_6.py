# Summary for lesson 6:
# - Tuple adalah tipe data immutable yang menyimpan urutan elemen.
# - Mendukung operasi indexing, slicing, dan iterasi.
# - Dapat berisi elemen dari berbagai tipe data, termasuk nested tuples dan lists.

# Inisialisasi tuple
angka_tuple = (1, 2, 3, 4, 5)

print("=== TUPLE DEMO ===")
print("Tuple awal:", angka_tuple)   # (1, 2, 3, 4, 5)
print("Panjang tuple:", len(angka_tuple))  # 5

# --- Indexing & Slicing ---
print("\nIndexing & Slicing:")
print("Elemen index 0:", angka_tuple[0])      # 1
print("Elemen index -1 (terakhir):", angka_tuple[-1])  # 5
print("Slice [1:4]:", angka_tuple[1:4])       # (2, 3, 4)
print("Slice [::2] (step 2):", angka_tuple[::2])  # (1, 3, 5)

# --- Iteration ---
print("\nIterasi tuple dengan for:")
for val in angka_tuple:
    print("elemen:", val)

# --- Tuple Bersarang (Nested) ---
nested = (1, (2, 3), [4, 5])
print("\nTuple bersarang:", nested)
print("Access nested tuple:", nested[1][0])   # ambil 2
print("Access nested list:", nested[2][1])    # ambil 5

# --- Immutable behavior ---
print("\nCoba mutasi tuple (akan error):")
try:
    angka_tuple[0] = 99 # type: ignore
except TypeError as e:
    print("Error ditangkap:", e)

hewan = ("kucing", "anjing", "burung", "kucing")

print("\n=== Fungsi Bawaan Tuple ===")
print("Tuple:", hewan)

# count() -> hitung jumlah elemen tertentu
print("Jumlah 'kucing':", hewan.count("kucing"))  # 2

# index() -> cari posisi pertama elemen
print("Index 'burung':", hewan.index("burung"))   # 2

# tuple() -> konversi dari list
hewan_list = ["ikan", "ular", "ayam"]
hewan_tuple = tuple(hewan_list)
print("Dari list ke tuple:", hewan_tuple)
