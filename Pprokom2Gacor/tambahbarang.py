from daftarbarang import daftar_barang

def tambah_barang():
    nama_baru = input("Masukkan nama barang baru: ").strip().lower()
    if nama_baru in daftar_barang:
        print("Barang sudah ada di daftar!\n")
        return

    while True:
        try:
            watt_baru = int(input(f"Masukkan batas watt wajar untuk {nama_baru}: "))
            break
        except ValueError:
            print("Input watt harus berupa angka!\n")

    daftar_barang[nama_baru] = watt_baru
    print(f"Barang '{nama_baru}' berhasil ditambahkan dengan batas {watt_baru}W.\n")

if __name__ == "__main__":
    tambah_barang()