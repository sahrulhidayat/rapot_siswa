import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import fonts
import sqlite3


class ReportClass:
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
            text="Rapot Hasil Belajar Siswa",
            padx=10,
            compound=tk.LEFT,
            font=fonts.get_font(self.root, 16),
            bg="orange",
            fg="#262626",
        )
        title.place(x=12, y=15, relwidth=0.98, height=35)

        # ===== Result Labels =======
        self.var_studyGroup = tk.StringVar()
        self.var_nisn = tk.StringVar()
        self.var_groupId = tk.StringVar()

        self.studyGroup_list = []
        self.student_list = []
        self.nisn_list = []

        # ===== Fetch Data =====
        self.fetch_studyGroup()

        lbl_studyGroup = tk.Label(
            self.root,
            text="Rombel",
            font=fonts.get_font(self.root, 11, "bold"),
            bg="white",
        ).place(relx=0.125, y=100)

        lbl_student = tk.Label(
            self.root,
            text="Nama",
            font=fonts.get_font(self.root, 11, "bold"),
            bg="white",
        ).place(relx=0.125, rely=0.285)

        lbl_nisn = tk.Label(
            self.root,
            text="NISN",
            font=fonts.get_font(self.root, 11, "bold"),
            bg="white",
        ).place(relx=0.125, rely=0.365)

        self.txt_studyGroup = ttk.Combobox(
            self.root,
            values=self.studyGroup_list,
            textvariable=self.var_studyGroup,
            font=fonts.get_font(self.root, 11),
            style="Custom.TCombobox",
            state="readonly",
        )
        self.txt_studyGroup.place(relx=0.200, y=100, relwidth=0.20)
        self.txt_studyGroup.set("Pilih")
        self.txt_studyGroup.bind(
            "<<ComboboxSelected>>", lambda event: self.fetch_student()
        )

        self.txt_student = ttk.Combobox(
            self.root,
            values=self.student_list,
            textvariable=tk.StringVar(),
            font=fonts.get_font(self.root, 11),
            style="Custom.TCombobox",
            state="readonly",
        )
        self.txt_student.place(relx=0.200, rely=0.285, relwidth=0.20)
        self.txt_student.set("Pilih")
        self.txt_student.bind("<<ComboboxSelected>>", self.on_student_selected)

        txt_nisn = tk.Entry(
            self.root,
            textvariable=self.var_nisn,
            font=fonts.get_font(self.root, 11),
            state="readonly",
        ).place(relx=0.200, rely=0.365, relwidth=0.20)

        # ============ Table ==============

        lbl_number = tk.Label(
            self.root,
            text="No.",
            font=fonts.get_font(self.root, 11, "bold"),
            bg="white",
            bd=2,
            relief=tk.GROOVE,
        ).place(relx=0.125, rely=0.45, relwidth=0.075, relheight=0.085)

        lbl_study = tk.Label(
            self.root,
            text="Pelajaran",
            font=fonts.get_font(self.root, 11, "bold"),
            bg="white",
            bd=2,
            relief=tk.GROOVE,
        ).place(relx=0.200, rely=0.45, relwidth=0.300, relheight=0.085)

        lbl_criteria = tk.Label(
            self.root,
            text="KKM",
            font=fonts.get_font(self.root, 11, "bold"),
            bg="white",
            bd=2,
            relief=tk.GROOVE,
        ).place(relx=0.5, rely=0.45, relwidth=0.125, relheight=0.085)

        lbl_mark = tk.Label(
            self.root,
            text="Nilai",
            font=fonts.get_font(self.root, 11, "bold"),
            bg="white",
            bd=2,
            relief=tk.GROOVE,
        ).place(relx=0.625, rely=0.45, relwidth=0.125, relheight=0.085)

        lbl_explain = tk.Label(
            self.root,
            text="Keterangan",
            font=fonts.get_font(self.root, 11, "bold"),
            bg="white",
            bd=2,
            relief=tk.GROOVE,
        ).place(relx=0.75, rely=0.45, relwidth=0.125, relheight=0.085)

        self.number = tk.Label(
            self.root,
            font=fonts.get_font(self.root, 11, "bold"),
            bg="white",
            bd=2,
            relief=tk.GROOVE,
        )
        self.number.place(relx=0.125, rely=0.535, relwidth=0.075, relheight=0.085)

        self.study = tk.Label(
            self.root,
            font=fonts.get_font(self.root, 11, "bold"),
            bg="white",
            bd=2,
            relief=tk.GROOVE,
        )
        self.study.place(relx=0.200, rely=0.535, relwidth=0.300, relheight=0.085)

        self.criteria = tk.Label(
            self.root,
            font=fonts.get_font(self.root, 11, "bold"),
            bg="white",
            bd=2,
            relief=tk.GROOVE,
        )
        self.criteria.place(relx=0.5, rely=0.535, relwidth=0.125, relheight=0.085)

        self.mark = tk.Label(
            self.root,
            font=fonts.get_font(self.root, 11, "bold"),
            bg="white",
            bd=2,
            relief=tk.GROOVE,
        )
        self.mark.place(relx=0.625, rely=0.535, relwidth=0.125, relheight=0.085)

        self.explain = tk.Label(
            self.root,
            font=fonts.get_font(self.root, 11, "bold"),
            bg="white",
            bd=2,
            relief=tk.GROOVE,
        )
        self.explain.place(relx=0.75, rely=0.535, relwidth=0.125, relheight=0.085)

    def fetch_studyGroup(self):
        con = sqlite3.connect(database="rapot_siswa.db")
        cur = con.cursor()
        try:
            cur.execute("""SELECT
                name
                FROM
                studyGroup""")
            rows = cur.fetchall()
            if len(rows) > 0:
                for row in rows:
                    self.studyGroup_list.append(row[0])

        except Exception as ex:
            messagebox.showerror("Error", f"error dikarenakan {str(ex)}")

    def fetch_student(self):
        self.student_list.clear()
        self.nisn_list.clear()
        self.txt_student.set("Pilih")
        self.txt_student.config(values=self.student_list)

        con = sqlite3.connect(database="rapot_siswa.db")
        cur = con.cursor()
        try:
            search_text = self.var_studyGroup.get().strip()
            cur.execute(
                """SELECT
                *
                FROM
                student
                WHERE
                study_group LIKE ?""",
                (f"%{search_text}%",),
            )
            rows = cur.fetchall()
            if len(rows) > 0:
                for row in rows:
                    self.nisn_list.append(row[0])
                    self.student_list.append(row[1])
                self.txt_student.config(values=self.student_list)

        except Exception as ex:
            messagebox.showerror("Error", f"error dikarenakan {str(ex)}")

    def on_student_selected(self, event=None):
        selected_index = self.txt_student.current()
        if selected_index < 0:
            return

        self.var_nisn.set(self.nisn_list[selected_index])


if __name__ == "__main__":
    root = tk.Tk()
    obj = ReportClass(root)
    root.mainloop()
