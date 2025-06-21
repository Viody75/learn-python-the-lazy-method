# Tuliskan program Python yang mensimulasikan antrian pembelian tiket bioskop.
# Maksimal kapasitas: x orang.
# Saat antrean mencapai batas, orang baru ditolak.

max_antri = int(input("Maksimal tiket bioskop (antrian) : "))

def simulate_queue(max : int =0):
    print("Maks. antrian :",max)
    data = []
    for i in range(max):
        nama = input(f'Masukan penonton ke {i+1}:')
        data.append(nama)
        # TODO : Can add handle more data functions here
    print("Data antrian :",data)
    # TODO : Can add handle seat assignment here

simulate_queue(max_antri)