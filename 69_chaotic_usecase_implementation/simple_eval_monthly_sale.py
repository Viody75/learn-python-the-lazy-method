# Tulis program untuk:
# Menjumlahkan total pembelian per bulan
# Menentukan bulan dengan pengeluaran tertinggi
# dengan data yg diberikan

data = [("Januari", 300_000), ("Februari", 250_000), ("Januari", 200_000), ("Maret", 100_000), ("Februari", 350_000)]

def check_sale_monthly(data:list):
    riwayat = []    
    nilai_tertinggi = 0
    bulan_tertinggi = ''

    for el in data: # Check Duplikasi & tambah total jika ada
        total = int(str(el[1]).replace('_','')) 

        ditemukan = False
        for in_el in riwayat:
            if in_el['bulan'] == el[0]:
                in_el['total'] += total
                ditemukan = True
        
        if not ditemukan :
            riwayat.append({'bulan': el[0], 'total': total})
    
    for el in riwayat: # Check tertinggi total dan bulan
        if nilai_tertinggi < el['total']:
            nilai_tertinggi = el['total']
            bulan_tertinggi = el['bulan']
    
    print('Data', riwayat)
    print('Teringgi', nilai_tertinggi, 'di', bulan_tertinggi)

check_sale_monthly(data)


