# nama file: populate_db.py

import random
from faker import Faker
import datetime

# Inisialisasi Faker untuk data Indonesia
fake = Faker('id_ID')

# --- PENGATURAN JUMLAH DATA ---
# Anda bisa mengubah angka-angka ini sesuai kebutuhan
JUMLAH_MAHASISWA = 300
JUMLAH_DOSEN = 35
JUMLAH_MATA_KULIAH_PER_PRODI = 15
JUMLAH_KELAS_PER_MK = 2
JUMLAH_MK_DIAMBIL_MAHASISWA = 6 # Rata-rata KRS per mahasiswa

# --- DATA MASTER ---
fakultas_data = [
    ('Sekolah Teknik Elektro dan Informatika', 'STEI'),
    ('Fakultas Teknologi Industri', 'FTI'),
    ('Fakultas Teknik Mesin dan Dirgantara', 'FTMD'),
    ('Sekolah Bisnis dan Manajemen', 'SBM')
]

prodi_data = {
    'STEI': [('135', 'Teknik Informatika', 'S1'), ('182', 'Teknik Elektro', 'S1'), ('181', 'Sistem dan Teknologi Informasi', 'S1')],
    'FTI': [('130', 'Teknik Kimia', 'S1'), ('134', 'Teknik Fisika', 'S1')],
    'FTMD': [('131', 'Teknik Mesin', 'S1'), ('136', 'Teknik Dirgantara', 'S1')],
    'SBM': [('190', 'Manajemen', 'S1'), ('192', 'Kewirausahaan', 'S1')]
}

tahun_kurikulum = 2023
tahun_semester, nama_semester = 2025, 'Ganjil'

# --- FUNGSI UNTUK GENERATE DATA ---

