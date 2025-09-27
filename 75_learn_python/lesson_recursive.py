def count_down(n: int):
    if n <= 0 :
        return
    print(f'Count A : ' + n*'*')
    count_down(n-1)
    print(f'Count B : ' + n*'*')
    count_down(n-1)
    print(f'Count C : ' + n*'*')

# count_down(6)

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

# list_kata = ["Hello", "World", "From", "Python"]
# print(list_kata[1:])
# print(list_kata[:1])

def question_1(words: str):
    if len(words) == 0:
        return
    tobe_checked = words[0]
    if tobe_checked.isdigit():
        print(f"{tobe_checked} adalah angka")
        return
    question_1(words[1:])

# question_1('Saya ingin menjabat 3 periode')

def recursive_sqrt(n: int):
    assert n > 0, "Tidak boleh kurang dari sama dengan 0"
    # if n < 2:
    #     return n
    # return recursive_sqrt(n // 2)
    
# print(recursive_sqrt(16))  # Output: 4

list_bilangan = [1, 2, 3, 4, 5]

def question_3(list : list, x : int ):
    
    if len(list) == 0:
        return 0
    new_list = list[1:]
    if list[0] == x:
        print('Yes')
        return question_3(new_list, x )
    else:
        print('No')
        return list[0] + question_3(new_list, x )

# question_3(list_bilangan, 15)
# print(question_3(list_bilangan, 16))