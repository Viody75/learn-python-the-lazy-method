# Diberikan dua array kelas_A dan kelas_B berisi data (hari, jam_mulai, jam_selesai).
# Tuliskan fungsi Python yang memeriksa apakah ada jadwal yang bentrok.

# Bentrok jika hari sama dan jamnya overlap.



def cek_bentrok(kelas_list):
    bentrok = []

    for i in range(len(kelas_list)):
        for j in range(i + 1, len(kelas_list)):
            kelas1 = kelas_list[i]
            kelas2 = kelas_list[j]

            if kelas1["hari"] == kelas2["hari"]:
                mulai1 = waktu_ke_menit(kelas1["mulai"])
                selesai1 = waktu_ke_menit(kelas1["keluar"])
                mulai2 = waktu_ke_menit(kelas2["mulai"])
                selesai2 = waktu_ke_menit(kelas2["keluar"])

                if mulai1 < selesai2 and mulai2 < selesai1:
                    bentrok.append((kelas1["nama"], kelas2["nama"], kelas1["hari"]))

    return bentrok

jumlah = int(input("Input jumlah kelas :"))

def waktu_ke_menit(waktu_str):
    jam, menit = waktu_str.split(":")
    return int(jam) * 60 + int(menit)


data = []

for i in range(jumlah):
    print('-')
    nama_kelas = input("Input nama kelas :")
    hari = input("Input hari :")
    jam_mulai =  input("Input jam mulai (ex: 13:00) :")
    jam_keluar = input("Input jam keluar (ex: 14:00) :")

    data.append({"nama" : nama_kelas,"hari" : hari, "mulai": jam_mulai, "keluar": jam_keluar})

bentrok = cek_bentrok(data)

if bentrok:
    for b in bentrok:
        print(f"Jadwal bentrok antara {b[0]} dan {b[1]} pada hari {b[2]}")
else:
    print("Tidak ada jadwal yang bentrok")