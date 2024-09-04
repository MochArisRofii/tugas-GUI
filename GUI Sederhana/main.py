import tkinter as tk
from tkinter import messagebox


def hitung_luas():
    try:
        pilihan = var.get()
        if pilihan == 1:  # Segitiga
            alas = float(entry_alas.get())
            tinggi = float(entry_tinggi.get())
            luas = 0.5 * alas * tinggi
            hasil.config(text=f"Luas Segitiga: {luas} unit²")
        elif pilihan == 2:  # Persegi Panjang
            panjang = float(entry_panjang.get())
            lebar = float(entry_lebar.get())
            luas = panjang * lebar
            hasil.config(text=f"Luas Persegi Panjang: {luas} unit²")
        elif pilihan == 3:  # Kubus
            sisi = float(entry_sisi.get())
            luas = 6 * sisi * sisi
            hasil.config(text=f"Luas Kubus: {luas} unit²")
        else:
            messagebox.showerror("Error", "Pilih jenis bangun terlebih dahulu!")
    except ValueError:
        messagebox.showerror("Error", "Input tidak valid! Harap masukkan angka.")


# Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Penghitung Luas - Dibuat oleh [Nama Anda]")

var = tk.IntVar()

# Judul
judul = tk.Label(root, text="Pilih Bangun Datar atau Bangun Ruang", font=("Arial", 14))
judul.pack(pady=10)

# Pilihan bangun
frame_radio = tk.Frame(root)
frame_radio.pack(pady=10)

tk.Radiobutton(frame_radio, text="Segitiga", variable=var, value=1).grid(
    row=0, column=0, padx=10, pady=5
)
tk.Radiobutton(frame_radio, text="Persegi Panjang", variable=var, value=2).grid(
    row=0, column=1, padx=10, pady=5
)
tk.Radiobutton(frame_radio, text="Kubus", variable=var, value=3).grid(
    row=0, column=2, padx=10, pady=5
)

# Input untuk segitiga
frame_segitiga = tk.Frame(root)
frame_segitiga.pack(pady=10)
tk.Label(frame_segitiga, text="Alas:").grid(row=0, column=0, padx=5)
entry_alas = tk.Entry(frame_segitiga)
entry_alas.grid(row=0, column=1, padx=5)
tk.Label(frame_segitiga, text="Tinggi:").grid(row=1, column=0, padx=5)
entry_tinggi = tk.Entry(frame_segitiga)
entry_tinggi.grid(row=1, column=1, padx=5)

# Input untuk persegi panjang
frame_persegi_panjang = tk.Frame(root)
frame_persegi_panjang.pack(pady=10)
tk.Label(frame_persegi_panjang, text="Panjang:").grid(row=0, column=0, padx=5)
entry_panjang = tk.Entry(frame_persegi_panjang)
entry_panjang.grid(row=0, column=1, padx=5)
tk.Label(frame_persegi_panjang, text="Lebar:").grid(row=1, column=0, padx=5)
entry_lebar = tk.Entry(frame_persegi_panjang)
entry_lebar.grid(row=1, column=1, padx=5)

# Input untuk kubus
frame_kubus = tk.Frame(root)
frame_kubus.pack(pady=10)
tk.Label(frame_kubus, text="Sisi:").grid(row=0, column=0, padx=5)
entry_sisi = tk.Entry(frame_kubus)
entry_sisi.grid(row=0, column=1, padx=5)

# Tombol untuk menghitung
btn_hitung = tk.Button(root, text="Hitung Luas", command=hitung_luas)
btn_hitung.pack(pady=10)

# Label untuk menampilkan hasil
hasil = tk.Label(root, text="", font=("Arial", 12))
hasil.pack(pady=10)

root.mainloop()
