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

        # ===== Result Labels =======
        self.var_studyGroup = tk.StringVar()
        self.var_nisn = tk.StringVar()
        self.var_groupId = tk.StringVar()
        self.number = tk.StringVar()
        self.study = tk.StringVar()
        self.criteria = tk.StringVar()
        self.mark = tk.StringVar()
        self.explain = tk.StringVar()

        self.studyGroup_list = []
        self.student_list = []
        self.nisn_list = []

        # ===== Fetch Data =====
        self.fetch_studyGroup()

        # ============ Canvas ==========

        scroll_wrap = tk.Frame(self.root, bg="white")
        scroll_wrap.pack(side="top", fill="both", expand=True)

        self.canvas = tk.Canvas(scroll_wrap, bg="white", highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(
            scroll_wrap, orient="vertical", command=self.canvas.yview
        )
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        self.content = tk.Frame(self.canvas, bg="white")
        self.content.pack_propagate(False)
        self.content_window = self.canvas.create_window(
            (0, 0), window=self.content, anchor="nw"
        )

        self.canvas.bind(
            "<Configure>",
            lambda event: (
                self.canvas.itemconfig(self.content_window, width=event.width),
                self.content.config(width=event.width),
            ),
        )

        self.canvas.bind("<Enter>", self._bind_mousewheel)
        self.canvas.bind("<Leave>", self._unbind_mousewheel)

        # ----- Title -----

        self.title_height = 65

        title = tk.Label(
            self.content,
            text="Rapot Hasil Belajar Siswa",
            padx=10,
            compound=tk.LEFT,
            font=fonts.get_font(self.root, 16),
            bg="orange",
            fg="#262626",
        )
        title.place(relx=0.01, y=15, relwidth=0.98, height=35)

        # ----- Form: Rombel / Nama / NISN -----

        lbl_studyGroup = tk.Label(
            self.content,
            text="Rombel",
            font=fonts.get_font(self.root, 11, "bold"),
            bg="white",
        ).place(relx=0.125, y=self.title_height + 20)

        lbl_student = tk.Label(
            self.content,
            text="Nama",
            font=fonts.get_font(self.root, 11, "bold"),
            bg="white",
        ).place(relx=0.125, y=self.title_height + 54)

        lbl_nisn = tk.Label(
            self.content,
            text="NISN",
            font=fonts.get_font(self.root, 11, "bold"),
            bg="white",
        ).place(relx=0.125, y=self.title_height + 88)

        self.txt_studyGroup = ttk.Combobox(
            self.content,
            values=self.studyGroup_list,
            textvariable=self.var_studyGroup,
            font=fonts.get_font(self.root, 11),
            style="Custom.TCombobox",
            state="readonly",
        )
        self.txt_studyGroup.place(
            relx=0.200, y=self.title_height + 18, relwidth=0.20, height=28
        )
        self.txt_studyGroup.set("Pilih")
        self.txt_studyGroup.bind(
            "<<ComboboxSelected>>", lambda event: self.fetch_student()
        )

        self.txt_student = ttk.Combobox(
            self.content,
            values=self.student_list,
            textvariable=tk.StringVar(),
            font=fonts.get_font(self.root, 11),
            style="Custom.TCombobox",
            state="readonly",
        )
        self.txt_student.place(
            relx=0.200, y=self.title_height + 52, relwidth=0.20, height=28
        )
        self.txt_student.set("Pilih")
        self.txt_student.bind("<<ComboboxSelected>>", self.on_student_selected)

        txt_nisn = tk.Entry(
            self.content,
            textvariable=self.var_nisn,
            font=fonts.get_font(self.root, 11),
            state="readonly",
        ).place(relx=0.200, y=self.title_height + 86, relwidth=0.20, height=28)

        # ----- Header tabel -----

        header_y = self.title_height + 140
        self.header_height = 40

        lbl_number = tk.Label(
            self.content,
            text="No.",
            font=fonts.get_font(self.root, 11, "bold"),
            bg="white",
            bd=2,
            relief=tk.GROOVE,
        ).place(relx=0.125, y=header_y, relwidth=0.075, height=self.header_height)

        lbl_study = tk.Label(
            self.content,
            text="Pelajaran",
            font=fonts.get_font(self.root, 11, "bold"),
            bg="white",
            bd=2,
            relief=tk.GROOVE,
        ).place(relx=0.200, y=header_y, relwidth=0.300, height=self.header_height)

        lbl_criteria = tk.Label(
            self.content,
            text="KKM",
            font=fonts.get_font(self.root, 11, "bold"),
            bg="white",
            bd=2,
            relief=tk.GROOVE,
        ).place(relx=0.5, y=header_y, relwidth=0.125, height=self.header_height)

        lbl_mark = tk.Label(
            self.content,
            text="Nilai",
            font=fonts.get_font(self.root, 11, "bold"),
            bg="white",
            bd=2,
            relief=tk.GROOVE,
        ).place(relx=0.625, y=header_y, relwidth=0.125, height=self.header_height)

        lbl_explain = tk.Label(
            self.content,
            text="Keterangan",
            font=fonts.get_font(self.root, 11, "bold"),
            bg="white",
            bd=2,
            relief=tk.GROOVE,
        ).place(relx=0.75, y=header_y, relwidth=0.125, height=self.header_height)

        # ----- Area baris data tabel  -----

        self.result_area_start = header_y + self.header_height
        self.row_height = 40

        self.result_rows = []

        self._update_content_height(0)

    def _update_content_height(self, row_count):
        total_height = self.result_area_start + row_count * self.row_height + 20
        self.content.config(height=total_height)
        # update_idletasks supaya bbox("all") langsung akurat, tidak menunggu
        # event loop berikutnya
        self.canvas.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def _bind_mousewheel(self, event=None):
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)
        # Linux (X11) scroll events
        self.canvas.bind_all("<Button-4>", self._on_mousewheel)
        self.canvas.bind_all("<Button-5>", self._on_mousewheel)

    def _unbind_mousewheel(self, event=None):
        self.canvas.unbind_all("<MouseWheel>")
        self.canvas.unbind_all("<Button-4>")
        self.canvas.unbind_all("<Button-5>")

    def _on_mousewheel(self, event):
        if event.num == 4:
            self.canvas.yview_scroll(-1, "units")
        elif event.num == 5:
            self.canvas.yview_scroll(1, "units")
        else:
            self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def clear_result_rows(self):
        for row_widgets in self.result_rows:
            for widget in row_widgets:
                widget.destroy()
        self.result_rows.clear()
        self._update_content_height(0)
        self.canvas.yview_moveto(0)

    def add_result_row(self, index, study_name, kkm, mark, explain_text):
        y = self.result_area_start + index * self.row_height

        number = tk.Label(
            self.content,
            text=str(index + 1),
            font=fonts.get_font(self.root, 11, "bold"),
            bg="white",
            bd=2,
            relief=tk.GROOVE,
        )
        number.place(relx=0.125, y=y, relwidth=0.075, height=self.row_height)

        study = tk.Label(
            self.content,
            text=study_name,
            font=fonts.get_font(self.root, 11, "bold"),
            bg="white",
            bd=2,
            relief=tk.GROOVE,
            anchor="w",
            padx=10,
        )
        study.place(relx=0.200, y=y, relwidth=0.300, height=self.row_height)

        criteria = tk.Label(
            self.content,
            text=kkm,
            font=fonts.get_font(self.root, 11, "bold"),
            bg="white",
            bd=2,
            relief=tk.GROOVE,
        )
        criteria.place(relx=0.5, y=y, relwidth=0.125, height=self.row_height)

        mark_label = tk.Label(
            self.content,
            text=mark,
            font=fonts.get_font(self.root, 11, "bold"),
            bg="white",
            bd=2,
            relief=tk.GROOVE,
        )
        mark_label.place(relx=0.625, y=y, relwidth=0.125, height=self.row_height)

        explain = tk.Label(
            self.content,
            text=explain_text,
            font=fonts.get_font(self.root, 11, "bold"),
            bg="white",
            bd=2,
            relief=tk.GROOVE,
            anchor="center",
        )
        explain.place(relx=0.75, y=y, relwidth=0.125, height=self.row_height)

        self._update_content_height(index + 1)

        self.result_rows.append((number, study, criteria, mark_label, explain))

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

    def fetch_student_results(self, nisn):
        self.clear_result_rows()

        if not nisn:
            return

        con = sqlite3.connect(database="rapot_siswa.db")
        cur = con.cursor()
        try:
            cur.execute(
                """SELECT
                    study,
                    kkm,
                    mark
                    FROM
                    RESULT
                    WHERE
                    nisn = ?""",
                (nisn,),
            )
            rows = cur.fetchall()
            if rows:
                for index, row in enumerate(rows):
                    study_name = row[0]
                    kkm = row[1]
                    mark = row[2]
                    mark_value = int(mark)
                    if mark_value < int(kkm):
                        explain_text = "Kurang"
                    elif mark_value < int(kkm) + 5:
                        explain_text = "Cukup"
                    elif mark_value < int(kkm) + 15:
                        explain_text = "Baik"
                    else:
                        explain_text = "Sangat Baik"

                    self.add_result_row(index, study_name, kkm, mark, explain_text)

        except Exception as ex:
            messagebox.showerror("Error", f"error dikarenakan {str(ex)}")
        finally:
            con.close()

    def on_student_selected(self, event=None):
        selected_index = self.txt_student.current()
        if selected_index < 0:
            return

        self.var_nisn.set(self.nisn_list[selected_index])
        self.fetch_student_results(self.var_nisn.get())


if __name__ == "__main__":
    root = tk.Tk()
    obj = ReportClass(root)
    root.mainloop()
