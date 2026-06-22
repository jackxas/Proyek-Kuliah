from daftarbarang import daftar_barang,tampilkan_daftar

def cek_barang():
    tampilkan_daftar()

    while True:
        try:
            pilih = int(input("Pilih nomor barang yang ingin dicek: "))
            if pilih < 1 or pilih > len(daftar_barang):
                print("Nomor tidak ada di daftar! Coba lagi.\n")
                continue
            break
        except ValueError:
            print("Input harus berupa angka!\n")

    nama_barang = list(daftar_barang.keys())[pilih - 1]
    batas = daftar_barang[nama_barang]

    while True:
        try:
            penggunaan = int(input(f"Masukkan penggunaan watt aktual {nama_barang}: "))
            break
        except ValueError:
            print("Input watt harus berupa angka!\n")

    if penggunaan <= batas:
        print(f"Penggunaan {nama_barang} masih dalam batas wajar ({penggunaan}W ≤ {batas}W)\n")
    else:
        print(f"Penggunaan {nama_barang} melebihi batas wajar ({penggunaan}W > {batas}W)\n")



