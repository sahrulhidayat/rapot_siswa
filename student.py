import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import fonts


class StudentClass:
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
            text="Sesuaikan Detail Siswa",
            padx=10,
            compound=tk.LEFT,
            font=fonts.get_font(self.root, 18),
            bg="#0e4979",
            fg="white",
        )
        title.place(relx=0.01, y=15, relwidth=0.98, height=35)

        # ==== Variables ====
        self.var_nisn = tk.StringVar()
        self.var_name = tk.StringVar()
        self.var_gender = tk.StringVar()
        self.var_religion = tk.StringVar()
        self.var_contact = tk.StringVar()
        self.var_studyGroup = tk.StringVar()
        self.var_birthPlace = tk.StringVar()
        self.var_birthDate = tk.StringVar()
        self.var_father = tk.StringVar()
        self.var_mother = tk.StringVar()

        # ==== Widgets ====
        # -------- Column 1 --------
        lbl_nisn = tk.Label(
            self.root,
            text="NISN",
            font=fonts.get_font(self.root, 11),
            bg="white",
        ).place(relx=0.01, y=60)

        lbl_name = tk.Label(
            self.root,
            text="Nama",
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

        lbl_address = tk.Label(
            self.root,
            text="Alamat",
            font=fonts.get_font(self.root, 11),
            bg="white",
        ).place(relx=0.01, y=260)

        # ==== Entry Fields ====

        vcmd = (self.root.register(self.validate_numeric), "%P")

        self.txt_nisn = tk.Entry(
            self.root,
            textvariable=self.var_nisn,
            font=fonts.get_font(self.root, 11),
            bg="lightyellow",
            validate="key",
            validatecommand=vcmd,
        )
        self.txt_nisn.place(relx=0.125, y=60, relwidth=0.18)

        txt_name = tk.Entry(
            self.root,
            textvariable=self.var_name,
            font=fonts.get_font(self.root, 11),
            bg="lightyellow",
        ).place(relx=0.125, y=100, relwidth=0.18)

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

        # -------- Column 2 --------
        lbl_studyGroup = tk.Label(
            self.root,
            text="Rombel",
            font=fonts.get_font(self.root, 11),
            bg="white",
        ).place(relx=0.31, y=60)

        lbl_birthPlace = tk.Label(
            self.root,
            text="Tempat Lahir",
            font=fonts.get_font(self.root, 11),
            bg="white",
        ).place(relx=0.31, y=100)

        lbl_birthDate = tk.Label(
            self.root,
            text="Tanggal Lahir",
            font=fonts.get_font(self.root, 11),
            bg="white",
        ).place(relx=0.31, y=140)

        lbl_father = tk.Label(
            self.root,
            text="Ayah",
            font=fonts.get_font(self.root, 11),
            bg="white",
        ).place(relx=0.31, y=180)

        lbl_mother = tk.Label(
            self.root,
            text="Ibu",
            font=fonts.get_font(self.root, 11),
            bg="white",
        ).place(relx=0.31, y=220)

        # ==== Entry Fields ====
        self.studyGroup_list = []
        # function_call to update the list
        self.fetch_studyGroup()

        self.txt_studyGroup = ttk.Combobox(
            self.root,
            textvariable=self.var_studyGroup,
            values=self.studyGroup_list,
            font=fonts.get_font(self.root, 11),
            state="readonly",
            justify=tk.CENTER,
        )
        self.txt_studyGroup.place(relx=0.411, y=60, relwidth=0.18, height=24)
        self.txt_studyGroup.set("Pilih")

        txt_birthPlace = tk.Entry(
            self.root,
            textvariable=self.var_birthPlace,
            font=fonts.get_font(self.root, 11),
            bg="lightyellow",
        ).place(relx=0.411, y=100, relwidth=0.18)

        txt_birthDate = tk.Entry(
            self.root,
            textvariable=self.var_birthDate,
            font=fonts.get_font(self.root, 11),
            bg="lightyellow",
        ).place(relx=0.411, y=140, relwidth=0.18)

        txt_father = tk.Entry(
            self.root,
            textvariable=self.var_father,
            font=fonts.get_font(self.root, 11),
            bg="lightyellow",
        ).place(relx=0.411, y=180, relwidth=0.18)

        txt_mother = tk.Entry(
            self.root,
            textvariable=self.var_mother,
            font=fonts.get_font(self.root, 11),
            bg="lightyellow",
        ).place(relx=0.411, y=220, relwidth=0.18)

        # --------- Text Address ---------

        self.txt_address = tk.Text(
            self.root,
            font=fonts.get_font(self.root, 11),
            bg="lightyellow",
        )
        self.txt_address.place(relx=0.125, y=260, relwidth=0.465, relheight=0.208)

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
        lbl_search_student = tk.Label(
            self.root,
            text="Cari Siswa",
            font=fonts.get_font(self.root, 11),
            bg="white",
        ).place(relx=0.60, y=60)

        txt_search_student = tk.Entry(
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

        self.StudentTable = ttk.Treeview(
            self.C_Frame,
            columns=(
                "nisn",
                "name",
                "gender",
                "religion",
                "contact",
                "address",
                "study_group",
                "birth_place",
                "birth_date",
                "father",
                "mother",
            ),
            xscrollcommand=scrollx.set,
            yscrollcommand=scrolly.set,
        )
        scrollx.pack(side=tk.BOTTOM, fill=tk.X)
        scrolly.pack(side=tk.RIGHT, fill=tk.Y)
        scrollx.config(command=self.StudentTable.xview)
        scrolly.config(command=self.StudentTable.yview)

        self.StudentTable.heading("nisn", text="NISN")
        self.StudentTable.heading("name", text="Nama")
        self.StudentTable.heading("gender", text="Jenis Kelamin")
        self.StudentTable.heading("religion", text="Agama")
        self.StudentTable.heading("contact", text="No. HP")
        self.StudentTable.heading("address", text="Alamat")
        self.StudentTable.heading("study_group", text="Rombel")
        self.StudentTable.heading("birth_place", text="Tempat Lahir")
        self.StudentTable.heading("birth_date", text="Tanggal Lahir")
        self.StudentTable.heading("father", text="Ayah")
        self.StudentTable.heading("mother", text="Ibu")
        self.StudentTable["show"] = "headings"

        self.StudentTable.column("nisn", width=100)
        self.StudentTable.column("name", width=100)
        self.StudentTable.column("gender", width=100)
        self.StudentTable.column("religion", width=100)
        self.StudentTable.column("contact", width=100)
        self.StudentTable.column("address", width=100)
        self.StudentTable.column("study_group", width=100)
        self.StudentTable.column("birth_place", width=100)
        self.StudentTable.column("birth_date", width=100)
        self.StudentTable.column("father", width=100)
        self.StudentTable.column("mother", width=100)

        self.StudentTable.pack(fill=tk.BOTH, expand=1)
        self.StudentTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()

    # ========================================================
    def clear(self):
        self.show()
        self.var_nisn.set("")
        self.var_name.set("")
        self.var_gender.set("")
        self.var_religion.set("")
        self.var_contact.set("")
        self.txt_address.delete("1.0", tk.END)
        self.var_studyGroup.set("")
        self.var_birthPlace.set("")
        self.var_birthDate.set("")
        self.var_father.set("")
        self.var_mother.set("")
        self.txt_nisn.config(state=tk.NORMAL)
        self.var_search.set("")
        self.txt_gender.set("Pilih")
        self.txt_studyGroup.set("Pilih")

    def delete(self):
        con = sqlite3.connect(database="rapot_siswa.db")
        cur = con.cursor()
        try:
            if self.var_nisn.get() == "":
                messagebox.showerror(
                    "Error", "Pilih salah satu siswa", parent=self.root
                )
            else:
                cur.execute(
                    """SELECT
                        *
                        FROM
                        student
                        WHERE
                        nisn = ?""",
                    (self.var_nisn.get(),),
                )
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror(
                        "Error",
                        "Pilih siswa dari daftar yang sudah ada",
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
                                nisn = ?""",
                            (self.var_nisn.get(),),
                        )
                        con.commit()
                        messagebox.showinfo(
                            "Menghapus", "Siswa berhasil dihapus", parent=self.root
                        )
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error", f"error dikarenakan {str(ex)}")

    def get_data(self, ev):
        self.txt_nisn.config(state="readonly")
        selected = self.StudentTable.selection()
        if not selected:
            return
        item_id = selected[0]
        row = self.StudentTable.item(item_id, "values")
        if not row:
            return
        self.var_nisn.set(row[0])
        self.var_name.set(row[1])
        self.var_gender.set(row[2])
        self.var_religion.set(row[3])
        self.var_contact.set(row[4])
        self.txt_address.delete("1.0", tk.END)
        self.txt_address.insert(tk.END, row[5])
        self.var_studyGroup.set(row[6])
        self.var_birthPlace.set(row[7])
        self.var_birthDate.set(row[8])
        self.var_father.set(row[9])
        self.var_mother.set(row[10])

    def add(self):
        con = sqlite3.connect(database="rapot_siswa.db")
        cur = con.cursor()
        try:
            if self.var_nisn.get() == "" or self.var_name.get().strip() == "":
                messagebox.showerror(
                    "Error", "NISN dan Nama harus diisi", parent=self.root
                )
            else:
                cur.execute(
                    """SELECT
                        *
                        FROM
                        student
                        WHERE
                        nisn = ?""",
                    (self.var_nisn.get(),),
                )
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "NISN sudah ada", parent=self.root)
                else:
                    cur.execute(
                        """INSERT INTO
                            student (
                            nisn,
                            name,
                            gender,
                            religion,
                            contact,
                            address,
                            study_group,
                            birth_place,
                            birth_date,
                            father,
                            mother
                            )
                            VALUES
                            (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                        (
                            self.var_nisn.get(),
                            self.var_name.get(),
                            self.var_gender.get(),
                            self.var_religion.get(),
                            self.var_contact.get(),
                            self.txt_address.get("1.0", tk.END),
                            self.var_studyGroup.get(),
                            self.var_birthPlace.get(),
                            self.var_birthDate.get(),
                            self.var_father.get(),
                            self.var_mother.get(),
                        ),
                    )
                    con.commit()
                    messagebox.showinfo(
                        "Berhasil", "Siswa berhasil ditambahkan", parent=self.root
                    )
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"error dikarenakan {str(ex)}")

    def update(self):
        con = sqlite3.connect(database="rapot_siswa.db")
        cur = con.cursor()
        try:
            if self.var_nisn.get() == "" or self.var_name.get().strip() == "":
                messagebox.showerror(
                    "Error", "NISN dan Nama harus diisi", parent=self.root
                )
            else:
                cur.execute(
                    """SELECT
                        *
                        FROM
                        student
                        WHERE
                        nisn = ?""",
                    (self.var_nisn.get(),),
                )
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror(
                        "Error",
                        "Pilih siswa dari daftar yang sudah ada",
                        parent=self.root,
                    )
                else:
                    cur.execute(
                        """UPDATE student
                            SET
                            name = ?,
                            gender = ?,
                            religion = ?,
                            contact = ?,
                            address = ?,
                            study_group = ?,
                            birth_place = ?,
                            birth_date = ?,
                            father = ?,
                            mother = ?
                            WHERE
                            nisn = ?""",
                        (
                            self.var_name.get(),
                            self.var_gender.get(),
                            self.var_religion.get(),
                            self.var_contact.get(),
                            self.txt_address.get("1.0", tk.END),
                            self.var_studyGroup.get(),
                            self.var_birthPlace.get(),
                            self.var_birthDate.get(),
                            self.var_father.get(),
                            self.var_mother.get(),
                            self.var_nisn.get(),
                        ),
                    )
                    con.commit()
                    messagebox.showinfo(
                        "Berhasil", "Siswa berhasil diperbarui", parent=self.root
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
                student""")
            rows = cur.fetchall()
            self.StudentTable.delete(*self.StudentTable.get_children())
            for row in rows:
                self.StudentTable.insert("", tk.END, values=row)

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

    def search(self):
        con = sqlite3.connect(database="rapot_siswa.db")
        cur = con.cursor()
        try:
            search_text = self.var_search.get().strip()
            if search_text == "":
                messagebox.showerror(
                    "Error",
                    "Masukkan nama siswa untuk mencari",
                    parent=self.root,
                )
                return

            cur.execute(
                """SELECT
                    *
                    FROM
                    student
                    WHERE
                    name LIKE ?""",
                (f"%{search_text}%",),
            )
            rows = cur.fetchall()
            if rows:
                self.StudentTable.delete(*self.StudentTable.get_children())
                for row in rows:
                    self.StudentTable.insert("", tk.END, values=row)
            else:
                messagebox.showerror("Error", "Data tidak ditemukan", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error", f"error dikarenakan {str(ex)}")

    def validate_numeric(self, value):
        return value.isdigit() or value == ""


if __name__ == "__main__":
    root = tk.Tk()
    obj = StudentClass(root)
    root.mainloop()
