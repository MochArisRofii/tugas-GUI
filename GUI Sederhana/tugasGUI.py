import tkinter as tk
from tkinter import messagebox

# Fungsi untuk menghitung luas permukaan kubus
def hitung_kubus():
    try:
        sisi = float(entry_sisi.get())
        luas = 6 * (sisi ** 2)
        result_label.config(text=f"Luas Permukaan Kubus: {luas} unit²")
        result_label.pack(side="bottom", pady=10)
    except ValueError:
        messagebox.showerror("Input Error", "Masukkan nilai numerik yang valid untuk sisi kubus.")

# Fungsi untuk menghitung luas segitiga
def hitung_segitiga():
    try:
        alas = float(entry_alas.get())
        tinggi = float(entry_tinggi.get())
        luas = 0.5 * alas * tinggi
        result_label.config(text=f"Luas Segitiga: {luas} unit²")
        result_label.pack(side="bottom", pady=10)
    except ValueError:
        messagebox.showerror("Input Error", "Masukkan nilai numerik yang valid untuk alas dan tinggi.")

# Fungsi untuk menampilkan input untuk menghitung kubus
def tampilkan_input_kubus():
    sembunyikan_semua_input()
    label_sisi.pack(pady=5)
    entry_sisi.pack(pady=5)
    button_hitung_kubus.pack(pady=10)

# Fungsi untuk menampilkan input untuk menghitung segitiga
def tampilkan_input_segitiga():
    sembunyikan_semua_input()
    label_alas.pack(pady=5)
    entry_alas.pack(pady=5)
    label_tinggi.pack(pady=5)
    entry_tinggi.pack(pady=5)
    button_hitung_segitiga.pack(pady=10)

# Fungsi untuk menyembunyikan semua input
def sembunyikan_semua_input():
    label_sisi.pack_forget()
    entry_sisi.pack_forget()
    button_hitung_kubus.pack_forget()

    label_alas.pack_forget()
    entry_alas.pack_forget()
    label_tinggi.pack_forget()
    entry_tinggi.pack_forget()
    button_hitung_segitiga.pack_forget()

# Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Penghitung Luas oleh Moch Aris Rofii")
root.geometry("400x400")  # Mengatur ukuran jendela
root.configure(bg="#f0f0f0")  # Mengatur warna background

# Frame untuk tombol pilihan
frame_pilihan = tk.Frame(root, bg="#f0f0f0")
frame_pilihan.pack(pady=20)

label_pilihan = tk.Label(frame_pilihan, text="Pilih Rumus yang Ingin Dihitung:", font=("Arial", 14), bg="#f0f0f0")
label_pilihan.pack()

button_pilih_kubus = tk.Button(frame_pilihan, text="Hitung Luas Kubus", font=("Arial", 12), bg="#4CAF50", fg="white", command=tampilkan_input_kubus)
button_pilih_kubus.pack(pady=5, ipadx=10)

button_pilih_segitiga = tk.Button(frame_pilihan, text="Hitung Luas Segitiga", font=("Arial", 12), bg="#4CAF50", fg="white", command=tampilkan_input_segitiga)
button_pilih_segitiga.pack(pady=5, ipadx=10)

# Frame untuk input dan hasil
frame_input = tk.Frame(root, bg="#f0f0f0")
frame_input.pack(pady=20)

# Bagian input untuk kubus
label_sisi = tk.Label(frame_input, text="Sisi Kubus:", font=("Arial", 12), bg="#f0f0f0")
entry_sisi = tk.Entry(frame_input, font=("Arial", 12), width=10)
button_hitung_kubus = tk.Button(frame_input, text="Hitung Luas Kubus", font=("Arial", 12), bg="#4CAF50", fg="white", command=hitung_kubus)

# Bagian input untuk segitiga
label_alas = tk.Label(frame_input, text="Alas Segitiga:", font=("Arial", 12), bg="#f0f0f0")
entry_alas = tk.Entry(frame_input, font=("Arial", 12), width=10)
label_tinggi = tk.Label(frame_input, text="Tinggi Segitiga:", font=("Arial", 12), bg="#f0f0f0")
entry_tinggi = tk.Entry(frame_input, font=("Arial", 12), width=10)
button_hitung_segitiga = tk.Button(frame_input, text="Hitung Luas Segitiga", font=("Arial", 12), bg="#4CAF50", fg="white", command=hitung_segitiga)

# Label untuk menampilkan hasil
result_label = tk.Label(root, text="", font=("Arial", 12), bg="#f0f0f0")

# Menjalankan aplikasi
root.mainloop()
