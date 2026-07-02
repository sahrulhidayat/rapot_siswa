import tkinter as tk
from PIL import Image, ImageTk
import fonts
from study_group import StudyGroupClass
from study import StudyClass
from student import StudentClass
from result import ResultClass
from teacher import TeacherClass
from report import ReportClass


class StudentReport:
    def __init__(self, root):
        self.root = root
        self.root.title("")
        self.root.geometry("1366x768+0+0")
        self.root.config(bg="white")

        try:
            root.state("zoomed")
        except tk.TclError:
            pass

        self.study_group_win = None
        self.study_win = None
        self.student_win = None
        self.teacher_win = None
        self.result_win = None
        self.report_win = None

        # ===== Icons =====
        self.logo_dash = ImageTk.PhotoImage(Image.open("images/logo_dash.png"))

        # ===== Title =====
        title = tk.Label(
            self.root,
            text="Sistem Rapot Siswa",
            padx=10,
            compound=tk.LEFT,
            image=self.logo_dash,
            font=fonts.get_font(self.root, 18),
            bg="#0e4979",
            fg="white",
        )
        title.place(x=0, y=0, relwidth=1)

        # ==== Menu ====
        M_Frame = tk.LabelFrame(
            self.root, text="Menu", font=fonts.get_font(self.root, 13), bg="white"
        )
        M_Frame.place(x=10, y=70, width=1346, height=80)

        btn_groupStudy = tk.Button(
            M_Frame,
            text="Rombel",
            font=fonts.get_font(self.root, 13),
            bg="#0f7c8f",
            fg="white",
            cursor="hand2",
            command=self.add_studyGroup,
        )
        btn_groupStudy.place(x=20, y=5, width=200, height=40)

        btn_study = tk.Button(
            M_Frame,
            text="Pelajaran",
            font=fonts.get_font(self.root, 13),
            bg="#0f7c8f",
            fg="white",
            cursor="hand2",
            command=self.add_study,
        )
        btn_study.place(x=240, y=5, width=200, height=40)

        btn_student = tk.Button(
            M_Frame,
            text="Siswa",
            font=fonts.get_font(self.root, 13),
            bg="#0f7c8f",
            fg="white",
            cursor="hand2",
            command=self.add_student,
        )
        btn_student.place(x=460, y=5, width=200, height=40)

        btn_teacher = tk.Button(
            M_Frame,
            text="Guru",
            font=fonts.get_font(self.root, 13),
            bg="#0f7c8f",
            fg="white",
            cursor="hand2",
            command=self.add_teacher,
        )
        btn_teacher.place(x=680, y=5, width=200, height=40)

        btn_result = tk.Button(
            M_Frame,
            text="Input Rapot",
            font=fonts.get_font(self.root, 13),
            bg="#0f7c8f",
            fg="white",
            cursor="hand2",
            command=self.add_result,
        )
        btn_result.place(x=900, y=5, width=200, height=40)

        btn_report = tk.Button(
            M_Frame,
            text="Rapot Siswa",
            font=fonts.get_font(self.root, 13),
            bg="#0f7c8f",
            fg="white",
            cursor="hand2",
            command=self.view_report,
        )
        btn_report.place(x=1120, y=5, width=200, height=40)

        # ==== Footer ====
        footer = tk.Label(
            self.root,
            text="Sistem Rapot Siswa | v0.01 2026",
            font=fonts.get_font(self.root, 11),
            bg="#262626",
            fg="white",
        )
        footer.pack(side=tk.BOTTOM, fill=tk.X)

        # ==== Content Window ====
        self.bg_img = Image.open("images/bg.png")
        self.bg_img = self.bg_img.resize((1366, 768), Image.Resampling.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg = tk.Label(self.root, image=self.bg_img)
        self.lbl_bg.place(x=0, y=50, width=1366, height=768)
        self.lbl_bg.lower()

        # ==== Update Details ====
        self.lbl_study = tk.Label(
            self.root,
            text="Total Pelajaran\n[ 0 ]",
            font=fonts.get_font(self.root, 18),
            bd=5,
            relief=tk.RIDGE,
            bg="#da590f",
            fg="white",
        ).place(x=400, y=530, width=300, height=100)

        self.lbl_student = tk.Label(
            self.root,
            text="Total Pelajaran\n[ 0 ]",
            font=fonts.get_font(self.root, 18),
            bd=5,
            relief=tk.RIDGE,
            bg="#05b63a",
            fg="white",
        ).place(x=710, y=530, width=300, height=100)

        self.lbl_result = tk.Label(
            self.root,
            text="Total Pelajaran\n[ 0 ]",
            font=fonts.get_font(self.root, 18),
            bd=5,
            relief=tk.RIDGE,
            bg="#0584b6",
            fg="white",
        ).place(x=1020, y=530, width=300, height=100)

    def add_studyGroup(self):
        if self.study_group_win is None or not self.study_group_win.winfo_exists():
            self.study_group_win = tk.Toplevel(self.root)
            self.new_obj = StudyGroupClass(self.study_group_win)
        else:
            self.study_group_win.lift()

    def add_study(self):
        if self.study_win is None or not self.study_win.winfo_exists():
            self.study_win = tk.Toplevel(self.root)
            self.new_obj = StudyClass(self.study_win)
        else:
            self.study_win.lift()

    def add_student(self):
        if self.student_win is None or not self.student_win.winfo_exists():
            self.student_win = tk.Toplevel(self.root)
            self.new_obj = StudentClass(self.student_win)
        else:
            self.student_win.lift()

    def add_teacher(self):
        if self.teacher_win is None or not self.teacher_win.winfo_exists():
            self.teacher_win = tk.Toplevel(self.root)
            self.new_obj = TeacherClass(self.teacher_win)
        else:
            self.teacher_win.lift()

    def add_result(self):
        if self.result_win is None or not self.result_win.winfo_exists():
            self.result_win = tk.Toplevel(self.root)
            self.new_obj = ResultClass(self.result_win)
        else:
            self.result_win.lift()

    def view_report(self):
        if self.report_win is None or not self.report_win.winfo_exists():
            self.report_win = tk.Toplevel(self.root)
            self.new_obj = ReportClass(self.report_win)
        else:
            self.report_win.lift()


if __name__ == "__main__":
    root = tk.Tk()
    obj = StudentReport(root)
    root.mainloop()
