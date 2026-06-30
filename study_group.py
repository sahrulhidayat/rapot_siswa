import tkinter as tk
from tkinter import ttk, messagebox
import fonts
import sqlite3


class StudyGroupClass:
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
            text="Sesuaikan Detail Rombel",
            padx=10,
            compound=tk.LEFT,
            font=fonts.get_font(self.root, 18),
            bg="#0e4979",
            fg="white",
        )
        title.place(x=12, y=15, relwidth=0.98, height=35)

        # ==== Variables ====
        self.var_groupName = tk.StringVar()
        self.var_class = tk.StringVar()
        self.var_guardianTeacher = tk.StringVar()

        # ==== Widgets ====
        lbl_groupName = tk.Label(
            self.root,
            text="Nama Rombel",
            font=fonts.get_font(self.root, 13),
            bg="white",
        ).place(relx=0.01, y=60)

        lbl_class = tk.Label(
            self.root,
            text="Kelas",
            font=fonts.get_font(self.root, 13),
            bg="white",
        ).place(relx=0.01, y=100)

        lbl_guardianTeacher = tk.Label(
            self.root,
            text="Wali Kelas",
            font=fonts.get_font(self.root, 13),
            bg="white",
        ).place(relx=0.01, y=140)

        # ==== Entry Fields ====

        self.txt_groupName = tk.Entry(
            self.root,
            textvariable=self.var_groupName,
            font=fonts.get_font(self.root, 13),
            bg="lightyellow",
        )
        self.txt_groupName.place(relx=0.125, y=60, relwidth=0.18)

        self.txt_class = tk.Entry(
            self.root,
            textvariable=self.var_class,
            font=fonts.get_font(self.root, 13),
            bg="lightyellow",
        )
        self.txt_class.place(relx=0.125, y=100, relwidth=0.18)

        self.txt_guardianTeacher = tk.Entry(
            self.root,
            textvariable=self.var_guardianTeacher,
            font=fonts.get_font(self.root, 13),
            bg="lightyellow",
        )
        self.txt_guardianTeacher.place(relx=0.125, y=140, relwidth=0.18)

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
        lbl_search_groupName = tk.Label(
            self.root,
            text="Cari Rombel",
            font=fonts.get_font(self.root, 13),
            bg="white",
        ).place(relx=0.6, y=60)

        txt_search_groupName = tk.Entry(
            self.root,
            textvariable=self.var_search,
            font=fonts.get_font(self.root, 13),
            bg="lightyellow",
        ).place(relx=0.70, y=60, relwidth=0.18)

        btn_search = tk.Button(
            self.root,
            text="Cari",
            font=fonts.get_font(self.root, 13),
            bg="#0f7c8f",
            fg="white",
            cursor="hand2",
            command=self.search,
        ).place(relx=0.89, y=60, relwidth=0.1, height=26)

        # ==== Content ====
        self.C_Frame = tk.Frame(self.root, bd=2, relief=tk.RIDGE)
        self.C_Frame.place(relx=0.6, y=100, relwidth=0.39, relheight=0.75)

        scrollx = ttk.Scrollbar(self.C_Frame, orient=tk.HORIZONTAL)
        scrolly = ttk.Scrollbar(self.C_Frame, orient=tk.VERTICAL)

        self.StudyGroupTable = ttk.Treeview(
            self.C_Frame,
            columns=("group_id", "name", "class", "guardian_teacher"),
            xscrollcommand=scrollx.set,
            yscrollcommand=scrolly.set,
        )
        scrollx.pack(side=tk.BOTTOM, fill=tk.X)
        scrolly.pack(side=tk.RIGHT, fill=tk.Y)
        scrollx.config(command=self.StudyGroupTable.xview)
        scrolly.config(command=self.StudyGroupTable.yview)

        self.StudyGroupTable.heading("group_id", text="ID Rombel")
        self.StudyGroupTable.heading("name", text="Nama")
        self.StudyGroupTable.heading("class", text="Kelas")
        self.StudyGroupTable.heading("guardian_teacher", text="Wali Kelas")
        self.StudyGroupTable["show"] = "headings"
        self.StudyGroupTable.column("group_id", width=100)
        self.StudyGroupTable.column("name", width=100)
        self.StudyGroupTable.column("class", width=100)
        self.StudyGroupTable.column("guardian_teacher", width=100)
        self.StudyGroupTable.pack(fill=tk.BOTH, expand=1)
        self.StudyGroupTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()

    # ========================================================
    def clear(self):
        self.show()
        self.var_groupName.set("")
        self.var_class.set("")
        self.var_guardianTeacher.set("")
        self.var_search.set("")
        self.txt_groupName.config(state=tk.NORMAL)

    def delete(self):
        con = sqlite3.connect(database="rapot_siswa.db")
        cur = con.cursor()
        try:
            if self.var_groupName.get() == "":
                messagebox.showerror(
                    "Error", "Pilih salah satu Rombel", parent=self.root
                )
            else:
                cur.execute(
                    """SELECT
                        *
                        FROM
                        studyGroup
                        WHERE
                        name = ?""",
                    (self.var_groupName.get(),),
                )
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror(
                        "Error",
                        "Pilih Rombel dari daftar yang sudah ada",
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
                            """DELETE FROM studyGroup
                                WHERE
                                name = ?""",
                            (self.var_groupName.get(),),
                        )
                        con.commit()
                        messagebox.showinfo(
                            "Menghapus", "Rombel berhasil dihapus", parent=self.root
                        )
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error", f"error dikarenakan {str(ex)}")

    def get_data(self, ev):
        self.txt_groupName.config(state="readonly")
        r = self.StudyGroupTable.focus()
        if not r:
            return
        content = self.StudyGroupTable.item(r)
        row = content.get("values")
        if not row:
            return
        self.var_groupName.set(row[1])
        self.var_class.set(row[2])
        self.var_guardianTeacher.set(row[3])

    def add(self):
        con = sqlite3.connect(database="rapot_siswa.db")
        cur = con.cursor()
        try:
            if self.var_groupName.get() == "":
                messagebox.showerror(
                    "Error", "Nama Rombel harus diisi", parent=self.root
                )
            else:
                cur.execute(
                    """SELECT
                        *
                        FROM
                        studyGroup
                        WHERE
                        name = ?""",
                    (self.var_groupName.get(),),
                )
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror(
                        "Error", "Nama Rombel sudah ada", parent=self.root
                    )
                else:
                    cur.execute(
                        """INSERT INTO
                            studyGroup (name, class, guardian_teacher)
                            VALUES
                            (?, ?, ?)""",
                        (
                            self.var_groupName.get(),
                            self.var_class.get(),
                            self.var_guardianTeacher.get(),
                        ),
                    )
                    con.commit()
                    messagebox.showinfo(
                        "Berhasil", "Rombel berhasil ditambahkan", parent=self.root
                    )
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"error dikarenakan {str(ex)}")

    def update(self):
        con = sqlite3.connect(database="rapot_siswa.db")
        cur = con.cursor()
        try:
            if self.var_groupName.get() == "":
                messagebox.showerror(
                    "Error", "Nama Rombel harus diisi", parent=self.root
                )
            else:
                cur.execute(
                    """SELECT
                        *
                        FROM
                        studyGroup
                        WHERE
                        name = ?""",
                    (self.var_groupName.get(),),
                )
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror(
                        "Error",
                        "Pilih Rombel dari daftar yang sudah ada",
                        parent=self.root,
                    )
                else:
                    cur.execute(
                        """UPDATE studyGroup
                            SET
                            class = ?,
                            guardian_teacher = ?
                            WHERE
                            name = ?""",
                        (
                            self.var_class.get(),
                            self.var_guardianTeacher.get(),
                            self.var_groupName.get(),
                        ),
                    )
                    con.commit()
                    messagebox.showinfo(
                        "Berhasil", "Rombel berhasil diperbarui", parent=self.root
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
                studyGroup""")
            rows = cur.fetchall()
            self.StudyGroupTable.delete(*self.StudyGroupTable.get_children())
            for row in rows:
                self.StudyGroupTable.insert("", tk.END, values=row)

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
                    "Masukkan nama Rombel untuk mencari",
                    parent=self.root,
                )
                return
            cur.execute(
                """SELECT
                    *
                    FROM
                    studyGroup
                    WHERE
                    name LIKE ?""",
                (f"%{search_text}%",),
            )
            rows = cur.fetchall()
            if rows:
                self.StudyGroupTable.delete(*self.StudyGroupTable.get_children())
                for row in rows:
                    self.StudyGroupTable.insert("", tk.END, values=row)
            else:
                messagebox.showerror("Error", "Data tidak ditemukan", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error", f"error dikarenakan {str(ex)}")


if __name__ == "__main__":
    root = tk.Tk()
    obj = StudyGroupClass(root)
    root.mainloop()
