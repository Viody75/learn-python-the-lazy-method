class CariSubmatriksMaksimum:
    def __init__(self):
        # Inisialisasi jumlah maksimum dengan nilai yang sangat kecil
        self.jumlah_maksimum = -float('inf')
        self.koordinat_terbaik = {}

    def cari_jumlah_maksimum(self, matrix):
        """
        Fungsi utama untuk memulai proses rekursif.
        """
        if not matrix:
            return 0, {}
        # Memulai rekursi untuk menjelajahi baris awal (r1)
        self._jelajahi_r1(matrix, 0)
        return self.jumlah_maksimum, self.koordinat_terbaik

    def _jelajahi_r1(self, matrix, r1):
        """Rekursi untuk baris awal (r1)."""
        if r1 >= len(matrix):
            return
        # Untuk r1 saat ini, jelajahi semua kolom awal (c1)
        self._jelajahi_c1(matrix, r1, 0)
        # Pindah ke r1 berikutnya
        self._jelajahi_r1(matrix, r1 + 1)

    def _jelajahi_c1(self, matrix, r1, c1):
        """Rekursi untuk kolom awal (c1)."""
        if c1 >= len(matrix[r1]):
            return
        # Untuk r1, c1 saat ini, jelajahi semua baris akhir (r2)
        self._jelajahi_r2(matrix, r1, c1, r1)
        # Pindah ke c1 berikutnya
        self._jelajahi_c1(matrix, r1, c1 + 1)

    def _jelajahi_r2(self, matrix, r1, c1, r2):
        """Rekursi untuk baris akhir (r2)."""
        if r2 >= len(matrix):
            return
        # Untuk r1, c1, r2 saat ini, jelajahi semua kolom akhir (c2)
        self._jelajahi_c2(matrix, r1, c1, r2, c1)
        # Pindah ke r2 berikutnya
        self._jelajahi_r2(matrix, r1, c1, r2 + 1)

    def _jelajahi_c2(self, matrix, r1, c1, r2, c2):
        """Rekursi untuk kolom akhir (c2) dan melakukan kalkulasi."""
        # Pastikan kolom akhir (c2) valid untuk semua baris dari r1 hingga r2
        is_valid_rectangle = True
        for i in range(r1, r2 + 1):
            if c2 >= len(matrix[i]):
                is_valid_rectangle = False
                break
        
        if not is_valid_rectangle:
            return

        # Hitung jumlah submatriks saat ini
        jumlah_saat_ini = 0
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                jumlah_saat_ini += matrix[i][j]

        # Perbarui jika ditemukan jumlah yang lebih besar
        if jumlah_saat_ini > self.jumlah_maksimum:
            self.jumlah_maksimum = jumlah_saat_ini
            self.koordinat_terbaik = {
                'start': (r1, c1),
                'end': (r2, c2)
            }

        # Pindah ke c2 berikutnya
        self._jelajahi_c2(matrix, r1, c1, r2, c2 + 1)

# Contoh penggunaan
matrix = [
    [1, 2, -1, -4, -20],
    [-8, -3, 4, 2],
    [3, 8, 10, 1, 3],
    [-4, -1, 1, 7, -6]
]

solver = CariSubmatriksMaksimum()
hasil_jumlah, hasil_koordinat = solver.cari_jumlah_maksimum(matrix)

print(f"Jumlah maksimum submatriks adalah: {hasil_jumlah}")
print(f"Koordinat kiri atas: {hasil_koordinat['start']}")
print(f"Koordinat kanan bawah: {hasil_koordinat['end']}")