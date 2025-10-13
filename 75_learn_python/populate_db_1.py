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
JUMLAH_RUANGAN = 20
JUMLAH_MATA_KULIAH_PER_PRODI = 10
JUMLAH_KELAS_PER_MK = 2
JUMLAH_MK_DIAMBIL_MAHASISWA = 6
JUMLAH_PERTEMUAN_PER_KELAS = 14 # Jumlah minggu dalam 1 semester
JUMLAH_BIMBINGAN_PER_MHS = 3

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
tanggal_mulai_semester = datetime.date(tahun_semester, 8, 25)

# --- FUNGSI UNTUK GENERATE DATA ---

def generate_data():
    sql_statements = []
    
    # Helper function to escape single quotes
    def escape_str(s):
        return s.replace("'", "''")

    # 1. Fakultas & Prodi
    sql_statements.append("-- 1. FAKULTAS & PROGRAM STUDI\n")
    # ... (code for fakultas and prodi remains the same)
    for nama, singkatan in fakultas_data:
        sql_statements.append(f"INSERT INTO fakultas (nama, singkatan) VALUES ('{escape_str(nama)}', '{singkatan}');")
    
    prodi_list = []
    for singkatan_fakultas, daftar_prodi in prodi_data.items():
        nama_fakultas = [f[0] for f in fakultas_data if f[1] == singkatan_fakultas][0]
        for kode_prodi, nama_prodi, jenjang in daftar_prodi:
            sql_statements.append(f"INSERT INTO program_studi (nama, jenjang, nama_fakultas) VALUES ('{escape_str(nama_prodi)}', '{jenjang}', '{escape_str(nama_fakultas)}');")
            prodi_list.append({'kode': kode_prodi, 'nama': nama_prodi, 'fakultas': singkatan_fakultas})


    # 2. Akun, Mahasiswa, Dosen
    sql_statements.append("\n-- 2. AKUN, MAHASISWA, DOSEN\n")
    # ... (code for akun, mahasiswa, dosen remains the same)
    mahasiswa_list = []
    for i in range(JUMLAH_MAHASISWA):
        prodi = random.choice(prodi_list)
        nim = int(f"{prodi['kode']}23{i+1:03}")
        nama = fake.name()
        email = f"{nim}@mahasiswa.itb.ac.id"
        
        sql_statements.append(f"INSERT INTO akun (email, peran, hash_password) VALUES ('{email}', 'mahasiswa', 'pbkdf2:sha256:...');")
        sql_statements.append(f"INSERT INTO mahasiswa (nim, email, nama_lengkap, nama_prodi) VALUES ({nim}, '{email}', '{escape_str(nama)}', '{escape_str(prodi['nama'])}');")
        mahasiswa_list.append({'nim': nim, 'prodi': prodi['nama']})
        
    dosen_list = []
    for i in range(JUMLAH_DOSEN):
        fakultas_singkatan = random.choice(list(prodi_data.keys()))
        nama_fakultas = [f[0] for f in fakultas_data if f[1] == fakultas_singkatan][0]
        nama = fake.name()
        email = f"{nama.lower().split()[0].replace('.', '')}{i+1}@itb.ac.id"
        nidn = int(f"10{i+1:08}")
        
        sql_statements.append(f"INSERT INTO akun (email, peran, hash_password) VALUES ('{email}', 'dosen', 'pbkdf2:sha256:...');")
        sql_statements.append(f"INSERT INTO dosen (nidn, email, nip, nama_lengkap, jabatan, nama_fakultas) VALUES ({nidn}, '{email}', '19{random.randint(70,90)}{random.randint(1,12):02}100{i}', '{escape_str(nama)}', 'Lektor', '{escape_str(nama_fakultas)}');")
        dosen_list.append({'nidn': nidn, 'fakultas': fakultas_singkatan})


    # 3. Dosen Wali
    sql_statements.append("\n-- 3. DOSEN WALI\n")
    dosen_wali_pairs = []
    # ... (code for dosen wali is modified to store pairs)
    for mhs in mahasiswa_list:
        mhs_fakultas = [p['fakultas'] for p in prodi_list if p['nama'] == mhs['prodi']][0]
        dosen_pool = [d for d in dosen_list if d['fakultas'] == mhs_fakultas]
        if dosen_pool:
            dosen_wali = random.choice(dosen_pool)
            sql_statements.append(f"INSERT INTO dosen_wali (nidn, nim) VALUES ({dosen_wali['nidn']}, {mhs['nim']});")
            dosen_wali_pairs.append({'nidn': dosen_wali['nidn'], 'nim': mhs['nim']})


    # 4. Kurikulum & Mata Kuliah
    sql_statements.append("\n-- 4. KURIKULUM & MATA KULIAH\n")
    # ... (code for kurikulum and mata kuliah remains the same)
    sql_statements.append(f"INSERT INTO kurikulum (tahun, bahan_kajian, capaian) VALUES ({tahun_kurikulum}, 'Bahan kajian untuk kurikulum {tahun_kurikulum}', 'Capaian pembelajaran untuk kurikulum {tahun_kurikulum}');")
    
    matkul_list = []
    for prodi in prodi_list:
        for i in range(JUMLAH_MATA_KULIAH_PER_PRODI):
            kode_mk = f"{prodi['kode'].replace('1','',1)}{random.randint(1,4)}{i+1:02}"
            nama_mk = f"Mata Kuliah {prodi['kode']} {i+1}"
            sks = random.choice([2, 3, 4])
            sql_statements.append(f"INSERT INTO mata_kuliah (kode_mk, nama_mk, deskripsi_mk, sks, tahun_kurikulum) VALUES ('{kode_mk}', '{escape_str(nama_mk)}', 'Deskripsi untuk {escape_str(nama_mk)}', {sks}, {tahun_kurikulum});")
            matkul_list.append({'kode_mk': kode_mk, 'prodi_kode': prodi['kode']})


    # 5. Semester & Kelas
    sql_statements.append("\n-- 5. SEMESTER & KELAS MATA KULIAH\n")
    # ... (code for semester and kelas mata kuliah remains the same)
    sql_statements.append(f"INSERT INTO semester (tahun, semester, waktu_mulai_pengisian_nilai, waktu_selesai_pengisisan_nilai) VALUES ({tahun_semester}, '{nama_semester}', '{tahun_semester}-12-20', '{tahun_semester+1}-01-20');")
    
    kelas_list = []
    for mk in matkul_list:
        for i in range(1, JUMLAH_KELAS_PER_MK + 1):
            nomor_kelas = f"{i:02}"
            sql_statements.append(f"INSERT INTO kelas_mata_kuliah (nomor_kelas, kode_mk, tahun, semester, kapasitas) VALUES ('{nomor_kelas}', '{mk['kode_mk']}', {tahun_semester}, '{nama_semester}', '100');")
            kelas_list.append({'nomor_kelas': nomor_kelas, 'kode_mk': mk['kode_mk'], 'prodi_kode': mk['prodi_kode']})


    # 6. Pengambilan Rencana Studi (KRS)
    sql_statements.append("\n-- 6. PENGAMBILAN RENCANA STUDI (KRS)\n")
    krs_list = []
    # ... (code for KRS is modified to store records)
    for mhs in mahasiswa_list:
        prodi_mhs_kode = [p['kode'] for p in prodi_list if p['nama'] == mhs['prodi']][0]
        krs_matkul_pool = [k for k in kelas_list if k['prodi_kode'] == prodi_mhs_kode]
        if len(krs_matkul_pool) >= JUMLAH_MK_DIAMBIL_MAHASISWA:
            krs_diambil = random.sample(krs_matkul_pool, JUMLAH_MK_DIAMBIL_MAHASISWA)
            for krs in krs_diambil:
                indeks_nilai = random.choice(['A', 'AB', 'B', 'BC', 'C', 'D', 'E'])
                sql_statements.append(f"INSERT INTO mengambil_rencana_studi (nim, nomor_kelas, kode_mk, tahun, semester, tanggal_persetujuan, status, indeks_nilai) VALUES ({mhs['nim']}, '{krs['nomor_kelas']}', '{krs['kode_mk']}', {tahun_semester}, '{nama_semester}', '{tahun_semester}-08-25', 'Disetujui', '{indeks_nilai}');")
                krs_list.append({'nim': mhs['nim'], **krs})


    # --- MULAI PENAMBAHAN UNTUK TABEL BARU ---
    
    # 7. Ruangan & Jadwal Kegiatan
    sql_statements.append("\n-- 7. RUANGAN & JADWAL KEGIATAN\n")
    for i in range(JUMLAH_RUANGAN):
        gedung = random.choice(['Gedung Labtek V', 'Gedung Labtek VIII', 'Gedung Oktagon', 'Gedung TVST'])
        lantai = random.randint(1, 4)
        sql_statements.append(f"INSERT INTO ruangan (kode_ruangan, nama_ruangan, kapasitas, lokasi, gedung, lantai) VALUES ({7600+i}, 'Ruang Kuliah {7600+i}', 100, 'Jl. Ganesha No. 10', '{gedung}', {lantai});")

    jadwal_list = []
    for kelas in kelas_list:
        jam_mulai_pilihan = [f"{h:02}:{m:02}" for h in range(7, 16) for m in [0, 30]]
        jam_mulai = random.choice(jam_mulai_pilihan)
        jam_selesai = f"{(int(jam_mulai.split(':')[0]) + random.choice([1, 2])):02}:{jam_mulai.split(':')[1]}"
        kode_ruangan = 7600 + random.randint(0, JUMLAH_RUANGAN - 1)
        
        for i in range(JUMLAH_PERTEMUAN_PER_KELAS):
            tanggal_pertemuan = tanggal_mulai_semester + datetime.timedelta(weeks=i)
            sql_statements.append(f"INSERT INTO jadwal_kegiatan (nomor_kelas, kode_mk, tahun, semester, tanggal, jam_mulai, jam_selesai, jenis_kegiatan, kode_ruangan) VALUES ('{kelas['nomor_kelas']}', '{kelas['kode_mk']}', {tahun_semester}, '{nama_semester}', '{tanggal_pertemuan}', '{jam_mulai}', '{jam_selesai}', 'Kuliah', {kode_ruangan});")
            jadwal_list.append({**kelas, 'tanggal': tanggal_pertemuan, 'jam_mulai': jam_mulai})
            
    # 8. Dosen Pengajar
    sql_statements.append("\n-- 8. DOSEN PENGAJAR\n")
    for kelas in kelas_list:
        prodi_kode = kelas['prodi_kode']
        fakultas = [p['fakultas'] for p in prodi_list if p['kode'] == prodi_kode][0]
        dosen_pool = [d for d in dosen_list if d['fakultas'] == fakultas]
        if dosen_pool:
            dosen_pengajar = random.choice(dosen_pool)
            sql_statements.append(f"INSERT INTO dosen_pengajar (nidn, nomor_kelas, kode_mk, tahun, semester) VALUES ({dosen_pengajar['nidn']}, '{kelas['nomor_kelas']}', '{kelas['kode_mk']}', {tahun_semester}, '{nama_semester}');")

    # 9. Kehadiran
    sql_statements.append("\n-- 9. KEHADIRAN\n")
    for krs in krs_list:
        jadwal_kelas_ini = [j for j in jadwal_list if j['kode_mk'] == krs['kode_mk'] and j['nomor_kelas'] == krs['nomor_kelas']]
        for jadwal in jadwal_kelas_ini:
            status = random.choices(['Hadir', 'Izin', 'Sakit', 'Alpa'], weights=[85, 5, 5, 5], k=1)[0]
            sql_statements.append(f"INSERT INTO kehadiran (nim, nomor_kelas, kode_mk, tahun, semester, tanggal, jam_mulai, status_hadir) VALUES ({krs['nim']}, '{krs['nomor_kelas']}', '{krs['kode_mk']}', {tahun_semester}, '{nama_semester}', '{jadwal['tanggal']}', '{jadwal['jam_mulai']}', '{status}');")
            
    return "\n".join(sql_statements)

# --- TULIS KE FILE ---
if __name__ == "__main__":
    semua_data_sql = generate_data()
    nama_file_output = "data_populasi_lengkap.sql"
    with open(nama_file_output, 'w', encoding='utf-8') as f:
        f.write(semua_data_sql)
    print(f"✅ Berhasil! Data populasi lengkap telah dibuat di file '{nama_file_output}'")