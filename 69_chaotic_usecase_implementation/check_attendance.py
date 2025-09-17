# Diberikan data kehadiran harian dalam bentuk:
# [("Andi", "2024-06-01"), ("Budi", "2024-06-01"), ("Andi", "2024-06-02")]
# Tulis program Python untuk menampilkan jumlah kehadiran masing-masing orang.

data = [("Andi", "2024-06-01"), ("Budi", "2024-06-01"), ("Andi", "2024-06-02")]

def format_absen(data:list):
    new_data = []
    for el in data:
        nama = el[0]
        tgl = el[1]
        ditemukan = False
        for in_el in new_data:
            if in_el['nama'] == nama:
                in_el['tanggal'].append(tgl)
                in_el['jumlah'] += 1
                ditemukan = True
        if not ditemukan:
            new_data.append({'nama': nama, 'tanggal': tgl, 'jumlah': 1})

    print(new_data)

format_absen(data)