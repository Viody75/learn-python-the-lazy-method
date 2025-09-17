# Summary for lesson 2:
# - String adalah tipe data immutable.
# - String mendukung berbagai operasi seperti indexing, slicing, dan metode bawaan.


# Inisialisasi string
teks = "Hello, Python!"

print("=== String Dasar ===")
print("Teks:", teks)
print("Panjang:", len(teks))          # panjang string
print("Uppercase:", teks.upper())     # huruf besar
print("Lowercase:", teks.lower())     # huruf kecil
print("Title:", teks.title())         # kapital di awal kata
print("Replace:", teks.replace("Python", "World"))  # membuat string baru

# --- Slicing ---
print("\n=== String Slicing ===")
print("Index 0:", teks[0])        # karakter pertama
print("Index -1:", teks[-1])      # karakter terakhir
print("Slice [0:5]:", teks[0:5])  # dari index 0 sampai 5
print("Slice [:5]:", teks[:5])    # dari awal sampai 5
print("Slice [7:]:", teks[7:])    # dari index 7 sampai akhir
print("Step [::2]:", teks[::2])   # lompat 2 karakter
print("Reverse:", teks[::-1])     # membalik string

kalimat = "Belajar Python itu menyenangkan"

print("\n=== Fungsi Bawaan String ===")
print("Apakah diawali 'Belajar'? ->", kalimat.startswith("Belajar"))
print("Apakah diakhiri 'seru'? ->", kalimat.endswith("seru"))
print("Apakah semua huruf? ->", kalimat.isalpha())
print("Apakah semua angka? ->", "12345".isdigit())

# Split dan Join
kata = kalimat.split(" ")      # pecah berdasarkan spasi
print("Split:", kata)

gabung = "-".join(kata)        # gabung dengan tanda "-"
print("Join:", gabung)

# Strip
teks2 = "   Python   "
print("Asli dengan spasi:", repr(teks2))
print("Strip:", repr(teks2.strip()))  # hapus spasi kiri/kanan
