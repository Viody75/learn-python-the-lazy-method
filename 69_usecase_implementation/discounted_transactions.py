# Buat program yang membaca list transaksi pembelian (item dan jumlah), lalu menghitung total harga berdasarkan daftar harga yang sudah ditentukan.
# Tambahkan logika diskon 10% jika total belanja > 500.000.

def after_discount(price:int = 0):
    discounted_price = price - (price * 0.1)
    return discounted_price

# Asumsikan
data_transaction = [
    {"name":"item 1", "price": 100000},
    {"name":"item 2", "price": 200000},
    {"name":"item 3", "price": 100000},
    ]

total_price = 0
for item in data_transaction:
    total_price += item['price']

if total_price >= 500000:
    total_price = after_discount(total_price)

print(total_price)