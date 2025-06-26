# Simulasikan sistem parkir dengan:
# Maksimum kapasitas 3 kendaraan
# Kendaraan masuk dicatat sebagai string (nomor polisi)
# Kendaraan keluar dihapus dari stack
# Tulis fungsi masuk(nopol) dan keluar(nopol).

data = []

def masuk(nopol: str):
    if len(data) < 3:
        data.append(nopol)

def keluar(nopol: str):
    for el in data:
        if el == nopol:
            data.remove(nopol)

masuk('123')
masuk('234')
masuk('345')
masuk('345')

keluar('234')

print(data)