import datetime
import random
import bcrypt
import json
import time
from faker import Faker

# ----------------------------------------------------------------------
# ⚙️ PENGATURAN - SESUAIKAN BAGIAN INI
# ----------------------------------------------------------------------
CB_BUCKET = "akademik"            # Nama bucket yang sudah Anda buat
OUTPUT_FILE = "couchbase_seed.txt" # Nama file output
# ----------------------------------------------------------------------

# Inisialisasi Faker untuk data Indonesia
fake = Faker('id_ID')

# --- Helper untuk Hashing Password ---
def hash_password(password):
    """Meng-hash password menggunakan bcrypt."""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

# --- Helper untuk Setup Scopes & Collections ---
def setup_collections(file_handle, bucket_name):
    """Menulis perintah N1QL untuk membuat Scopes dan Collections."""
    print("\n--- 🏗️ Menulis Kueri N1QL untuk Setup Scopes & Collections ---")
    file_handle.write(f"\n/* --- 1. MEMBUAT SCOPES & COLLECTIONS (IF ERROR Execute 1 by 1 just for this batch)--- */\n\n")

    scopes_collections = {
        "mahasiswa": ["profile", "krs", "keuangan"],
        "dosen": ["profile"],
        "akademik": ["fakultas", "program_studi", "kurikulum", "mata_kuliah", "kelas"],
        "shared_resources": ["ruangan", "semester"],
        "utility": ["log_aktivitas"]
    }
    
    # Buat Scopes
    for scope_name in scopes_collections.keys():
        query = f'CREATE SCOPE `{bucket_name}`.`{scope_name}` IF NOT EXISTS;'
        file_handle.write(query + "\n")
        
    # Buat Collections
    for scope_name, collections in scopes_collections.items():
        for collection_name in collections:
            query = f'CREATE COLLECTION `{bucket_name}`.`{scope_name}`.`{collection_name}` IF NOT EXISTS;'
            file_handle.write(query + "\n")
            
    print(f"  [+] Kueri untuk {len(scopes_collections)} Scopes & {sum(len(v) for v in scopes_collections.values())} Collections ditulis.")

# --- Fungsi Seeder Utama ---
# Setiap fungsi seeder sekarang menerima file_handle dan bucket_name
# dan menulis perintah INSERT N1QL ke file.

def write_insert_query(file_handle, bucket, scope, collection, doc_id, doc_body):
    """Helper untuk menulis satu perintah INSERT N1QL."""
    # Ubah dict Python ke string JSON
    json_value = json.dumps(doc_body, ensure_ascii=False)
    # Buat kueri N1QL
    query = f'INSERT INTO `{bucket}`.`{scope}`.`{collection}` (KEY, VALUE) VALUES ("{doc_id}", {json_value});'
    file_handle.write(query + "\n")

