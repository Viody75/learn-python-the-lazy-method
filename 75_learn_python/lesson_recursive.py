def count_down(n: int):
    if n <= 0 :
        return
    print(f'Count A : ' + n*'*')
    count_down(n-1)
    print(f'Count B : ' + n*'*')
    count_down(n-1)
    print(f'Count C : ' + n*'*')

count_down(6)

struktur_folder = {
    "tipe": "folder",
    "nama": "Proyek_Besar",
    "isi": [
        {"tipe": "file", "nama": "dokumen_utama.txt", "ukuran": 100},
        {"tipe": "file", "nama": "gambar_logo.png", "ukuran": 250},
        {
            "tipe": "folder",
            "nama": "src",
            "isi": [
                {"tipe": "file", "nama": "main.py", "ukuran": 50},
                {"tipe": "file", "nama": "utils.py", "ukuran": 25},
            ]
        },
        {
            "tipe": "folder",
            "nama": "aset",
            "isi": [
                {
                    "tipe": "folder",
                    "nama": "ikon",
                    "isi": [
                        {"tipe": "file", "nama": "user.png", "ukuran": 15},
                        {"tipe": "file", "nama": "home.png", "ukuran": 20},
                    ]
                },
                {"tipe": "file", "nama": "suara.mp3", "ukuran": 500}
            ]
        }
    ]
}

def count_folder(folder):
    if folder['tipe'] == 'file':
        return 1
    total = 0
    for item in folder['isi']:
        total += count_folder(item)
    return total

# print("Total file:", count_folder(struktur_folder)) 

# def count_folder(folder):
#     if folder["tipe"] == "file":
#         return 1
#     total = 0
#     for item in folder["isi"]:
#         total += count_folder(item)
#     return total