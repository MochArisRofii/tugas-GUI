import tkinter as tk

button = tk.Tk()

button.title("Azhar Zakaria Bintang - Button")

label = tk.Label(button, text="Masukkan Nama:")
label.pack()

entry = tk.Entry(button)
entry.pack()

def on_button_click():
    nama = entry.get()
    label.config(text=f"Nama Anda: {nama}")

button = tk.Button(button, text="Klik", command=on_button_click)
button.pack()

button.mainloop()