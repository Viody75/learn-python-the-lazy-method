jumlah_pegawai = int(input("Set Jumlah Pegawai : "))

data = {}  # key: nama_pegawai, value: dict dengan skor dan hasil

i = 0
while i < jumlah_pegawai:
    print(f"Entri data ke-{i+1}")
    nama_pegawai = input('Masukan Nama :')

    if nama_pegawai in data:
        print("❌ Nama sudah ada! Silakan masukkan nama yang berbeda.\n")
        continue

    skor_hadir = int(input('Skor Kehadiran :')) 
    skor_disiplin = int(input('Skor Disiplin :')) 
    skor_kerja = int(input('Skor Hasil Kerja :'))

    nilai_akhir = 0.3 * skor_hadir + 0.2 * skor_disiplin + 0.5 * skor_kerja

    if nilai_akhir >= 85:
        predikat = 'Sangat Baik'
    elif nilai_akhir >= 70:
        predikat = 'Baik'
    elif nilai_akhir >= 55:
        predikat = 'Cukup'
    else:
        predikat = 'Perlu Pembinaan'

    # Simpan dalam dict
    data[nama_pegawai] = {
        "skor_hadir": skor_hadir,
        "skor_disiplin": skor_disiplin,
        "skor_kerja": skor_kerja,
        "nilai_akhir": round(nilai_akhir, 2),
        "predikat": predikat
    }

    i += 1

# Output hasil
print("\nData Pegawai:")
print("-" * 40)
for nama, info in data.items():
    print(f"Nama         : {nama}")
    print(f"Kehadiran    : {info['skor_hadir']}")
    print(f"Disiplin     : {info['skor_disiplin']}")
    print(f"Hasil Kerja  : {info['skor_kerja']}")
    print(f"Nilai Akhir  : {info['nilai_akhir']}")
    print(f"Predikat     : {info['predikat']}")
    print("-" * 40)
