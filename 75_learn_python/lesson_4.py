# Summary for lesson 4:
# - Dictionary adalah tipe data mutable yang menyimpan pasangan key-value.
# - Key harus tipe data yang hashable (seperti str, int, tuple), sedangkan value bisa tipe data apa saja.
# - Mendukung operasi penambahan, penghapusan, dan pengubahan elemen.
# - Exception handling dengan try-except untuk menghindari error saat mengakses key yang tidak ada.

# Inisialisasi dictionary
profil = {"nama": "Viody", "umur": 25}

print("\n=== DICT DEMO ===")
print("Dict awal:", profil)  # {'nama': 'Viody', 'umur': 25}

# --- Mutation ---
profil["kota"] = "Bandung"  
print("Setelah tambah key 'kota':", profil)  # {'nama': 'Viody', 'umur': 25, 'kota': 'Bandung'}

profil["umur"] = 26  
print("Setelah update 'umur' jadi 26:", profil)  # {'nama': 'Viody', 'umur': 26, 'kota': 'Bandung'}

del profil["nama"]  
print("Setelah hapus key 'nama':", profil)  # {'umur': 26, 'kota': 'Bandung'}

# --- Iteration ---
print("\nIterasi key-value pair:")
for key, value in profil.items():
    print(f"{key} -> {value}")

# --- Exception Handling ---
print("\nCoba akses key yang tidak ada:")
try:
    print(profil["alamat"])
except KeyError as e:
    print("KeyError ditangkap:", e)
