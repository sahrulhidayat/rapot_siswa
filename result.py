import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import fonts
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
            font=fonts.get_font(self.root, 16),
            bg="orange",
            fg="#262626",
        )
        title.place(x=12, y=15, relwidth=0.98, height=35)

        # ==== Widgets ======
        # ========== Variables ============
        self.var_nisn = tk.StringVar()
        self.var_mark = tk.StringVar()

        self.nisn_list = []
        self.student_list = []
        self.study_list = []
        self.fetch_students()
        self.fetch_study()

        self.style = ttk.Style(self.root)
        self.style.configure("Custom.TCombobox", padding=(8, 4, 8, 4))

        lbl_select = tk.Label(
            self.root,
            text="Pilih Siswa",
            font=fonts.get_font(self.root, 14),
            bg="white",
        ).place(relx=0.01, y=100)

        lbl_name = tk.Label(
            self.root,
            text="NISN",
            font=fonts.get_font(self.root, 14),
            bg="white",
        ).place(relx=0.01, y=160)

        lbl_study = tk.Label(
            self.root,
            text="Pelajaran",
            font=fonts.get_font(self.root, 14),
            bg="white",
        ).place(relx=0.01, y=220)

        lbl_mark = tk.Label(
            self.root,
            text="Nilai",
            font=fonts.get_font(self.root, 14),
            bg="white",
        ).place(relx=0.01, y=280)

        self.txt_student = ttk.Combobox(
            self.root,
            values=self.student_list,
            font=fonts.get_font(self.root, 14),
            style="Custom.TCombobox",
            state="readonly",
        )
        self.txt_student.place(relx=0.150, y=100, relwidth=0.33, height=28)
        self.txt_student.set("Pilih")
        self.txt_student.bind("<<ComboboxSelected>>", self.on_student_selected)

        txt_nisn = tk.Entry(
            self.root,
            textvariable=self.var_nisn,
            font=fonts.get_font(self.root, 14),
            bg="lightyellow",
            state="readonly",
        ).place(relx=0.15, y=160, relwidth=0.33)

        self.txt_study = ttk.Combobox(
            self.root,
            values=self.study_list,
            font=fonts.get_font(self.root, 14),
            style="Custom.TCombobox",
            state="readonly",
        )
        self.txt_study.place(relx=0.150, y=210, relwidth=0.33, height=28)
        self.txt_study.set("Pilih")

        txt_mark = tk.Entry(
            self.root,
            textvariable=self.var_mark,
            font=fonts.get_font(self.root, 14),
            bg="lightyellow",
        ).place(relx=0.15, y=280, relwidth=0.33)

        # ====== Button ======
        btn_submit = tk.Button(
            self.root,
            text="Kirim",
            font=fonts.get_font(self.root, 11),
            bg="lightgreen",
            activebackground="lightgreen",
            cursor="hand2",
        ).place(
            relx=0.15,
            rely=0.87,
            relwidth=0.117,
            height=35,
        )

        btn_clear = tk.Button(
            self.root,
            text="Bersihkan",
            font=fonts.get_font(self.root, 11),
            bg="lightgray",
            activebackground="lightgray",
            cursor="hand2",
        ).place(
            relx=0.28,
            rely=0.87,
            relwidth=0.117,
            height=35,
        )

        # ===== Image ======
        self.bg_img = Image.open("images/bg2.png").convert("RGBA")
        self.bg_img = self.bg_img.resize((500, 300), Image.Resampling.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg = tk.Label(self.root, image=self.bg_img, bg="white").place(
            relx=0.50, rely=0.15
        )

    # ==============================================

    def fetch_students(self):
        con = sqlite3.connect(database="rapot_siswa.db")
        cur = con.cursor()
        try:
            cur.execute("""SELECT
                *
                FROM
                student""")
            rows = cur.fetchall()
            if len(rows) > 0:
                for row in rows:
                    self.nisn_list.append(row[0])
                    self.student_list.append(row[1])

        except Exception as ex:
            messagebox.showerror("Error", f"error dikarenakan {str(ex)}")

    def fetch_study(self):
        con = sqlite3.connect(database="rapot_siswa.db")
        cur = con.cursor()
        try:
            cur.execute("""SELECT
                *
                FROM
                study""")
            rows = cur.fetchall()
            if len(rows) > 0:
                for row in rows:
                    self.study_list.append(row[1])

        except Exception as ex:
            messagebox.showerror("Error", f"error dikarenakan {str(ex)}")

    def on_student_selected(self, event=None):
        selected_index = self.txt_student.current()
        if selected_index < 0:
            return

        self.var_nisn.set(self.nisn_list[selected_index])


if __name__ == "__main__":
    root = tk.Tk()
    obj = ResultClass(root)
    root.mainloop()
