def cek_ganjil_genap(angka):
    if angka % 2 == 0:
        return "genap"
    else:
        return "ganjil"

# Program utama
while True:
    try:
        input_user = input("Masukkan angka (atau ketik 'keluar' untuk berhenti): ")
        
        if input_user.lower() == 'keluar':
            break
            
        angka = int(input_user)
        hasil = cek_ganjil_genap(angka)
        print(f"Angka {angka} adalah bilangan {hasil}")
        
    except ValueError:
        print("Mohon masukkan angka yang valid!")