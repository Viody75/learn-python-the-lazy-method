# Tulis fungsi Python deteksi_login_beruntun(data) yang mengembalikan nama-nama pengguna yang melakukan login lebih dari sekali dalam selang waktu ≤ 5 menit.

data = [("andi", "10:00"), ("budi", "10:05"), ("andi", "10:05"), ("cici", "10:15")]

def deteksi_login_beruntun(data: list):
    riwayat = []
    for el in data :
        jam, menit =  el[1].split(':') # Penggunaan Split String

        ditemukan = False
        for in_el in riwayat:
            if in_el['nama'] == el[0]:
             in_jam,in_menit = in_el['waktu_login'].split(':')
             if in_jam == jam and abs(int(in_menit) - int(menit)) <= 5: # Penggunaan fungsi Absolute untuk mengubah bilangan selalu positif
                print(in_el['nama'], 'Sudah login')
             ditemukan = True
        
        if not ditemukan:
            riwayat.append({'nama': el[0], 'waktu_login': el[1]})

deteksi_login_beruntun(data)