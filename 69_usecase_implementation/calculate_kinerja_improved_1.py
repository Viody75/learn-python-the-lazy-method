# mengambil input tanpa inisial banyak data
def input_data():
    state = True
    new_data = []
    while state:
        print('- - Entry Data Pegawai - -')
        nama_pegawai = input('Nama :')
        nilai_pegawai = float(input('Nilai :'))
        new_data.append({'nama': nama_pegawai, 'nilai': nilai_pegawai})
        input_lagi = input('Ingin input data lagi? (Y/N)')
        match input_lagi.lower():
            case 'y':
                state = True
            case 'n':
                state = False
            case _:
                print('Input tidak diketahui, sistem anggap input data selesai')
                state = False
    print(new_data)

input_data()