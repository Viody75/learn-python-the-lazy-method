# Buatlah program Python yang menerima input daftar mahasiswa, masing-masing dengan nilai tugas, UTS, dan UAS. Hitung nilai akhir dengan bobot berikut:
# Tugas: 20%
# UTS: 30%
# UAS: 50%
# Tampilkan output berupa daftar nama mahasiswa, nilai akhirnya, dan predikat huruf (A, B, C, D, E).


def hitung_nilai_akhir(tugas, uts, uas):
    return round((0.2 * tugas) + (0.3 * uts) + (0.5 * uas), 2)

def konversi_predikat(nilai):
    if nilai >= 85:
        return 'A'
    elif nilai >= 75:
        return 'B'
    elif nilai >= 65:
        return 'C'
    elif nilai >= 50:
        return 'D'
    else:
        return 'E'

# Input jumlah mahasiswa
jumlah = int(input("Berapa jumlah mahasiswa? "))

mahasiswa_list = []

for i in range(jumlah):
    print(f"\nMahasiswa ke-{i+1}")
    nama = input("Nama: ")
    tugas = float(input("Nilai Tugas: "))
    uts = float(input("Nilai UTS: "))
    uas = float(input("Nilai UAS: "))
    
    mahasiswa_list.append({
        "name": nama,
        "tugas": tugas,
        "uts": uts,
        "uas": uas
    })

# Output
print("\nHasil Nilai Mahasiswa:")
print("-" * 40)
for m in mahasiswa_list:
    akhir = hitung_nilai_akhir(m['tugas'], m['uts'], m['uas'])
    predikat = konversi_predikat(akhir)
    print(f"Nama       : {m['name']}")
    print(f"Nilai Akhir: {akhir}")
    print(f"Predikat   : {predikat}")
    print("-" * 40)