def generate_data():
    sql_statements = []

    # 1. Fakultas & Prodi
    sql_statements.append("-- 1. FAKULTAS & PROGRAM STUDI\n")
    for nama, singkatan in fakultas_data:
        sql_statements.append(f"INSERT INTO fakultas (nama, singkatan) VALUES ('{nama}', '{singkatan}');")
    
    prodi_list = []
    for singkatan_fakultas, daftar_prodi in prodi_data.items():
        nama_fakultas = [f[0] for f in fakultas_data if f[1] == singkatan_fakultas][0]
        for kode_prodi, nama_prodi, jenjang in daftar_prodi:
            sql_statements.append(f"INSERT INTO program_studi (nama, jenjang, nama_fakultas) VALUES ('{nama_prodi}', '{jenjang}', '{nama_fakultas}');")
            prodi_list.append({'kode': kode_prodi, 'nama': nama_prodi, 'fakultas': singkatan_fakultas})
            
    # 2. Akun, Mahasiswa, Dosen
    sql_statements.append("\n-- 2. AKUN, MAHASISWA, DOSEN\n")
    mahasiswa_list = []
    for i in range(JUMLAH_MAHASISWA):
        prodi = random.choice(prodi_list)
        nim = int(f"{prodi['kode']}23{i+1:03}")
        nama = fake.name()
        email = f"{nim}@mahasiswa.itb.ac.id"
        
        sql_statements.append(f"INSERT INTO akun (email, peran, hash_password) VALUES ('{email}', 'mahasiswa', 'pbkdf2:sha256:...');")
        sql_statements.append(f"INSERT INTO mahasiswa (nim, email, nama_lengkap, nama_prodi) VALUES ({nim}, '{email}', '{nama.replace('\'', '')}', '{prodi['nama']}');")
        mahasiswa_list.append({'nim': nim, 'prodi': prodi['nama']})
        
    dosen_list = []
    for i in range(JUMLAH_DOSEN):
        fakultas_singkatan = random.choice(list(prodi_data.keys()))
        nama_fakultas = [f[0] for f in fakultas_data if f[1] == fakultas_singkatan][0]
        nama = fake.name()
        email = f"{nama.lower().split()[0]}{i+1}@itb.ac.id"
        nidn = int(f"10{i+1:08}")
        
        sql_statements.append(f"INSERT INTO akun (email, peran, hash_password) VALUES ('{email}', 'dosen', 'pbkdf2:sha256:...');")
        sql_statements.append(f"INSERT INTO dosen (nidn, email, nip, nama_lengkap, jabatan, nama_fakultas) VALUES ({nidn}, '{email}', '19{random.randint(70,90)}{random.randint(1,12):02}100{i}', '{nama.replace('\'', '')}', 'Lektor', '{nama_fakultas}');")
        dosen_list.append({'nidn': nidn, 'fakultas': fakultas_singkatan})
        
    # 3. Dosen Wali
    sql_statements.append("\n-- 3. DOSEN WALI\n")
    for mhs in mahasiswa_list:
        # Pilih dosen wali dari fakultas yang sama
        dosen_prodi = [d for d in dosen_list if d['fakultas'] == [p['fakultas'] for p in prodi_list if p['nama'] == mhs['prodi']][0]]
        if dosen_prodi:
            dosen_wali = random.choice(dosen_prodi)
            sql_statements.append(f"INSERT INTO dosen_wali (nidn, nim) VALUES ({dosen_wali['nidn']}, {mhs['nim']});")

    # 4. Kurikulum & Mata Kuliah
    sql_statements.append("\n-- 4. KURIKULUM & MATA KULIAH\n")
    sql_statements.append(f"INSERT INTO kurikulum (tahun, bahan_kajian, capaian) VALUES ({tahun_kurikulum}, 'Bahan kajian untuk kurikulum {tahun_kurikulum}', 'Capaian pembelajaran untuk kurikulum {tahun_kurikulum}');")
    
    matkul_list = []
    for prodi in prodi_list:
        for i in range(JUMLAH_MATA_KULIAH_PER_PRODI):
            kode_mk = f"{prodi['kode'].replace('1','',1)}{random.randint(1,4)}{i+1:02}"
            nama_mk = f"Mata Kuliah {prodi['kode']} {i+1}"
            sks = random.choice([2, 3, 4])
            sql_statements.append(f"INSERT INTO mata_kuliah (kode_mk, nama_mk, deskripsi_mk, sks, tahun_kurikulum) VALUES ('{kode_mk}', '{nama_mk}', 'Deskripsi untuk {nama_mk}', {sks}, {tahun_kurikulum});")
            matkul_list.append({'kode_mk': kode_mk, 'prodi_kode': prodi['kode']})
            
    # 5. Semester & Kelas
    sql_statements.append("\n-- 5. SEMESTER & KELAS MATA KULIAH\n")
    sql_statements.append(f"INSERT INTO semester (tahun, semester, waktu_mulai_pengisian_nilai, waktu_selesai_pengisisan_nilai) VALUES ({tahun_semester}, '{nama_semester}', '{tahun_semester}-12-20', '{tahun_semester+1}-01-20');")
    
    kelas_list = []
    for mk in matkul_list:
        for i in range(1, JUMLAH_KELAS_PER_MK + 1):
            nomor_kelas = f"{i:02}"
            sql_statements.append(f"INSERT INTO kelas_mata_kuliah (nomor_kelas, kode_mk, tahun, semester, kapasitas) VALUES ('{nomor_kelas}', '{mk['kode_mk']}', {tahun_semester}, '{nama_semester}', '100');")
            kelas_list.append({'nomor_kelas': nomor_kelas, 'kode_mk': mk['kode_mk'], 'prodi_kode': mk['prodi_kode']})

    # 6. Pengambilan Rencana Studi (KRS)
    sql_statements.append("\n-- 6. PENGAMBILAN RENCANA STUDI (KRS)\n")
    for mhs in mahasiswa_list:
        prodi_mhs = [p for p in prodi_list if p['nama'] == mhs['prodi']][0]
        # Ambil MK dari prodinya sendiri
        krs_matkul_pool = [k for k in kelas_list if k['prodi_kode'] == prodi_mhs['kode']]
        if len(krs_matkul_pool) > JUMLAH_MK_DIAMBIL_MAHASISWA:
            krs_diambil = random.sample(krs_matkul_pool, JUMLAH_MK_DIAMBIL_MAHASISWA)
            for krs in krs_diambil:
                sql_statements.append(f"INSERT INTO mengambil_rencana_studi (nim, nomor_kelas, kode_mk, tahun, semester, tanggal_persetujuan, status, indeks_nilai) VALUES ({mhs['nim']}, '{krs['nomor_kelas']}', '{krs['kode_mk']}', {tahun_semester}, '{nama_semester}', '{tahun_semester}-08-25', 'Disetujui', '{random.choice(['A', 'AB', 'B', 'BC', 'C', 'D', 'E'])}');")

    return "\n".join(sql_statements)

# --- TULIS KE FILE ---
if __name__ == "__main__":
    semua_data_sql = generate_data()
    nama_file_output = "data_populasi.sql"
    with open(nama_file_output, 'w') as f:
        f.write(semua_data_sql)
    print(f"✅ Berhasil! Data populasi telah dibuat di file '{nama_file_output}'")