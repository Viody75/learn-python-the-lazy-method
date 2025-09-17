# Summary for lesson 5:
# - Set adalah tipe data mutable yang menyimpan elemen unik.
# - Mendukung operasi seperti penambahan, penghapusan, dan pengujian keanggotaan.
# - Operasi himpunan seperti union, intersection, dan difference.

# Inisialisasi set (otomatis hilangkan duplikat)
angka_set = {1, 2, 2, 3, 4}
print("\n=== SET DEMO ===")
print("Set awal (otomatis unik):", angka_set)  # {1, 2, 3, 4}

# --- Mutation ---
angka_set.add(5)
print("Setelah add(5):", angka_set)  # {1, 2, 3, 4, 5}

angka_set.discard(2)
print("Setelah discard(2):", angka_set)  # {1, 3, 4, 5}

# --- Iteration ---
print("\nIterasi set (tidak urut):")
for val in angka_set:
    print("elemen:", val)

# --- Operasi himpunan ---
ganjil = {1, 3, 5, 7}
print("\nUnion (angka_set | ganjil):", angka_set | ganjil)
print("Intersection (angka_set & ganjil):", angka_set & ganjil)
print("Difference (angka_set - ganjil):", angka_set - ganjil)
