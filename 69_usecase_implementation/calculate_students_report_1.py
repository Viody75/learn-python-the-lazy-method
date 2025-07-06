# Hitung nilai akhir dengan bobot:
# MTK: 40%
# B. Indonesia: 30%
# IPA: 30%
# Keluarkan nama siswa dan nilai akhirnya.

data = [("Ani", {"MTK": 80, "B.Indonesia": 71, "IPA": 92}),
        ("Adi", {"MTK": 70, "B.Indonesia": 66, "IPA": 80}),
        ("Budi", {"MTK": 45, "B.Indonesia": 73, "IPA": 82})]

def hitung_hilai_dan_bobot(data:list):
    data_baru = []
    for el in data:
        nilai_akhir = round(el[1]['MTK'] * 0.4 + el[1]['B.Indonesia'] * 0.3 + el[1]['IPA'] * 0.3, 2) 
        el[1]['MTK']
        data_baru.append({'nama': el[0], 'nilai_akhir': nilai_akhir})
    print(data_baru)

hitung_hilai_dan_bobot(data)