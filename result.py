import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3


class ResultClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Rapot Siswa")
        self.root.geometry("1200x480+80+170")
        self.root.resizable(True, True)
        self.root.config(bg="white")
        self.root.focus_force()

        # ===== Title =====
        title = tk.Label(
            self.root,
            text="Tambahkan Hasil Belajar Siswa",
            padx=10,
            compound=tk.LEFT,
            font=("goudy old style", 20, "bold"),
            bg="orange",
            fg="#262626",
        )
        title.place(x=12, y=15, relwidth=0.98, height=35)

        # ==== Widgets ======
        # ========== Variables ============
        self.var_nisn = tk.StringVar()
        self.var_name = tk.StringVar()
        self.var_study = tk.StringVar()
        self.var_mark = tk.StringVar()

        self.nisn_list = []

        lbl_select = tk.Label(
            self.root,
            text="Pilih Siswa",
            font=("goudy old style", 20, "bold"),
            bg="white",
        ).place(relx=0.01, y=100)

        lbl_name = tk.Label(
            self.root,
            text="Nama",
            font=("goudy old style", 20, "bold"),
            bg="white",
        ).place(relx=0.01, y=160)

        lbl_study = tk.Label(
            self.root,
            text="Pelajaran",
            font=("goudy old style", 20, "bold"),
            bg="white",
        ).place(relx=0.01, y=220)

        lbl_mark = tk.Label(
            self.root,
            text="Nilai",
            font=("goudy old style", 20, "bold"),
            bg="white",
        ).place(relx=0.01, y=280)

        self.txt_student = ttk.Combobox(
            self.root,
            textvariable=self.var_nisn,
            values=self.nisn_list,
            font=("goudy old style", 15, "bold"),
            state="readonly",
            justify=tk.CENTER,
        )
        self.txt_student.place(relx=0.150, y=100, relwidth=0.18)
        self.txt_student.set("Pilih")

        btn_search = tk.Button(
            self.root,
            text="Cari",
            font=("goudy old style", 20, "bold"),
            bg="#0f7c8f",
            fg="white",
            cursor="hand2",
        ).place(relx=0.343, y=100, relwidth=0.137, height=28)

        txt_name = tk.Entry(
            self.root,
            textvariable=self.var_name,
            font=("goudy old style", 20, "bold"),
            bg="lightyellow",
            state="readonly",
        ).place(relx=0.15, y=160, relwidth=0.33)

        txt_study = tk.Entry(
            self.root,
            textvariable=self.var_study,
            font=("goudy old style", 20, "bold"),
            bg="lightyellow",
        ).place(relx=0.15, y=220, relwidth=0.33)

        txt_mark = tk.Entry(
            self.root,
            textvariable=self.var_mark,
            font=("goudy old style", 20, "bold"),
            bg="lightyellow",
        ).place(relx=0.15, y=280, relwidth=0.33)

        # ====== Button ======
        btn_add = tk.Button(
            self.root,
            text="Kirim",
            font=("Times new roman", 15, "bold"),
            bg="lightgreen",
            activebackground="lightgreen",
            cursor="hand2",
        ).place(
            relx=0.15,
            rely=0.87,
            relwidth=0.137,
            height=35,
        )

        btn_clear = tk.Button(
            self.root,
            text="Bersihkan",
            font=("Times new roman", 15, "bold"),
            bg="lightgray",
            activebackground="lightgray",
            cursor="hand2",
        ).place(
            relx=0.30,
            rely=0.87,
            relwidth=0.137,
            height=35,
        )

        # ===== Image ======
        self.bg_img = Image.open("images/bg.jpg")
        self.bg_img = self.bg_img.resize((500, 300), Image.Resampling.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg = tk.Label(self.root, image=self.bg_img).place(x=630, y=100)


if __name__ == "__main__":
    root = tk.Tk()
    obj = ResultClass(root)
    root.mainloop()
