import msvcrt
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def input_password(prompt="Password: "):
    print(prompt, end='', flush=True)
    password = ""

    while True:
        char = msvcrt.getch()

        if char == b'\r':  # Enter
            print()
            break
        
        elif char == b'\x08':  # Backspace
            if len(password) > 0:
                # hapus bintang terakhir
                print('\b \b', end='', flush=True)
                password = password[:-1]
        
        elif char == b'\x00' or char == b'\xe0':  # tombol khusus
            msvcrt.getch()  # skip
            continue
        else:
            # tambah char ke password
            password += char.decode()
            print('*', end='', flush=True)

    return password


def login():
    clear()
    print("=== LOGIN SMART HOME ENERGY MONITOR ===")
    nama = input("Masukkan Username: ")

    coba = 2

    while coba > 0:
        clear()
        print("=== LOGIN SMART HOME ENERGY MONITOR ===")
        print(f"User: {nama}")
        print("Masukkan Password (minimal 6 karakter, harus ada huruf dan angka)")
        password = input_password("Password: ")

        if len(password) < 6:
            print("\nPassword terlalu pendek!")
            print(f"Sisa percobaan: {coba}\n")
            input("ENTER untuk lanjut...")
            coba -= 1
            continue

        huruf = any(c.isalpha() for c in password)
        angka = any(c.isdigit() for c in password)

        if not huruf or not angka:
            print("\nPassword harus ada huruf dan angka!")
            input("ENTER untuk lanjut...")
            coba -= 1
            continue

        clear()
        print(f"Login berhasil! Selamat datang, {nama}.")
        return

    clear()
    print("Terlalu banyak percobaan. Akses ditolak!")
    exit()

if __name__ == "__main__":
    login()