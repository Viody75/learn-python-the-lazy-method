# Asumsi bentuk data sebagai berikut [{"nama" : "budi", "waktu" : "12:00"},{"nama" : "andi", "waktu" : "11:00"}]
# Sistem bisa melakukan pengecekan data jam clock-in kerja, lalu menyatukan waktu di nama yang relevan secara langsung mengubah format data nya

data = [
    {"nama": "budi", "waktu": "12:00"},
    {"nama": "andi", "waktu": "11:00"},
    {"nama": "budi", "waktu": "12:10"},
    {"nama": "rudi", "waktu": "10:30"},
    {"nama": "budi", "waktu": "12:20"},
    {"nama": "tabuti", "waktu": "11:30"},
    {"nama": "rudi", "waktu": "11:30"},
    {"nama": "dimas", "waktu": "12:30"},
]

riwayat_waktu = []

for e in data: 
    print('Cek element:', e)
    nama = e["nama"]
    waktu = e["waktu"]

    # Cek apakah nama sudah ada di riwayat
    ditemukan = False
    for r in riwayat_waktu:
        if r["nama"] == nama:
            r["waktu"].append(waktu)
            ditemukan = True
            break

    if not ditemukan:
        riwayat_waktu.append({"nama": nama, "waktu": [waktu]})

print(riwayat_waktu)

