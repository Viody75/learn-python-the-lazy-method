# Python menyediakan built-in open() untuk manipulasi file.
# Mode umum:
# "r" → read (default)
# "w" → write (overwrite)
# "a" → append
# "x" → create (error jika sudah ada)
# "b" → binary (misal "rb")

# Membuat / overwrite file
with open("contoh.txt", "w") as f:
    f.write("Halo, ini baris pertama.\n")
    f.write("Baris kedua.\n")

print("\nFile 'contoh.txt' berhasil dibuat dan ditulis ulang.")

# Menambahkan ke file tanpa menghapus isi lama
with open("contoh.txt", "a") as f:
    f.write("Tambahan baris ketiga.\n")

print("Isi baru berhasil ditambahkan ke 'contoh.txt'.")

# Membaca seluruh isi
with open("contoh.txt", "r") as f:
    isi = f.read()

print("\n=== Isi file ===")
print(isi)

# Membaca baris demi baris
with open("contoh.txt", "r") as f:
    for baris in f:
        print("Baris:", baris.strip())

try:
    with open("tidak_ada.txt", "r") as f:
        data = f.read()
except FileNotFoundError as e:
    print("\nException ditangkap:", e)
