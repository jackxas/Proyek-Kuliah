import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class KegiatanFactory:
    @staticmethod
    def create_kegiatan(nama, prioritas, hari, tanggal, jam):
        return Kegiatan(nama, prioritas, hari, tanggal, jam)
    
class TaskRepository:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(TaskRepository, cls).__new__(cls, *args, **kwargs)
            cls._instance.daftar_kegiatan = []  # List data dipindah ke sini
        return cls._instance

    def get_all(self):
        return self.daftar_kegiatan

    def add(self, kegiatan):
        self.daftar_kegiatan.append(kegiatan)

    def remove(self, indeks):
        del self.daftar_kegiatan[indeks]

# 1. Class Data Kegiatan
class Kegiatan:
    def __init__(self, nama, prioritas, hari, tanggal, jam):
        self.nama = nama
        self.prioritas = prioritas
        self.hari = hari
        self.tanggal = tanggal
        self.jam = jam
        self.selesai = False

    def toggle_status(self):
        self.selesai = not self.selesai


# 2. Class Utama Aplikasi GUI
class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Jurnal To-Do List")
        
        # --- 1. MEMBESARKAN UKURAN LAYAR APLIKASI ---
        self.root.geometry("900x550") 
        self.root.resizable(False, False)
        
        self.daftar_kegiatan = []
        
        self.nama_hari = {
            "Monday": "Senin", "Tuesday": "Selasa", "Wednesday": "Rabu",
            "Thursday": "Kamis", "Friday": "Jumat", "Saturday": "Sabtu", "Sunday": "Minggu"
        }
        
        # --- ATUR TEMA GAYA BUKU KLASIK ---
        self.root.configure(bg="#FBF8F3") 
        style = ttk.Style()
        style.theme_use("classic") 
        
        WARNA_KERTAS = "#FBF8F3"   
        WARNA_TINTA = "#2C2520"    
        WARNA_SAMPUL = "#8B5A2B"   
        WARNA_TOMBOL = "#E6D7C3"   
        FONT_BUKU = ("Georgia", 11)
        FONT_JUDUL = ("Georgia", 11, "bold")

        style.configure(".", background=WARNA_KERTAS, foreground=WARNA_TINTA, font=FONT_BUKU)
        style.configure("TLabelframe", background=WARNA_KERTAS, borderwidth=1, relief="solid")
        style.configure("TLabelframe.Label", background=WARNA_KERTAS, foreground=WARNA_SAMPUL, font=FONT_JUDUL)
        style.configure("TButton", background=WARNA_TOMBOL, foreground=WARNA_TINTA, font=("Georgia", 10, "bold"), relief="flat")
        style.map("TButton", background=[("active", "#D4C2A8")])
        
        style.configure("Treeview", background="#FAF6EE", fieldbackground="#FAF6EE", foreground=WARNA_TINTA, font=("Georgia", 10), rowheight=28)
        style.configure("Treeview.Heading", background=WARNA_TOMBOL, foreground=WARNA_TINTA, font=("Georgia", 10, "bold"))
        
        self.buat_antarmuka()
        self.isi_waktu_otomatis()

    def buat_antarmuka(self):
        # --- FRAME INPUT ---
        frame_input = ttk.LabelFrame(self.root, text=" Tambah Kegiatan Baru ", padding=10)
        frame_input.pack(fill="x", padx=15, pady=10)

        # BARIS 0: Nama Kegiatan & Prioritas
        ttk.Label(frame_input, text="Kegiatan:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.ent_nama = ttk.Entry(frame_input, width=35)
        # Menggunakan columnspan=3 agar input nama memanjang dengan rapi
        self.ent_nama.grid(row=0, column=1, columnspan=3, sticky="we", padx=5, pady=5)

        ttk.Label(frame_input, text="Prioritas:").grid(row=0, column=4, sticky="w", padx=5, pady=5)
        self.cmb_prioritas = ttk.Combobox(frame_input, values=["Tinggi", "Sedang", "Rendah"], width=12)
        self.cmb_prioritas.set("Sedang")
        self.cmb_prioritas.grid(row=0, column=5, padx=5, pady=5)

        # BARIS 1: Hari, Tanggal, Jam (Sudah dipisah kolomnya agar tidak tabrakan)
        ttk.Label(frame_input, text="Hari:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.ent_hari = ttk.Entry(frame_input, width=12)
        self.ent_hari.grid(row=1, column=1, sticky="w", padx=5, pady=5)

        ttk.Label(frame_input, text="Tanggal:").grid(row=1, column=2, sticky="w", padx=5, pady=5)
        self.ent_tanggal = ttk.Entry(frame_input, width=12)
        self.ent_tanggal.grid(row=1, column=3, sticky="w", padx=5, pady=5)

        ttk.Label(frame_input, text="Jam:").grid(row=1, column=4, sticky="w", padx=5, pady=5)
        self.ent_jam = ttk.Entry(frame_input, width=12)
        self.ent_jam.grid(row=1, column=5, sticky="w", padx=5, pady=5)

        # --- 2. PERBAIKAN TOMBOL TAMBAH ---
        # Dipindah khusus ke Kolom 6 (membentang dari Baris 0 sampai Baris 1)
        btn_tambah = ttk.Button(frame_input, text="Tambah Kegiatan", command=self.tambah_kegiatan)
        btn_tambah.grid(row=0, column=6, rowspan=2, padx=15, pady=5, sticky="nswe")

        # --- FRAME DAFTAR TUGAS (TREEVIEW) ---
        frame_list = ttk.Frame(self.root, padding=10)
        frame_list.pack(fill="both", expand=True, padx=15, pady=5)

        kolom = ("status", "nama", "prioritas", "hari", "tanggal", "jam")
        self.tabel = ttk.Treeview(frame_list, columns=kolom, show="headings", selectmode="browse")
        
        self.tabel.heading("status", text="Status")
        self.tabel.heading("nama", text="Nama Kegiatan")
        self.tabel.heading("prioritas", text="Prioritas")
        self.tabel.heading("hari", text="Hari")
        self.tabel.heading("tanggal", text="Tanggal")
        self.tabel.heading("jam", text="Jam")

        # Menyesuaikan lebar kolom tabel agar pas dengan layar yang lebar
        self.tabel.column("status", width=120, anchor="center")
        self.tabel.column("nama", width=300, anchor="w")
        self.tabel.column("prioritas", width=100, anchor="center")
        self.tabel.column("hari", width=100, anchor="center")
        self.tabel.column("tanggal", width=110, anchor="center")
        self.tabel.column("jam", width=90, anchor="center")

        scrollbar = ttk.Scrollbar(frame_list, orient="vertical", command=self.tabel.yview)
        self.tabel.configure(yscrollcommand=scrollbar.set)
        
        self.tabel.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # --- FRAME TOMBOL AKSI ---
        frame_aksi = ttk.Frame(self.root, padding=10)
        frame_aksi.pack(fill="x", padx=15, pady=10)

        btn_centang = ttk.Button(frame_aksi, text="Centang / Ubah Status Selesai", command=self.centang_kegiatan)
        btn_centang.pack(side="left", padx=5)

        btn_hapus = ttk.Button(frame_aksi, text="Hapus Kegiatan", command=self.hapus_kegiatan)
        btn_hapus.pack(side="right", padx=5)

    def isi_waktu_otomatis(self):
        sekarang = datetime.now()
        hari_en = sekarang.strftime("%A")
        hari_id = self.nama_hari.get(hari_en, hari_en)
        
        self.ent_hari.insert(0, hari_id)
        self.ent_tanggal.insert(0, sekarang.strftime("%d/%m/%Y"))
        self.ent_jam.insert(0, sekarang.strftime("%H:%M"))

    def tambah_kegiatan(self):
        nama = self.ent_nama.get().strip()
        prioritas = self.cmb_prioritas.get()
        hari = self.ent_hari.get().strip()
        tanggal = self.ent_tanggal.get().strip()
        jam = self.ent_jam.get().strip()

        if not nama or not hari or not tanggal or not jam:
            messagebox.showwarning("Input Kosong", "Semua kolom data kegiatan wajib diisi!")
            return

        kegiatan_baru = Kegiatan(nama, prioritas, hari, tanggal, jam)
        self.daftar_kegiatan.append(kegiatan_baru)
        self.perbarui_tabel()
        self.ent_nama.delete(0, tk.END)

    def perbarui_tabel(self):
        for item in self.tabel.get_children():
            self.tabel.delete(item)

        for indeks, kgtn in enumerate(self.daftar_kegiatan):
            status_simbol = "✅ Selesai" if kgtn.selesai else "⬜ Belum"
            self.tabel.insert("", "end", iid=indeks, values=(
                status_simbol, kgtn.nama, kgtn.prioritas, kgtn.hari, kgtn.tanggal, kgtn.jam
            ))

    def centang_kegiatan(self):
        item_terpilih = self.tabel.selection()
        if not item_terpilih:
            messagebox.showwarning("Pilih Kegiatan", "Silakan pilih kegiatan dari tabel terlebih dahulu!")
            return

        indeks = int(item_terpilih[0])
        self.daftar_kegiatan[indeks].toggle_status()
        self.perbarui_tabel()

    def hapus_kegiatan(self):
        item_terpilih = self.tabel.selection()
        if not item_terpilih:
            messagebox.showwarning("Pilih Kegiatan", "Silakan pilih kegiatan yang ingin dihapus!")
            return

        indeks = int(item_terpilih[0])
        del self.daftar_kegiatan[indeks]
        self.perbarui_tabel()


# --- Main Program ---
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()