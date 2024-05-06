import tkinter as tk
import os


class Mon:
    def __init__(self):
        netappb1 = "netappb"
        netappbUP = os.system("ping -a -n 1 " + netappb1)
        response = print(netappb1)

        window = tk.Tk()
        netappbUPYES = tk.Label(text="Server Status")
        netappbUPYES.pack()

        entry = tk.Entry()
        status = entry.get()
        entry.pack()

        text_box = tk.Text()
        text_box.pack()


