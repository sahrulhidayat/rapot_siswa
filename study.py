import tkinter as tk
from tkinter import ttk, messagebox
import fonts
import sqlite3


class StudyClass:
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
            text="Sesuaikan Detail Pelajaran",
            padx=10,
            compound=tk.LEFT,
            font=fonts.get_font(self.root, 18),
            bg="#0e4979",
            fg="white",
        )
        title.place(x=12, y=15, relwidth=0.98, height=35)

        # ==== Variables ====
        self.var_study = tk.StringVar()
        self.var_studyGroup = tk.StringVar()
        self.var_teacher = tk.StringVar()

        self.teacher_list = []
        self.fetch_teacher()

        # ==== Widgets ====
        lbl_studyName = tk.Label(
            self.root,
            text="Pelajaran",
            font=fonts.get_font(self.root, 13),
            bg="white",
        ).place(relx=0.01, y=60)

        lbl_studyGroup = tk.Label(
            self.root,
            text="Rombel",
            font=fonts.get_font(self.root, 13),
            bg="white",
        ).place(relx=0.01, y=100)

        lbl_teacher = tk.Label(
            self.root,
            text="Guru",
            font=fonts.get_font(self.root, 13),
            bg="white",
        ).place(relx=0.01, y=140)

        lbl_description = tk.Label(
            self.root,
            text="Deskripsi",
            font=fonts.get_font(self.root, 13),
            bg="white",
        ).place(relx=0.01, y=180)

        # ==== Entry Fields ====
        self.studyGroup_list = []
        # function_call to update the list
        self.fetch_studyGroup()

        self.txt_studyName = tk.Entry(
            self.root,
            textvariable=self.var_study,
            font=fonts.get_font(self.root, 13),
            bg="lightyellow",
        )
        self.txt_studyName.place(relx=0.125, y=60, relwidth=0.18, height=28)

        self.txt_studyGroup = ttk.Combobox(
            self.root,
            textvariable=self.var_studyGroup,
            values=self.studyGroup_list,
            font=fonts.get_font(self.root, 13),
            state="readonly",
            justify=tk.CENTER,
        )
        self.txt_studyGroup.place(relx=0.125, y=100, relwidth=0.18, height=28)
        self.txt_studyGroup.set("Pilih")

        self.txt_teacher = ttk.Combobox(
            self.root,
            textvariable=self.var_teacher,
            values=self.teacher_list,
            font=fonts.get_font(self.root, 13),
            state="readonly",
            justify=tk.CENTER,
        )
        self.txt_teacher.place(relx=0.125, y=140, relwidth=0.18, height=28)
        self.txt_teacher.set("Pilih")

        self.txt_description = tk.Text(
            self.root,
            font=fonts.get_font(self.root, 13),
            bg="lightyellow",
        )
        self.txt_description.place(relx=0.125, y=180, relwidth=0.45, relheight=0.27)

        # ==== Buttons ====
        self.btn_add = tk.Button(
            self.root,
            text="Simpan",
            font=fonts.get_font(self.root, 13),
            bg="#2196f3",
            fg="white",
            cursor="hand2",
            command=self.add,
        ).place(relx=0.125, rely=0.88, relwidth=0.105, height=40)

        self.btn_update = tk.Button(
            self.root,
            text="Perbarui",
            font=fonts.get_font(self.root, 13),
            bg="#4caf50",
            fg="white",
            cursor="hand2",
            command=self.update,
        ).place(relx=0.235, rely=0.88, relwidth=0.105, height=40)

        self.btn_delete = tk.Button(
            self.root,
            text="Hapus",
            font=fonts.get_font(self.root, 13),
            bg="#f44336",
            fg="white",
            cursor="hand2",
            command=self.delete,
        ).place(relx=0.345, rely=0.88, relwidth=0.105, height=40)

        self.btn_clear = tk.Button(
            self.root,
            text="Bersihkan",
            font=fonts.get_font(self.root, 13),
            bg="#607d8b",
            fg="white",
            cursor="hand2",
            command=self.clear,
        ).place(relx=0.455, rely=0.88, relwidth=0.105, height=40)

        # ==== Search Panel ====
        self.var_search = tk.StringVar()
        lbl_search_studyName = tk.Label(
            self.root,
            text="Cari Pelajaran",
            font=fonts.get_font(self.root, 13),
            bg="white",
        ).place(relx=0.6, y=60)

        txt_search_studyName = tk.Entry(
            self.root,
            textvariable=self.var_search,
            font=fonts.get_font(self.root, 13),
            bg="lightyellow",
        ).place(relx=0.73, y=60, relwidth=0.18, height=28)

        btn_search = tk.Button(
            self.root,
            text="Cari",
            font=fonts.get_font(self.root, 13),
            bg="#0f7c8f",
            fg="white",
            cursor="hand2",
            command=self.search,
        ).place(relx=0.92, y=60, relwidth=0.07, height=28)

        # ==== Content ====
        self.C_Frame = tk.Frame(self.root, bd=2, relief=tk.RIDGE)
        self.C_Frame.place(relx=0.6, y=100, relwidth=0.39, relheight=0.75)

        scrolly = tk.Scrollbar(self.C_Frame, orient=tk.VERTICAL)
        scrollx = tk.Scrollbar(self.C_Frame, orient=tk.HORIZONTAL)

        self.StudyTable = ttk.Treeview(
            self.C_Frame,
            columns=("study_id", "name", "study_group", "teacher", "description"),
            xscrollcommand=scrollx.set,
            yscrollcommand=scrolly.set,
        )
        scrollx.pack(side=tk.BOTTOM, fill=tk.X)
        scrolly.pack(side=tk.RIGHT, fill=tk.Y)
        scrollx.config(command=self.StudyTable.xview)
        scrolly.config(command=self.StudyTable.yview)

        self.StudyTable.heading("study_id", text="ID Pelajaran")
        self.StudyTable.heading("name", text="Nama")
        self.StudyTable.heading("study_group", text="Rombel")
        self.StudyTable.heading("teacher", text="Guru")
        self.StudyTable.heading("description", text="Deskripsi")
        self.StudyTable["show"] = "headings"
        self.StudyTable.column("study_id", width=100)
        self.StudyTable.column("name", width=100)
        self.StudyTable.column("study_group", width=100)
        self.StudyTable.column("teacher", width=100)
        self.StudyTable.column("description", width=100)
        self.StudyTable.pack(fill=tk.BOTH, expand=1)
        self.StudyTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()

    # ========================================================
    def clear(self):
        self.show()
        self.var_study.set("")
        self.var_studyGroup.set("")
        self.var_teacher.set("")
        self.var_search.set("")
        self.txt_description.delete("1.0", tk.END)
        self.txt_studyName.config(state=tk.NORMAL)
        self.txt_studyGroup.set("Pilih")
        self.txt_teacher.set("Pilih")

    def delete(self):
        con = sqlite3.connect(database="rapot_siswa.db")
        cur = con.cursor()
        try:
            if self.var_study.get() == "":
                messagebox.showerror(
                    "Error", "Pilih salah satu pelajaran", parent=self.root
                )
            else:
                cur.execute(
                    """SELECT
                    *
                    FROM
                    study
                    WHERE
                    name = ?""",
                    (self.var_study.get(),),
                )
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror(
                        "Error",
                        "Pilih pelajaran dari daftar yang sudah ada",
                        parent=self.root,
                    )
                else:
                    op = messagebox.askyesno(
                        "Konfirmasi",
                        "Apakah anda yakin ingin menghapus ini?",
                        parent=self.root,
                    )
                    if op is True:
                        cur.execute(
                            """DELETE FROM study
                                WHERE
                                name = ?""",
                            (self.var_study.get(),),
                        )
                        con.commit()
                        messagebox.showinfo(
                            "Menghapus", "Pelajaran berhasil dihapus", parent=self.root
                        )
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error", f"error dikarenakan {str(ex)}")

    def get_data(self, ev):
        self.txt_studyName.config(state="readonly")
        selected = self.StudyTable.selection()
        if not selected:
            return
        item_id = selected[0]
        row = self.StudyTable.item(item_id, "values")
        if not row:
            return
        self.var_study.set(row[1])
        self.var_studyGroup.set(row[2])
        self.var_teacher.set(row[3])
        self.txt_description.delete("1.0", tk.END)
        self.txt_description.insert(tk.END, row[4])

    def add(self):
        con = sqlite3.connect(database="rapot_siswa.db")
        cur = con.cursor()
        try:
            if self.var_study.get() == "":
                messagebox.showerror(
                    "Error", "Nama Pelajaran harus diisi", parent=self.root
                )
            else:
                cur.execute(
                    """SELECT
                    *
                    FROM
                    study
                    WHERE
                    name = ?""",
                    (self.var_study.get(),),
                )
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror(
                        "Error", "Nama Pelajaran sudah ada", parent=self.root
                    )
                else:
                    cur.execute(
                        """INSERT INTO
                            study (name, study_group, teacher, description)
                            VALUES
                            (?, ?, ?, ?)""",
                        (
                            self.var_study.get(),
                            self.var_studyGroup.get(),
                            self.var_teacher.get(),
                            self.txt_description.get("1.0", tk.END),
                        ),
                    )
                    con.commit()
                    messagebox.showinfo(
                        "Berhasil", "Pelajaran berhasil ditambahkan", parent=self.root
                    )
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"error dikarenakan {str(ex)}")

    def update(self):
        con = sqlite3.connect(database="rapot_siswa.db")
        cur = con.cursor()
        try:
            if self.var_study.get() == "":
                messagebox.showerror(
                    "Error", "Nama Pelajaran harus diisi", parent=self.root
                )
            else:
                cur.execute(
                    """SELECT
                    *
                    FROM
                    study
                    WHERE
                    name = ?""",
                    (self.var_study.get(),),
                )
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror(
                        "Error",
                        "Pilih Pelajaran dari daftar yang sudah ada",
                        parent=self.root,
                    )
                else:
                    cur.execute(
                        """UPDATE study
                            SET
                            study_group = ?,
                            teacher = ?,
                            description = ?
                            WHERE
                            name = ?""",
                        (
                            self.var_studyGroup.get(),
                            self.var_teacher.get(),
                            self.txt_description.get("1.0", tk.END),
                            self.var_study.get(),
                        ),
                    )
                    con.commit()
                    messagebox.showinfo(
                        "Berhasil", "Pelajaran berhasil diperbarui", parent=self.root
                    )
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"error dikarenakan {str(ex)}")

    def show(self):
        con = sqlite3.connect(database="rapot_siswa.db")
        cur = con.cursor()
        try:
            cur.execute("""SELECT
                *
                FROM
                study""")
            rows = cur.fetchall()
            self.StudyTable.delete(*self.StudyTable.get_children())
            for row in rows:
                self.StudyTable.insert("", tk.END, values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"error dikarenakan {str(ex)}")

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

    def fetch_teacher(self):
        con = sqlite3.connect(database="rapot_siswa.db")
        cur = con.cursor()
        try:
            cur.execute("""SELECT
                name
                FROM
                teacher""")
            rows = cur.fetchall()
            if len(rows) > 0:
                for row in rows:
                    self.teacher_list.append(row[0])

        except Exception as ex:
            messagebox.showerror("Error", f"error dikarenakan {str(ex)}")

    def search(self):
        con = sqlite3.connect(database="rapot_siswa.db")
        cur = con.cursor()
        try:
            search_text = self.var_search.get().strip()
            if search_text == "":
                messagebox.showerror(
                    "Error",
                    "Masukkan nama pelajaran untuk mencari",
                    parent=self.root,
                )
                return
            cur.execute(
                """SELECT
                    *
                    FROM
                    study
                    WHERE
                    name LIKE ?""",
                (f"%{search_text}%",),
            )
            rows = cur.fetchall()
            if rows:
                self.StudyTable.delete(*self.StudyTable.get_children())
                for row in rows:
                    self.StudyTable.insert("", tk.END, values=row)
            else:
                messagebox.showerror("Error", "Data tidak ditemukan", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error", f"error dikarenakan {str(ex)}")


if __name__ == "__main__":
    root = tk.Tk()
    obj = StudyClass(root)
    root.mainloop()
