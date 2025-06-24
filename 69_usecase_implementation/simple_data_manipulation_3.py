# Buat program Python yang membaca daftar suara dalam array seperti:
# ["Andi", "Budi", "Andi", "Cici", "Budi", "Budi"]
# Keluarkan hasil kandidat dengan suara terbanyak dan jumlah suaranya.

data = ["Andi", "Budi", "Andi", "Cici", "Budi", "Budi"]

def calculate_data(data: list):
    riwayat = []
    for el in data:
        ditemukan = False
        for in_el in riwayat:
            if in_el['nama'] == el:
                in_el['suara'] += 1
                ditemukan = True
        
        if not ditemukan:
            riwayat.append({'nama': el, 'suara': 1})
    print(riwayat)

    suara_tertinggi = 0
    data_pemenang = {}
    for el in riwayat:
        print('Perbandingan', el['nama'], ':', el['suara']) 
        for in_el in riwayat:
            print('dengan ', in_el['suara']) 
            if suara_tertinggi < in_el['suara']:
                suara_tertinggi = in_el['suara']
                data_pemenang['nama'] = in_el['nama']
    data_pemenang['suara'] = suara_tertinggi
    print('Pemenang Vote adalah',data_pemenang)

calculate_data(data)