def seed_shared_resources(file_handle, bucket_name):
    """Tulis N1QL untuk data shared_resources & akademik (master)."""
    print("\n---  Menulis N1QL: shared_resources & akademik (master) ---")
    
    file_handle.write(f"\n/* --- 2. SEEDING DATA MASTER (FAKULTAS, PRODI, MK, DLL) --- */\n\n")
    
    data_store = { "fakultas": [], "prodi": [], "kurikulum": [], "matkul": [], "ruangan": [], "semester": [] }

    # 1. Fakultas
    fakultas_list = [
        {"nama": "Fakultas Teknik", "singkatan": "FT"},
        {"nama": "Fakultas Ekonomi dan Bisnis", "singkatan": "FEB"},
        {"nama": "Fakultas Ilmu Komputer", "singkatan": "FIK"},
    ]
    for f in fakultas_list:
        doc_id = f"fakultas::{f['singkatan'].lower()}"
        write_insert_query(file_handle, bucket_name, "akademik", "fakultas", doc_id, f)
        data_store["fakultas"].append(f['nama'])
    print(f"  [+] {len(fakultas_list)} Fakultas INSERTs ditulis.")

    # 2. Program Studi
    prodi_list = [
        {"nama": "Teknik Informatika", "jenjang": "S1", "fakultas_nama": "Fakultas Ilmu Komputer"},
        {"nama": "Sistem Informasi", "jenjang": "S1", "fakultas_nama": "Fakultas Ilmu Komputer"},
        {"nama": "Manajemen", "jenjang": "S1", "fakultas_nama": "Fakultas Ekonomi dan Bisnis"},
        {"nama": "Teknik Sipil", "jenjang": "S1", "fakultas_nama": "Fakultas Teknik"},
    ]
    for p in prodi_list:
        doc_id = f"prodi::{p['nama'].lower().replace(' ', '_')}"
        write_insert_query(file_handle, bucket_name, "akademik", "program_studi", doc_id, p)
        data_store["prodi"].append(p['nama'])
    print(f"  [+] {len(prodi_list)} Program Studi INSERTs ditulis.")
    
    # 3. Kurikulum
    kurikulum_tahun = 2020
    doc_id = f"kurikulum::{kurikulum_tahun}"
    kurikulum_doc = {
        "tahun": kurikulum_tahun, "bahan_kajian": "...", "capaian": "...", 
        "metode_pembelajaran": "...", "modalitas": "...", "jenis_nilai": "...",
        "metode_penilaian": "...", "catatan": "Kurikulum 2020"
    }
    write_insert_query(file_handle, bucket_name, "akademik", "kurikulum", doc_id, kurikulum_doc)
    data_store["kurikulum"].append(kurikulum_tahun)
    print(f"  [+] 1 Kurikulum INSERT ditulis.")

    # 4. Mata Kuliah
    matkul_list = [
        {"kode_mk": "IF101", "nama_mk": "Dasar Pemrograman", "sks": 4, "tahun_kurikulum": 2020},
        {"kode_mk": "IF102", "nama_mk": "Struktur Data", "sks": 3, "tahun_kurikulum": 2020},
        {"kode_mk": "SI101", "nama_mk": "Analisis Proses Bisnis", "sks": 3, "tahun_kurikulum": 2020},
        {"kode_mk": "MN101", "nama_mk": "Pengantar Manajemen", "sks": 3, "tahun_kurikulum": 2020},
        {"kode_mk": "TS101", "nama_mk": "Mekanika Tanah", "sks": 4, "tahun_kurikulum": 2020},
        {"kode_mk": "UM101", "nama_mk": "Pendidikan Pancasila", "sks": 2, "tahun_kurikulum": 2020},
    ]
    for mk in matkul_list:
        doc_id = f"matkul::{mk['kode_mk']}"
        write_insert_query(file_handle, bucket_name, "akademik", "mata_kuliah", doc_id, mk)
        data_store["matkul"].append(mk)
    print(f"  [+] {len(matkul_list)} Mata Kuliah INSERTs ditulis.")

    # 5. Ruangan
    for i in range(1, 6):
        kode = 100 + i
        ruangan = {
            "kode_ruangan": kode, "nama_ruangan": f"Ruang R.{kode}",
            "kapasitas": random.choice([30, 50, 100]), "lokasi": "Gedung A",
            "daerah": "Kampus Pusat", "gedung": "Gedung A", "lantai": i, "status": "Aktif"
        }
        doc_id = f"ruangan::{kode}"
        write_insert_query(file_handle, bucket_name, "shared_resources", "ruangan", doc_id, ruangan)
        data_store["ruangan"].append(ruangan)
    print(f"  [+] 5 Ruangan INSERTs ditulis.")

    # 6. Semester (Saat ini)
    semester_aktif = {"tahun": 2024, "semester": "ganjil"}
    doc_id = f"semester::{semester_aktif['tahun']}_{semester_aktif['semester']}"
    semester_doc = {
        **semester_aktif,
        "waktu_mulai_pengisian_nilai": "2024-12-01",
        "waktu_selesai_pengisian_nilai": "2024-12-15"
    }
    write_insert_query(file_handle, bucket_name, "shared_resources", "semester", doc_id, semester_doc)
    data_store["semester"].append(semester_aktif)
    print(f"  [+] 1 Semester Aktif INSERT ditulis.")
    
    return data_store

