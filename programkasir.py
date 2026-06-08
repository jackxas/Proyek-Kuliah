def hitung_total_harga_barang():
    daftar_harga = []
    
    while True:
        try:
            jumlah_barang = int(input("Masukkan jumlah barang yang anda beli: "))
            if jumlah_barang <= 0:
                print("Jumlah barang harus lebih dari 0.")
                continue
            break 
        except ValueError:
            print("Input tidak valid. Masukkan angka bulat")
        
    for i in range(jumlah_barang):
        while True:
            try:
                harga = float(input(f"Masukkan harga barang ke-{i+1}: Rp."))
                if harga < 0:
                    print("Harga tidak boleh negatif. Silakan ulangi.")
                    continue
                daftar_harga.append(harga)
                break
            except ValueError:
                print("Input tidak valid. Masukkan angka")
         
    total_belanja = sum(daftar_harga)
    print("\n==== TOTAL BELANJA SEMENTARA ====")
    print(f"Total harga sebelum diskon: Rp {total_belanja:,.0f}")
    return total_belanja

def diskon_belanja(total_belanja):
    print("\nDI TOKO INI TERSEDIA BERBAGAI DISKON!")
    lihat_diskon = input("Apakah Anda ingin melihat daftar diskon? (y/n): ").lower()

    if lihat_diskon == "y":
        print("\n=== DAFTAR DISKON ===")
        print("Total Belanja > 1.000.000  : Diskon 15%")
        print("Total Belanja > 500.000    : Diskon 10%")
        print("Total Belanja > 100.000    : Diskon 5%")

    if total_belanja > 1_000_000:
        diskon = 0.15
    elif total_belanja > 500_000:
        diskon = 0.10
    elif total_belanja > 100_000:
        diskon = 0.05
    else:
        diskon = 0

    total_diskon = total_belanja * diskon
    total_setelah_diskon = total_belanja - total_diskon

    print("\n===== HASIL DISKON =====")
    print(f"Diskon: {diskon*100:.0f}%")
    print(f"Total potongan: Rp {total_diskon:,.0f}")
    print(f"Total setelah diskon: Rp {total_setelah_diskon:,.0f}")

    return total_setelah_diskon

def proses_pembayaran(total_setelah_diskon):
    print("\n==== PROSES PEMBAYARAN ====")

    while True:
        print("\nPilih metode pembayaran:")
        print("1. Kartu Kredit (biaya admin Rp 0)")
        print("2. Transfer Bank (biaya admin Rp 2.500)")
        print("3. E-Wallet (biaya admin Rp 1.500)")

        metode = input("Masukkan pilihan (1/2/3): ")

        if metode == "1":
            biaya_admin = 0
            metode_bayar = "Kartu Kredit"
            break
        elif metode == "2":
            biaya_admin = 2500
            metode_bayar = "Transfer Bank"
            break
        elif metode == "3":
            biaya_admin = 1500
            metode_bayar = "E-Wallet"
            break
        else:
            print("Pilihan tidak valid, silakan ulangi.")

    total_akhir = total_setelah_diskon + biaya_admin

    print("\n==== RINCIAN PEMBAYARAN ====")
    print(f"Metode pembayaran : {metode_bayar}")
    print(f"Biaya admin       : Rp {biaya_admin:,.0f}")
    print(f"Total akhir harga : Rp {total_akhir:,.0f}")
    print("\n=== TERIMA KASIH SUDAH BERBELANJA ===")

    return total_akhir

print("=== SELAMAT DATANG DI KASIR ===\n")

total_belanja = hitung_total_harga_barang()
total_setelah_diskon = diskon_belanja(total_belanja)
proses_pembayaran(total_setelah_diskon)
