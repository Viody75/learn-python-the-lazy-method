def waktu_ke_menit(waktu_str):
    jam, menit = waktu_str.split(":")
    return int(jam) * 60 + int(menit)

def ada_transaksi_ganda(transaksi_list):
    riwayat = {}

    for nama, waktu in transaksi_list:
        menit = waktu_ke_menit(waktu)
        
        if nama in riwayat:
            # Cek apakah beda waktunya < 15 menit
            for waktu_lalu in riwayat[nama]:
                if abs(menit - waktu_lalu) < 15:
                    return True
            riwayat[nama].append(menit)
        else:
            riwayat[nama] = [menit]

    print('Riwayat : ' , riwayat)
    return False

transaksi = [("Andi", "09:00"), ("Budi", "09:15"), ("Andi", "09:40"), ("Cici", "09:40")]

print(ada_transaksi_ganda(transaksi)) 