def seed_dosen(file_handle, bucket_name, list_fakultas, total=10):
    """Tulis N1QL untuk Dosen."""
    print(f"\n--- 👨‍🏫 Menulis N1QL: Dosen ({total} data) ---")
    file_handle.write(f"\n/* --- 3. SEEDING DATA DOSEN --- */\n\n")
    
    dosen_list = []
    for i in range(total):
        nidn = int(f"11{i:06d}")
        nama = fake.name()
        email = f"dosen.{nidn}@kampus.ac.id"
        
        dosen_doc = {
            "_type": "dosen", "nidn": nidn, "email": email,
            "nip": fake.numerify(text="##################"), "nama_lengkap": nama,
            "golongan": random.choice(["III/c", "III/d", "IV/a"]), "pangkat": "Lektor",
            "jabatan": "Dosen", "akademik": "S2",
            "fakultas_nama": random.choice(list_fakultas),
            "auth": { "peran": "dosen", "hash_password": hash_password("dosen123") },
            "telepon": [fake.phone_number()]
        }
        
        doc_id = f"dosen::{nidn}"
        write_insert_query(file_handle, bucket_name, "dosen", "profile", doc_id, dosen_doc)
        dosen_list.append(dosen_doc)
        
    print(f"  [+] {total} Dosen INSERTs ditulis.")
    return dosen_list

def seed_mahasiswa(file_handle, bucket_name, list_prodi, list_dosen, total=50):
    """Tulis N1QL untuk Mahasiswa."""
    print(f"\n--- 👩‍🎓 Menulis N1QL: Mahasiswa ({total} data) ---")
    file_handle.write(f"\n/* --- 4. SEEDING DATA MAHASISWA --- */\n\n")
    
    mahasiswa_list = []
    for i in range(total):
        nim = int(f"13521{i:03d}")
        nama = fake.name()
        email = f"mhs.{nim}@kampus.ac.id"
        
        mahasiswa_doc = {
            "_type": "mahasiswa", "nim": nim, "email": email,
            "nama_lengkap": nama, "dokumen_transkrip": "Belum ada",
            "prodi_nama": random.choice(list_prodi),
            "dosen_wali_nidn": random.choice(list_dosen)['nidn'],
            "auth": { "peran": "mahasiswa", "hash_password": hash_password("mahasiswa123") },
            "telepon": [fake.phone_number()],
            "yudisium": None
        }
        
        if i < total * 0.1: # 10% yudisium
            mahasiswa_doc["yudisium"] = { "tahun": 2024, "bulan": "Maret" }

        doc_id = f"mhs::{nim}"
        write_insert_query(file_handle, bucket_name, "mahasiswa", "profile", doc_id, mahasiswa_doc)
        mahasiswa_list.append(mahasiswa_doc)
        
    print(f"  [+] {total} Mahasiswa INSERTs ditulis.")
    return mahasiswa_list

def seed_akademik_data(file_handle, bucket_name, list_matkul, list_ruangan, list_semester):
    """Tulis N1QL untuk Kelas dan Jadwalnya."""
    print("\n--- 📚 Menulis N1QL: Kelas dan Jadwal ---")
    file_handle.write(f"\n/* --- 5. SEEDING DATA KELAS & JADWAL --- */\n\n")
    
    semester_aktif = list_semester[0]
    kelas_list = []
    
    for mk in list_matkul:
        for kelas_nama in ["A", "B"]:
            ruangan = random.choice(list_ruangan)
            hari = random.choice(["Senin", "Selasa", "Rabu", "Kamis", "Jumat"])
            jam_mulai = random.choice(["08:00", "10:00", "13:00"])
            
            kelas_doc = {
                "nomor_kelas": kelas_nama, "kode_mk": mk['kode_mk'],
                "tahun": semester_aktif['tahun'], "semester": semester_aktif['semester'],
                "kapasitas": ruangan['kapasitas'],
                "jadwal": [
                    {
                        "jenis_kegiatan": "Kuliah", "hari": hari,
                        "jam_mulai": jam_mulai, "jam_selesai": f"{int(jam_mulai[:2]) + 2}:00",
                        "kode_ruangan": ruangan['kode_ruangan']
                    }
                ]
            }
            
            doc_id = f"kelas::{mk['kode_mk']}::{kelas_nama}::{semester_aktif['tahun']}::{semester_aktif['semester']}"
            write_insert_query(file_handle, bucket_name, "akademik", "kelas", doc_id, kelas_doc)
            kelas_list.append(kelas_doc)
            
    print(f"  [+] {len(kelas_list)} Kelas INSERTs ditulis.")
    return kelas_list

