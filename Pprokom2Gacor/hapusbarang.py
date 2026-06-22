from daftarbarang import daftar_barang, tampilkan_daftar

def hapus_barang():
    tampilkan_daftar()

    while True:
        try:
            pilihan = int(input("Pilih nomor barang yang ingin dihapus: "))
            if pilihan < 1 or pilihan > len(daftar_barang):
                print("Input tidak valid! Masukkan nomor sesuai daftar.")
                continue
            break
        except ValueError:
            print("Input harus berupa angka!")

    barang_dihapus = daftar_barang[pilihan - 1]
    daftar_barang.pop(barang_dihapus)

    print(f"\n{barang_dihapus} berhasil dihapus.\n")

    