import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import fonts


class TeacherClass:
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
            text="Sesuaikan Detail Guru",
            padx=10,
            compound=tk.LEFT,
            font=fonts.get_font(self.root, 18),
            bg="#0e4979",
            fg="white",
        )
        title.place(relx=0.01, y=15, relwidth=0.98, height=35)

        # ==== Variables ====

        self.var_teacherId = tk.StringVar()
        self.var_name = tk.StringVar()
        self.var_nip = tk.StringVar()
        self.var_gender = tk.StringVar()
        self.var_religion = tk.StringVar()
        self.var_contact = tk.StringVar()

        # ==== Widgets ====
        # -------- Column 1 --------
        lbl_name = tk.Label(
            self.root,
            text="Nama",
            font=fonts.get_font(self.root, 11),
            bg="white",
        ).place(relx=0.01, y=60)

        lbl_nip = tk.Label(
            self.root,
            text="NIP",
            font=fonts.get_font(self.root, 11),
            bg="white",
        ).place(relx=0.01, y=100)

        lbl_gender = tk.Label(
            self.root,
            text="Jenis Kelamin",
            font=fonts.get_font(self.root, 11),
            bg="white",
        ).place(relx=0.01, y=140)

        lbl_religion = tk.Label(
            self.root,
            text="Agama",
            font=fonts.get_font(self.root, 11),
            bg="white",
        ).place(relx=0.01, y=180)

        lbl_contact = tk.Label(
            self.root,
            text="No. HP",
            font=fonts.get_font(self.root, 11),
            bg="white",
        ).place(relx=0.01, y=220)

        # ==== Entry Fields ====

        self.txt_name = tk.Entry(
            self.root,
            textvariable=self.var_name,
            font=fonts.get_font(self.root, 11),
            bg="lightyellow",
        )
        self.txt_name.place(relx=0.125, y=60, relwidth=0.18)

        self.txt_nip = tk.Entry(
            self.root,
            textvariable=self.var_nip,
            font=fonts.get_font(self.root, 11),
            bg="lightyellow",
        )
        self.txt_nip.place(relx=0.125, y=100, relwidth=0.18)

        self.txt_gender = ttk.Combobox(
            self.root,
            textvariable=self.var_gender,
            values=("Pilih", "Laki-laki", "Perempuan"),
            font=fonts.get_font(self.root, 11),
            state="readonly",
            justify=tk.CENTER,
        )
        self.txt_gender.place(relx=0.125, y=140, relwidth=0.18, height=24)
        self.txt_gender.current(0)

        txt_religion = tk.Entry(
            self.root,
            textvariable=self.var_religion,
            font=fonts.get_font(self.root, 11),
            bg="lightyellow",
        ).place(relx=0.125, y=180, relwidth=0.18)

        txt_contact = tk.Entry(
            self.root,
            textvariable=self.var_contact,
            font=fonts.get_font(self.root, 11),
            bg="lightyellow",
        ).place(relx=0.125, y=220, relwidth=0.18)

        # ==== Buttons ====
        self.btn_add = tk.Button(
            self.root,
            text="Simpan",
            font=fonts.get_font(self.root, 11),
            bg="#2196f3",
            fg="white",
            cursor="hand2",
            command=self.add,
        ).place(relx=0.125, rely=0.88, relwidth=0.105, height=40)

        self.btn_update = tk.Button(
            self.root,
            text="Perbarui",
            font=fonts.get_font(self.root, 11),
            bg="#4caf50",
            fg="white",
            cursor="hand2",
            command=self.update,
        ).place(relx=0.235, rely=0.88, relwidth=0.105, height=40)

        self.btn_delete = tk.Button(
            self.root,
            text="Hapus",
            font=fonts.get_font(self.root, 11),
            bg="#f44336",
            fg="white",
            cursor="hand2",
            command=self.delete,
        ).place(relx=0.345, rely=0.88, relwidth=0.105, height=40)

        self.btn_clear = tk.Button(
            self.root,
            text="Bersihkan",
            font=fonts.get_font(self.root, 11),
            bg="#607d8b",
            fg="white",
            cursor="hand2",
            command=self.clear,
        ).place(relx=0.455, rely=0.88, relwidth=0.105, height=40)

        # ==== Search Panel ====
        self.var_search = tk.StringVar()

        lbl_search_teacher = tk.Label(
            self.root,
            text="Cari Guru",
            font=fonts.get_font(self.root, 11),
            bg="white",
        ).place(relx=0.60, y=60)

        txt_search_teacher = tk.Entry(
            self.root,
            textvariable=self.var_search,
            font=fonts.get_font(self.root, 11),
            bg="lightyellow",
        ).place(relx=0.725, y=60, relwidth=0.18)

        btn_search = tk.Button(
            self.root,
            text="Cari",
            font=fonts.get_font(self.root, 11),
            bg="#0f7c8f",
            fg="white",
            cursor="hand2",
            command=self.search,
        ).place(relx=0.92, y=60, relwidth=0.07, height=24)

        # ==== Content ====
        self.C_Frame = tk.Frame(self.root, bd=2, relief=tk.RIDGE)
        self.C_Frame.place(relx=0.60, y=100, relwidth=0.39, relheight=0.75)

        scrolly = tk.Scrollbar(self.C_Frame, orient=tk.VERTICAL)
        scrollx = tk.Scrollbar(self.C_Frame, orient=tk.HORIZONTAL)

        self.TeacherTable = ttk.Treeview(
            self.C_Frame,
            columns=(
                "teacher_id",
                "name",
                "nip",
                "gender",
                "religion",
                "contact",
            ),
            xscrollcommand=scrollx.set,
            yscrollcommand=scrolly.set,
        )
        scrollx.pack(side=tk.BOTTOM, fill=tk.X)
        scrolly.pack(side=tk.RIGHT, fill=tk.Y)
        scrollx.config(command=self.TeacherTable.xview)
        scrolly.config(command=self.TeacherTable.yview)

        self.TeacherTable.heading("teacher_id", text="ID Guru")
        self.TeacherTable.heading("name", text="Nama")
        self.TeacherTable.heading("nip", text="NIP")
        self.TeacherTable.heading("gender", text="Jenis Kelamin")
        self.TeacherTable.heading("religion", text="Agama")
        self.TeacherTable.heading("contact", text="No. HP")
        self.TeacherTable["show"] = "headings"

        self.TeacherTable.column("teacher_id", width=100)
        self.TeacherTable.column("name", width=100)
        self.TeacherTable.column("nip", width=100)
        self.TeacherTable.column("gender", width=100)
        self.TeacherTable.column("religion", width=100)
        self.TeacherTable.column("contact", width=100)

        self.TeacherTable.pack(fill=tk.BOTH, expand=1)
        self.TeacherTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()

    # ========================================================
    def clear(self):
        self.show()
        self.var_name.set("")
        self.var_nip.set("")
        self.var_gender.set("")
        self.var_religion.set("")
        self.var_contact.set("")
        self.txt_gender.set("Pilih")

    def delete(self):
        con = sqlite3.connect(database="rapot_siswa.db")
        cur = con.cursor()
        try:
            if self.var_name.get() == "":
                messagebox.showerror("Error", "Pilih salah satu guru", parent=self.root)
            else:
                cur.execute(
                    """SELECT
                        *
                        FROM
                        teacher
                        WHERE
                        teacher_id = ?""",
                    (self.var_teacherId.get(),),
                )
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror(
                        "Error",
                        "Pilih guru dari daftar yang sudah ada",
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
                            """DELETE FROM student
                                WHERE
                                teacher_id = ?""",
                            (self.var_teacherId.get(),),
                        )
                        con.commit()
                        messagebox.showinfo(
                            "Menghapus", "Guru berhasil dihapus", parent=self.root
                        )
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error", f"error dikarenakan {str(ex)}")

    def get_data(self, ev):
        self.txt_nip.config(state="readonly")
        r = self.TeacherTable.focus()
        content = self.TeacherTable.item(r)
        row = content["values"]
        if not row:
            return
        self.var_teacherId.set(row[0])
        self.var_name.set(row[1])
        self.var_nip.set(row[2])
        self.var_gender.set(row[3])
        self.var_religion.set(row[4])
        self.var_contact.set(row[5])

    def add(self):
        con = sqlite3.connect(database="rapot_siswa.db")
        cur = con.cursor()
        try:
            if self.var_name.get() == "":
                messagebox.showerror("Error", "Nama harus diisi", parent=self.root)
            else:
                cur.execute(
                    """SELECT
                        *
                        FROM
                        teacher
                        WHERE
                        name = ?""",
                    (self.var_name.get(),),
                )
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "Guru sudah ada", parent=self.root)
                else:
                    cur.execute(
                        """INSERT INTO
                            teacher (
                            
                            name,
                            nip,
                            gender,
                            religion,
                            contact
                            )
                            VALUES
                            (?, ?, ?, ?, ?)""",
                        (
                            self.var_name.get(),
                            self.var_nip.get(),
                            self.var_gender.get(),
                            self.var_religion.get(),
                            self.var_contact.get(),
                        ),
                    )
                    con.commit()
                    messagebox.showinfo(
                        "Berhasil", "Guru berhasil ditambahkan", parent=self.root
                    )
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"error dikarenakan {str(ex)}")

    def update(self):
        con = sqlite3.connect(database="rapot_siswa.db")
        cur = con.cursor()
        try:
            if self.var_name.get() == "":
                messagebox.showerror("Error", "Nama harus diisi", parent=self.root)
            else:
                cur.execute(
                    """SELECT
                        *
                        FROM
                        teacher
                        WHERE
                        teacher_id = ?""",
                    (self.var_teacherId.get(),),
                )
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror(
                        "Error",
                        "Pilih guru dari daftar yang sudah ada",
                        parent=self.root,
                    )
                else:
                    cur.execute(
                        """UPDATE teacher
                            SET
                            name = ?,
                            nip = ?,
                            gender = ?,
                            religion = ?,
                            contact = ?
                            WHERE
                            teacher_id = ?""",
                        (
                            self.var_name.get(),
                            self.var_nip.get(),
                            self.var_gender.get(),
                            self.var_religion.get(),
                            self.var_contact.get(),
                            self.var_teacherId.get(),
                        ),
                    )
                    con.commit()
                    messagebox.showinfo(
                        "Berhasil", "Guru berhasil diperbarui", parent=self.root
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
                teacher""")
            rows = cur.fetchall()
            self.TeacherTable.delete(*self.TeacherTable.get_children())
            for row in rows:
                self.TeacherTable.insert("", tk.END, values=row)

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
                    "Masukkan nama guru untuk mencari",
                    parent=self.root,
                )
                return

            cur.execute(
                """SELECT
                    *
                    FROM
                    teacher
                    WHERE
                    name LIKE ?""",
                (f"%{search_text}%",),
            )
            rows = cur.fetchall()
            if rows:
                self.TeacherTable.delete(*self.TeacherTable.get_children())
                for row in rows:
                    self.TeacherTable.insert("", tk.END, values=row)
            else:
                messagebox.showerror("Error", "Data tidak ditemukan", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error", f"error dikarenakan {str(ex)}")


if __name__ == "__main__":
    root = tk.Tk()
    obj = TeacherClass(root)
    root.mainloop()