def seed_mahasiswa_data(file_handle, bucket_name, list_mahasiswa, list_kelas):
    """Tulis N1QL untuk KRS dan Keuangan Mahasiswa."""
    print("\n--- 💳 Menulis N1QL: KRS dan Keuangan Mahasiswa ---")
    file_handle.write(f"\n/* --- 6. SEEDING DATA KRS & KEUANGAN MAHASISWA --- */\n\n")
    
    semester_aktif = list_kelas[0]
    tahun = semester_aktif['tahun']
    semester = semester_aktif['semester']
    
    krs_count = 0
    keuangan_count = 0
    
    for mhs in list_mahasiswa:
        nim = mhs['nim']
        
        # 1. Seed KRS
        jumlah_mk = random.randint(4, 6)
        kelas_diambil = random.sample(list_kelas, jumlah_mk)
        
        krs_doc = {
            "nim": nim, "tahun": tahun, "semester": semester,
            "tanggal_waktu_pengisian": fake.iso8601(),
            "mata_kuliah": [
                {
                    "kode_mk": k['kode_mk'], "nomor_kelas": k['nomor_kelas'],
                    "indeks_nilai": random.choice(["A", "B", "C", "D", "E", None])
                } for k in kelas_diambil
            ]
        }
        doc_id_krs = f"krs::{nim}::{tahun}::{semester}"
        write_insert_query(file_handle, bucket_name, "mahasiswa", "krs", doc_id_krs, krs_doc)
        krs_count += 1
        
        # 2. Seed Keuangan
        tagihan = 5000000
        status_bayar = random.choice([True, False])
        
        keuangan_doc = {
            "nim": nim, "tahun": tahun, "semester": semester,
            "tagihan": str(tagihan),
            "pembayaran": str(tagihan) if status_bayar else "0",
            "tanggal_batas_pembayaran": f"{tahun}-08-15"
        }
        doc_id_keuangan = f"keuangan::{nim}::{tahun}::{semester}"
        write_insert_query(file_handle, bucket_name, "mahasiswa", "keuangan", doc_id_keuangan, keuangan_doc)
        keuangan_count += 1
        
    print(f"  [+] {krs_count} KRS INSERTs ditulis.")
    print(f"  [+] {keuangan_count} Keuangan INSERTs ditulis.")

# --- Fungsi Eksekusi Utama ---
def main():
    try:
        # Buka file output untuk ditulis
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            f.write(f"-- Skrip Seeding N1QL untuk Bucket: {CB_BUCKET}\n")
            f.write(f"-- Dibuat pada: {datetime.datetime.now().isoformat()}\n")
            f.write("-- PENTING: Jalankan kueri ini di Couchbase Query Editor.\n")
            f.write("-- Pastikan Anda sudah membuat Bucket '{CB_BUCKET}' terlebih dahulu.\n")

            print(f"✅ Mulai menulis kueri N1QL ke file '{OUTPUT_FILE}'...")

            # 1. Setup struktur
            setup_collections(f, CB_BUCKET)

            # 2. Seed Master Data
            shared_data = seed_shared_resources(f, CB_BUCKET)

            # 3. Seed Dosen
            dosen_data = seed_dosen(f, CB_BUCKET, shared_data['fakultas'], total=15)
            
            # 4. Seed Mahasiswa
            mahasiswa_data = seed_mahasiswa(f, CB_BUCKET, shared_data['prodi'], dosen_data, total=100)
            
            # 5. Seed Kelas
            kelas_data = seed_akademik_data(f, CB_BUCKET, shared_data['matkul'], shared_data['ruangan'], shared_data['semester'])
            
            # 6. Seed Data Transaksional Mahasiswa
            seed_mahasiswa_data(f, CB_BUCKET, mahasiswa_data, kelas_data)
            
            print(f"\n🎉 --- Penulisan N1QL Selesai. File '{OUTPUT_FILE}' telah dibuat. --- 🎉")

    except Exception as e:
        print(f"\n❌ GAGAL menulis file: {e}")

if __name__ == "__main__":
    main()