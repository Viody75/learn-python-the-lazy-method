data = [
    {'nama':'vio', 'total': 90},
    {'nama':'budi', 'total': 60},
    ]

for e in data :
    if e['total'] > 70 :
        e['target'] = 'tercapai'
    else :
        e['target'] = 'tidak tercapai'

print(data)