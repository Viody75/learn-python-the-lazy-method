# Buat program Python yang menerima daftar pegawai berupa:
# [("Ali", 80, 85, 90), ("Budi", 70, 65, 80), ...]
# Setiap tuple berisi nama, skor kehadiran, skor kedisiplinan, dan skor hasil kerja.
# Hitung nilai akhir pegawai dengan rumus:
# nilai_akhir = 0.3 * kehadiran + 0.2 * kedisiplinan + 0.5 * hasil_kerja
# Klasifikasikan kinerja:

# ≥ 85: Sangat Baik
# ≥ 70: Baik
# ≥ 55: Cukup
# < 55: Perlu Pembinaan

jumlah_pegawai = int(input("Set Jumlah Pegawai : "))

data = []
for i in range(jumlah_pegawai):
    print(f"Entri data ke-{i+1}")
    nama_pegawai = input('Masukan Nama :')
    skor_hadir = int(input('Skor Kehadiran :')) 
    skor_disiplin = int(input('Skor Disiplin :')) 
    skor_kerja = int(input('Skor Hasil Kerja :'))
    nilai_akhir = 0.3 * skor_hadir + 0.2 * skor_disiplin + 0.5 * skor_kerja

    predikat = ''
    if nilai_akhir >= 85:
        predikat = 'Sangat Baik'
    elif nilai_akhir >= 70:
        predikat = 'Baik'
    elif nilai_akhir >= 55:
        predikat = 'Cukup'
    else :
        predikat = 'Perlu Pembinaan'

    data.append((nama_pegawai, skor_hadir, skor_disiplin, skor_kerja, nilai_akhir, predikat))

print(data)