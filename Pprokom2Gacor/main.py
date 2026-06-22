from autentikasi import login
from daftarbarang import tampilkan_daftar
from cekbarang import cek_barang
from tambahbarang import tambah_barang
from hapusbarang import hapus_barang

def menu():
    while True:
        print("\n[1] Cek Barang")
        print("[2] Tambah Barang")
        print("[3] Lihat Daftar Barang")
        print("[4] Hapus Barang")
        print("[5] Keluar")

        try:
            opsi = int(input("Pilih menu -> "))
        except ValueError:
            print("Input harus berupa angka!\n")
            continue

        if opsi == 1:
            cek_barang()
        elif opsi == 2:
            tambah_barang()
        elif opsi == 3:
            tampilkan_daftar()
        elif opsi == 4:
            hapus_barang()
        elif opsi == 5:
            print("\n=== Anda Keluar dari Program ===")
            break
        else:
            print("Pilihan tidak valid! Coba lagi.\n")

print("=== SMART HOME ENERGY MONITOR ===")
login()
menu()