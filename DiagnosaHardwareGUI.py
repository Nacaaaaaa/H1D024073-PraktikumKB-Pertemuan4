import tkinter as tk
from tkinter import messagebox

# 1. KNOWLEDGE BASE
# Struktur: "Nama Kerusakan": {"gejala": [daftar_gejala], "solusi": "Teks solusi"}
database_kerusakan = {
    "RAM Bermasalah": {
        "gejala": ["beep_berulang", "blue_screen", "tidak_tampil_layar"],
        "solusi": "Cabut RAM, bersihkan pin kuningan dengan penghapus bersih, lalu pasang kembali dengan kencang."
    },
    "Power Supply (PSU) Lemah/Mati": {
        "gejala": ["mati_mendadak", "bau_gosong", "kipas_tidak_muter"],
        "solusi": "Segera cabut kabel power. Jangan dinyalakan paksa. Kemungkinan besar PSU harus diganti dengan daya yang sesuai."
    },
    "Overheat (Prosesor Terlalu Panas)": {
        "gejala": ["mati_mendadak", "kipas_berisik", "kinerja_lambat"],
        "solusi": "Bersihkan debu pada kipas/heatsink prosesor dan ganti thermal paste (pasta pendingin)."
    },
    "VGA Bermasalah": {
        "gejala": ["layar_garis", "blue_screen", "tidak_tampil_layar"],
        "solusi": "Pastikan kabel monitor terpasang benar. Jika memakai VGA Card, cabut dan bersihkan pinnya. Update driver grafis."
    },
    "Hardisk / SSD Corrupt": {
        "gejala": ["bunyi_klik", "kinerja_lambat", "gagal_booting"],
        "solusi": "Cek kabel DATA. Segera backup data penting jika masih bisa masuk Windows, atau ganti media penyimpanan."
    }
}

# DAFTAR SEMUA GEJALA UNTUK PERTANYAAN GUI
semua_gejala = [
    ("beep_berulang", "Apakah komputer mengeluarkan bunyi beep berulang kali?"),
    ("blue_screen", "Apakah sering muncul layar biru (Blue Screen/BSOD)?"),
    ("tidak_tampil_layar", "Apakah mesin nyala tapi monitor gelap (No Display)?"),
    ("mati_mendadak", "Apakah komputer sering mati/restart mendadak?"),
    ("bau_gosong", "Apakah tercium bau gosong dari arah casing CPU?"),
    ("kipas_tidak_muter", "Apakah kipas power supply/prosesor berhenti berputar?"),
    ("kipas_berisik", "Apakah suara kipas terdengar sangat bising/ngebut?"),
    ("kinerja_lambat", "Apakah performa komputer sangat lambat atau sering hang?"),
    ("layar_garis", "Apakah tampilan di monitor bergaris atau warnanya aneh?"),
    ("bunyi_klik", "Apakah terdengar bunyi 'klik-klik' aneh dari dalam casing?"),
    ("gagal_booting", "Apakah gagal masuk Windows (muncul 'Boot Device Not Found')?")
]

class SistemPakarHardware:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Pakar Diagnosa Hardware")
        self.gejala_terpilih = []
        self.index_pertanyaan = 0

        # Label Pertanyaan
        self.label_tanya = tk.Label(root, text="Diagnosa Kerusakan Komputer/Laptop", font=("Times New Roman", 12, "bold"))
        self.label_tanya.pack(pady=20)

        # Tombol Mulai
        self.btn_mulai = tk.Button(root, text="Mulai Diagnosa", bg="lightblue", font=("Times New Roman", 12), command=self.mulai_tanya)
        self.btn_mulai.pack(pady=10)

        # Frame Tombol Jawaban
        self.frame_jawaban = tk.Frame(root)
        self.btn_ya = tk.Button(self.frame_jawaban, text="YA", width=10, bg="lightgreen", command=lambda: self.jawab('y'))
        self.btn_tidak = tk.Button(self.frame_jawaban, text="TIDAK", width=10, bg="salmon", command=lambda: self.jawab('t'))
        
        self.btn_ya.pack(side=tk.LEFT, padx=15)
        self.btn_tidak.pack(side=tk.LEFT, padx=15)

    def mulai_tanya(self):
        self.gejala_terpilih = []
        self.index_pertanyaan = 0
        self.btn_mulai.pack_forget() 
        self.frame_jawaban.pack(pady=20)
        self.tampilkan_pertanyaan()

    def tampilkan_pertanyaan(self):
        if self.index_pertanyaan < len(semua_gejala):
            kode, teks = semua_gejala[self.index_pertanyaan]
            self.label_tanya.config(text=teks, wraplength=350, font=("Times New Roman", 12, "normal"))
        else:
            self.proses_hasil()

    def jawab(self, respon):
        if respon == 'y':
            kode = semua_gejala[self.index_pertanyaan][0]
            self.gejala_terpilih.append(kode)

        self.index_pertanyaan += 1
        self.tampilkan_pertanyaan()

    def proses_hasil(self):
        hasil_diagnosa = []
        
        # 2. MESIN INFERENSI
        for kerusakan, data in database_kerusakan.items():
            syarat_gejala = data["gejala"]
            solusi = data["solusi"]
            
            # Cek apakah semua syarat gejala dari kerusakan ada di gejala_terpilih pengguna
            if all(s in self.gejala_terpilih for s in syarat_gejala):
                hasil_diagnosa.append(f"Kerusakan: {kerusakan}\nSolusi: {solusi}")

        # 3. OUTPUT & PENANGANAN "UNKNOWN" 
        if hasil_diagnosa:
            kesimpulan = "\n\n".join(hasil_diagnosa)
            pesan = f"Berdasarkan input Anda, ditemukan indikasi:\n\n{kesimpulan}"
        else:
            pesan = "Kerusakan tidak terdeteksi.\nSolusi: Gejala yang Anda masukkan tidak mengarah pada kerusakan spesifik di database. Coba periksa ulang atau hubungi teknisi terdekat."

        messagebox.showinfo("Hasil Diagnosa", pesan)

        # Reset ke awal
        self.frame_jawaban.pack_forget()
        self.btn_mulai.pack(pady=10)
        self.label_tanya.config(text="Diagnosa Selesai. Ingin mencoba lagi?", font=("Times New Roman", 12, "bold"))

# Menjalankan Aplikasi
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("450x250")
    app = SistemPakarHardware(root)
    root.mainloop()
