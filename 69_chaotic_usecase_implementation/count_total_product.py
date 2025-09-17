data = [("Sabun", 3), ("Sikat", 1), ("Sabun", 2), ("Shampo", 5)]

def count_item(data:list):
    new_data = []
    for el in data:
        ditemukan = False
        for in_el in new_data: # Pengecekan pada data lama pada terbaru, Apakah nama sudah ada di data terbaru
            if in_el['nama'] == el[0]: 
                in_el['total'] += el[1]
                ditemukan = True # Set true jika ada
                break
        
        if not ditemukan: # Jika tidak ada yg sama maka tambah data terbaru
            new_data.append({'nama': el[0], 'total': el[1]})
    print(new_data)

count_item(data)
