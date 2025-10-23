# ===============================================
# SOAL 1: Basic Python & Data Structures
# ===============================================

# a. Simpan data ke dalam dictionary bernama data_karyawan
data_karyawan = {
    201: {
        "Nama": "John",
        "Perusahaan": "Google",
        "Departemen": "Engineering",
        "Rincian Gaji": {"Basic": 50000, "Bonus": 10000},
        "Pengalaman (Tahun)": 5
    },
    202: {
        "Nama": "Mary",
        "Perusahaan": "Microsoft",
        "Departemen": "Sales",
        "Rincian Gaji": {"Basic": 60000, "Bonus": 15000},
        "Pengalaman (Tahun)": 4
    },
    203: {
        "Nama": "Alex",
        "Perusahaan": "Amazon",
        "Departemen": "Engineering",
        "Rincian Gaji": {"Basic": 55000, "Bonus": 20000},
        "Pengalaman (Tahun)": 6
    },
    204: {
        "Nama": "Sarah",
        "Perusahaan": "Apple",
        "Departemen": "Marketing",
        "Rincian Gaji": {"Basic": 58000, "Bonus": 12000},
        "Pengalaman (Tahun)": 7
    },
    205: {
        "Nama": "Chris",
        "Perusahaan": "Meta",
        "Departemen": "Engineering",
        "Rincian Gaji": {"Basic": 62000, "Bonus": 18000},
        "Pengalaman (Tahun)": 5
    },
    206: {
        "Nama": "Jessica",
        "Perusahaan": "Twitter",
        "Departemen": "Marketing",
        "Rincian Gaji": {"Basic": 49000, "Bonus": 11000},
        "Pengalaman (Tahun)": 4
    },
    207: {
        "Nama": "Tom",
        "Perusahaan": "Google",
        "Departemen": "Sales",
        "Rincian Gaji": {"Basic": 61000, "Bonus": 9000},
        "Pengalaman (Tahun)": 3
    }
}

print("=== (a) Data Karyawan Awal ===")
for k, v in data_karyawan.items():
    print(f"ID {k}: {v}")

# b. Ubah departemen Alex menjadi Product Development di Amazon
data_karyawan[203]["Departemen"] = "Product Development"
print("\n=== (b) Setelah Update Departemen Alex ===")
print(f"ID 203: {data_karyawan[203]}")

# c. Hitung total gaji dan tambahkan ke setiap data karyawan
for v in data_karyawan.values():
    rincian = v["Rincian Gaji"]
    v["Total Gaji"] = rincian["Basic"] + rincian["Bonus"]

print("\n=== (c) Setelah Menambahkan Total Gaji ===")
for k, v in data_karyawan.items():
    print(f"ID {k}: {v['Nama']} - Total Gaji = {v['Total Gaji']}")

# d. Hapus data Tom (ID 207)
data_karyawan.pop(207)
print("\n=== (d) Setelah Menghapus Tom ===")
for k, v in data_karyawan.items():
    print(f"ID {k}: {v['Nama']}")

# e. Buat dictionary baru untuk karyawan departemen Engineering
karyawan_engineering = {
    k: v for k, v in data_karyawan.items() if v["Departemen"] == "Engineering"
}

print("\n=== (e) Karyawan di Departemen Engineering ===")
for k, v in karyawan_engineering.items():
    print(f"ID {k}: {v['Nama']} - {v['Departemen']}")

# f. Karyawan dengan total gaji di atas rata-rata
total_all = sum(v["Total Gaji"] for v in data_karyawan.values())
avg_total = total_all / len(data_karyawan)

karyawan_gaji_tinggi = {
    k: v for k, v in data_karyawan.items() if v["Total Gaji"] > avg_total
}

print("\n=== (f) Karyawan dengan Gaji di Atas Rata-Rata ===")
print(f"Rata-rata total gaji: {avg_total:.2f}")
for k, v in karyawan_gaji_tinggi.items():
    print(f"{v['Nama']} - Total Gaji: {v['Total Gaji']}")

# g. Karyawan dengan gaji tertinggi di departemen Marketing
marketing_employees = {
    k: v for k, v in data_karyawan.items() if v["Departemen"] == "Marketing"
}

if marketing_employees:
    highest_marketing = max(marketing_employees.values(), key=lambda x: x["Total Gaji"])
    print("\n=== (g) Gaji Tertinggi di Departemen Marketing ===")
    print(f"{highest_marketing['Nama']} - Total Gaji: {highest_marketing['Total Gaji']}")
else:
    print("\nTidak ada karyawan di departemen Marketing")

# h. Hitung rata-rata total gaji per departemen
rata_gaji_departemen = {}
for v in data_karyawan.values():
    dept = v["Departemen"]
    if dept not in rata_gaji_departemen:
        rata_gaji_departemen[dept] = []
    rata_gaji_departemen[dept].append(v["Total Gaji"])

rata_gaji_departemen = {dept: sum(g)/len(g) for dept, g in rata_gaji_departemen.items()}

print("\n=== (h) Rata-rata Total Gaji per Departemen ===")
for dept, avg in rata_gaji_departemen.items():
    print(f"{dept}: {avg:.2f}")
