import tkinter as tk
from tkinter import ttk
from info_sistema import *

def boot_ui():

    cpu = pegar_uso_cpu
    ram = pegar_uso_ram
    disk = pegar_uso_disco
    temp = pegar_temp

    root = tk.Tk()
    root.title("System Monitor")
    root.geometry("300x300")
    root.configure(bg="#1e1e1e")

    frame = tk.Frame(root, bg="#1e1e1e")
    frame.pack(pady=20)

    # CPU
    cpu_label = tk.Label(frame, text="CPU", fg="white", bg="#1e1e1e")
    cpu_label.pack()
   
    cpu_bar = ttk.Progressbar(frame, length=200, maximum=100)
    cpu_label = tk.Label(frame, text=f"{cpu}")
    cpu_bar.pack()
    
    cpu_percent_label = tk.Label(frame, text="0%", fg="white", bg="#1e1e1e")
    cpu_percent_label.pack()

    # RAM
    ram_label = tk.Label(frame, text="RAM", fg="white", bg="#1e1e1e")
    ram_label.pack()

    ram_bar = ttk.Progressbar(frame, length=200, maximum=100)
    ram_bar.pack()
    
    ram_percent_label = tk.Label(frame, text="0%", fg="white", bg="#1e1e1e")
    ram_percent_label.pack()
    # DISK
    disk_label = tk.Label(frame, text="DISK", fg="white", bg="#1e1e1e")
    disk_label.pack()

    disk_bar = ttk.Progressbar(frame, length=200, maximum=100)
    disk_bar.pack()

    disk_percent_label = tk.Label(frame, text="0%", fg="white", bg="#1e1e1e")
    disk_percent_label.pack

    # TEMP
    temp_label = tk.Label(frame, text="Temp: --", fg="white", bg="#1e1e1e")
    temp_label.pack()

    temp_percent_label = tk.Label(frame, text="0%", fg="white", bg="#1e1e1e")
    temp_percent_label.pack

    def update():
        cpu = pegar_uso_cpu()
        ram = pegar_uso_ram()
        disk = pegar_uso_disco()
        temp = pegar_temp()

        cpu_bar["value"] = cpu
        ram_bar["value"] = ram
        disk_bar["value"] = disk

        if temp:
            temp_label.config(text=f"Temp: {temp}°C")

        root.after(1000, update)
        cpu_percent_label.config(text=f"{cpu}%")
        ram_percent_label.config(text=f"{ram}%")
        disk_percent_label.config(text=f"{disk}%")
    update()
    root.mainloop()