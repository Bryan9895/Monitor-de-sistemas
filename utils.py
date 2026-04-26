import tkinter as tk
from tkinter import ttk
from info_sistema import *

def boot_ui():

    cpu = pegar_uso_cpu()
    ram = pegar_uso_ram()
    disk = pegar_uso_disco()
    temp = pegar_temp()

    root = tk.Tk()
    root.title("Visualizador de Sistemas")
    root.geometry("300x300")
    root.configure(bg="#000000")

    frame = tk.Frame(root, bg="#000000")
    frame.pack(pady=20)

   
    cpu_label = tk.Label(frame, text="CPU", fg="white", bg="#000000")
    cpu_label.pack()
   
    cpu_bar = ttk.Progressbar(frame, length=200, maximum=100)
    cpu_label = tk.Label(frame, text=f"{cpu}")
    cpu_bar.pack()
    
    cpu_percent_label = tk.Label(frame, text="0%", fg="white", bg="#000000")
    cpu_percent_label.pack()

    #* ----------RAM------------*#
    ram_label = tk.Label(frame, text="RAM", fg="white", bg="#000000")
    ram_label.pack()

    ram_bar = ttk.Progressbar(frame, length=200, maximum=100)
    ram_bar.pack()
    
    ram_percent_label = tk.Label(frame, text="0%", fg="white", bg="#000000")
    ram_percent_label.pack()
     #* ----------DISK------------*#
    disk_label = tk.Label(frame, text="DISK", fg="white", bg="#000000")
    disk_label.pack()

    disk_bar = ttk.Progressbar(frame, length=200, maximum=100)
    disk_bar.pack()

    disk_percent_label = tk.Label(frame, text="0%", fg="white", bg="#000000")
    disk_percent_label.pack

    #* ----------TEMP------------*#
    temp_label = tk.Label(frame, text="Temp: --", fg="white", bg="#000000")
    temp_label.pack()

    temp_percent_label = tk.Label(frame, text="0%", fg="white", bg="#000000")
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
        core_labels = []
        cores = pegar_uso_por_cores()

        for i in range(len(cores)):
            label = tk.Label(root, text=f"Core {i}: 0%", fg="white", bg="#000000")
            label.pack()
            core_labels.append(label)
            
    update()
    root.mainloop()