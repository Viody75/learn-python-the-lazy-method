# Diberikan daftar transaksi berisi (tanggal, nominal)
# Tuliskan program untuk menjumlahkan total transaksi per tanggal, dan cetak dalam format:
# 2024-01-01: 30000
# 2024-01-02: 50000

data = [{'tanggal': '2025-01-01', 'nominal':'20000'},
        {'tanggal': '2025-01-01', 'nominal':'10000'},
        {'tanggal': '2025-01-01', 'nominal':'10000'},
        {'tanggal': '2025-01-02', 'nominal':'50000'},
        {'tanggal': '2025-01-02', 'nominal':'20000'},
        {'tanggal': '2025-01-03', 'nominal':'50000'},
        {'tanggal': '2025-01-04', 'nominal':'10000'},
        {'tanggal': '2025-01-04', 'nominal':'10000'},
        {'tanggal': '2025-01-05', 'nominal':'10000'},]

def convert_data(data: list):
    riwayat = []
    for el in data:
        print('Converting:',el['tanggal'])
        # tahun, month, day = el['tanggal'].split('-')
        ditemukan = False
        for in_el in riwayat:
            if in_el['tanggal'] in el['tanggal']:
                total_now = int(in_el['total_nominal']) + int(el['nominal'])
                in_el['total_nominal'] = total_now
                ditemukan = True
        
        if not ditemukan:
            riwayat.append({'tanggal': el['tanggal'], 'total_nominal': el['nominal']} )
    return riwayat

def print_c_data(data: list):
    print('Print Output')
    for el in data:
        print(el['tanggal'],':',el['total_nominal'])

converted_data = convert_data(data)
print_c_data(converted_data)
