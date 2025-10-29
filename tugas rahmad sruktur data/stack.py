# Definisi kelas stack untuk tumpukan buku
class TumpukanBuku:
    def __init__(self):
        self.stack = []

    def tambah_buku(self, buku):
        self.stack.append(buku)
        print(f'Buku "{buku}" ditambahkan ke tumpukan.')

    def ambil_buku(self):
        if not self.stack:
            print("Tumpukan kosong, tidak ada buku yang bisa diambil.")
        else:
            buku = self.stack.pop()
            print(f'Buku "{buku}" diambil dari tumpukan.')

    def lihat_tumpukan(self):
        if not self.stack:
            print("Tumpukan kosong.")
        else:
            print("Isi tumpukan buku (dari bawah ke atas):")
            for i, buku in enumerate(self.stack):
                print(f"{i+1}. {buku}")

# Inisialisasi tumpukan
tumpukan = TumpukanBuku()

# Tambahkan Buku A1 sampai Buku A10
for i in range(1, 11):
    tumpukan.tambah_buku(f"Buku A{i}")

# Tampilkan isi tumpukan
print("\nMelihat isi tumpukan:")
tumpukan.lihat_tumpukan()

# Ambil satu buku dari tumpukan
print("\nMengambil satu buku dari tumpukan:")
tumpukan.ambil_buku()

# Tampilkan isi tumpukan setelah pengambilan
print("\nMelihat isi tumpukan setelah pengambilan:")
tumpukan.lihat_tumpukan()