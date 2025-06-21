# Buatlah program Python yang menerima input daftar mahasiswa, masing-masing dengan nilai tugas, UTS, dan UAS. Hitung nilai akhir dengan bobot berikut:
# Tugas: 20%
# UTS: 30%
# UAS: 50%
# Tampilkan output berupa daftar nama mahasiswa, nilai akhirnya, dan predikat huruf (A, B, C, D, E).

import json

inputted_data = input("input data (list of json format) : ")
data = json.loads(inputted_data) # convert json to

for i, e in enumerate(data): # i as index, e as element
    print('Calculating : ', e['name'])

    tugas = e['tugas']*20/100
    uts = e['uts']*30/100
    uas = e['uas']*50/100
    nilai_final = tugas + uts + uas
    data[i]['nilai_final'] = nilai_final
    
    if nilai_final < 50:
        data[i]['predikat'] = 'E'
    elif 50 <= nilai_final < 60:
        data[i]['predikat'] = 'D'
    elif 60 <= nilai_final < 70:
        data[i]['predikat'] = 'C'
    elif 70 <= nilai_final < 80:
        data[i]['predikat'] = 'B'
    else:
        data[i]['predikat'] = 'A'

    print('Updating Data : ', data[i])
    
print('Final Data', data)