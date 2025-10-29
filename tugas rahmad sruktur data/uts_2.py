from collections import deque

# Struktur data pengunjung
class Pengunjung:
    def __init__(self, nama, pesanan):
        self.nama = nama
        self.pesanan = pesanan

    def __str__(self):
        return f"{self.nama} - Pesanan: {self.pesanan}"

# Queue untuk antrian pengunjung
class AntrianKafe:
    def __init__(self):
        self.antrian = deque()

    def tambah_pengunjung(self, pengunjung):
        self.antrian.append(pengunjung)
        print(f"{pengunjung.nama} masuk ke antrian.")

    def layani_pengunjung(self):
        if self.antrian:
            pengunjung = self.antrian.popleft()
            print(f"{pengunjung.nama} telah dilayani dan keluar dari antrian.")
        else:
            print("Tidak ada pengunjung dalam antrian.")

    def tampilkan_antrian(self):
        if self.antrian:
            print("Antrian saat ini:")
            for idx, p in enumerate(self.antrian, start=1):
                print(f"{idx}. {p}")
        else:
            print("Antrian kosong.")

# Simulasi
kafe = AntrianKafe()

# Tambah pengunjung
kafe.tambah_pengunjung(Pengunjung("Andi", "Kopi Hitam"))
kafe.tambah_pengunjung(Pengunjung("Budi", "Cappuccino"))
kafe.tambah_pengunjung(Pengunjung("Citra", "Teh Tarik"))

# Tampilkan antrian
kafe.tampilkan_antrian()

# Layani pengunjung
kafe.layani_pengunjung()
kafe.layani_pengunjung()

# Tampilkan antrian setelah pelayanan
kafe.tampilkan_antrian()