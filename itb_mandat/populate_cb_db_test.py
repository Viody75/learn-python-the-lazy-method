# generate_seed_auto.py
# Script otomatis untuk membuat file seeding Couchbase dalam format INSERT INTO

import random

# --- Konfigurasi dasar ---
bucket_name = "test_bucket"
output_file = "seed_data_generated.txt"
total_users = 100  # ubah jumlah user di sini

# --- Daftar role yang mungkin ---
roles = ["admin", "user", "editor", "viewer"]

# --- Generate data user ---
values = []
for i in range(1, total_users + 1):
    user_id = f"user_{i:03d}"
    name = f"User {i:03d}"
    email = f"user{i:03d}@example.com"
    role = random.choice(roles)
    values.append(
        f"(\"{user_id}\", {{ \"id\": \"{user_id}\", \"name\": \"{name}\", \"email\": \"{email}\", \"role\": \"{role}\" }})"
    )

# --- Susun query Couchbase ---
insert_query = f"INSERT INTO `{bucket_name}` (KEY, VALUE)\nVALUES \n" + ",\n".join(values) + ";"

# --- Simpan ke file .txt ---
with open(output_file, "w") as f:
    f.write(insert_query)

print(f"✅ File '{output_file}' berhasil dibuat dengan {total_users} user data.")
