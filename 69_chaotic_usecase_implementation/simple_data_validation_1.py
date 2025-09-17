# Tulislah program Python yang menerima daftar data karyawan dalam bentuk:
# Nama, Jenis Kelamin, dan Usia
# Validasi bahwa:
# Jenis kelamin hanya boleh "L" atau "P"
# Usia harus > 0 dan ≤ 100
# Tampilkan daftar karyawan yang datanya valid saja.

data = [("Andi", "L", 101), ("Budi", "X", 32), ("Cici", "P", 20)] # Asumsikan ke data ke list of tuple, karena anggap data adalah final / fix / immutable

data_valid = []
for el in data :
    if (el[1] == "L" or el[1] == "P") and (0 < el[2] <= 100):
        print(el[0], 'Valid')
        data_valid.append((el[0],el[1],el[2]))
    else:
        print(el[0], 'InValid')
print(data_valid)