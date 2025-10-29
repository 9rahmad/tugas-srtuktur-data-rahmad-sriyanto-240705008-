class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)
        print(f"Menambahkan {item} ke antrian")

    def dequeue(self):
        if not self.is_empty():
            item = self.items.pop(0)
            print(f"Mengambil {item} dari antrian")
            return item
        return "Antrian kosong"

    def display(self):
        if self.is_empty():
            print("Antrian kosong")
        else:
            print("Isi antrian:")
            print("Depan ->", end=" ")
            for item in self.items:
                print(f"| {item} ", end="")
            print("|<- Belakang")

# Program simulasi antrian A1-A10
print("Simulasi Antrian A1-A10")
print("-----------------------")

# Buat objek queue
antrian = Queue()

# Enqueue A1 sampai A10
print("\nMenambahkan A1-A10 ke antrian:")
for i in range(1, 11):
    item = f"A{i}"
    antrian.enqueue(item)

# Tampilkan isi antrian
print("\nIsi antrian setelah penambahan:")
antrian.display()

# Dequeue beberapa item
print("\nMengambil 3 item dari antrian:")
for _ in range(3):
    item = antrian.dequeue()

# Tampilkan isi antrian setelah pengambilan
print("\nIsi antrian setelah pengambilan 3 item:")
antrian.display()