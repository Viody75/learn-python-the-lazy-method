# Summary for lesson 3:
# - List adalah tipe data mutable.
# - List mendukung berbagai operasi seperti penambahan, penghapusan, dan pengubahan elemen.

# Inisialisasi list
angka = [1, 2, 3]

print("=== LIST DEMO ===")
print("List awal:", angka)  # [1, 2, 3]

# --- Mutation ---
angka.append(4)  
print("Setelah append(4):", angka)  # [1, 2, 3, 4]

angka[0] = 99  
print("Setelah ubah index 0 jadi 99:", angka)  # [99, 2, 3, 4]

angka.remove(2)  
print("Setelah remove(2):", angka)  # [99, 3, 4]

# --- Iteration ---
print("\nIterasi dengan for-loop:")
for val in angka:
    print("elemen:", val)

# --- List comprehension ---
kuadrat = [x**2 for x in angka]
print("\nHasil kuadrat tiap elemen (list comprehension):", kuadrat)

# --- Fungsi bawaan ---
print("\nFungsi bawaan list:")
print("sorted(angka):", sorted(angka))     # return list baru, tidak mengubah asli
angka.sort(reverse=True)                   # in-place sorting (descending)
print("setelah angka.sort(reverse=True):", angka)

