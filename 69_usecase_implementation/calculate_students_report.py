data = [("Andi", [80, 90, 75]), ("Budi", [60, 65, 70])]

def hitung_nilai (data:list):
    new_data = []
    for el in data:
        nilais = 0
        for in_el in el[1]:
            nilais += in_el
        nilai_rata = round(nilais / len(el[1]), 1) 
        predikat = ''
        if nilai_rata < 55:
            predikat = 'D'
        elif nilai_rata < 70:
            predikat = 'C'
        elif nilai_rata < 85:
            predikat = 'B'
        elif nilai_rata >= 85:
            predikat = 'A'
        new_data.append({'nama': el[0], 'nilai': el[1], 'rata-rata': nilai_rata, 'predikat': predikat})
    print(new_data)
    return new_data
    

hitung_nilai(data)