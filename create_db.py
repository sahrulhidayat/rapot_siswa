import sqlite3


def create_db():
    con = sqlite3.connect(database="rapot_siswa.db")
    cur = con.cursor()
    cur.execute(
        """CREATE TABLE IF NOT EXISTS study (
            study_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name text,
            study_group text,
            teacher text,
            description text
            )"""
    )
    con.commit()

    cur.execute(
        """CREATE TABLE IF NOT EXISTS student (
            nisn INTEGER PRIMARY KEY AUTOINCREMENT,
            name text,
            gender text,
            religion text,
            contact text,
            address text,
            study_group text,
            birth_place text,
            birth_date text,
            father text,
            mother text
            )"""
    )
    con.commit()

    cur.execute(
        """CREATE TABLE IF NOT EXISTS teacher (
            teacher_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name text,
            nip text,
            gender text,
            religion text,
            contact text
            )"""
    )
    con.commit()

    cur.execute(
        """CREATE TABLE IF NOT EXISTS studyGroup (
            group_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name text,
            class text,
            guardian_teacher text
            )"""
    )
    con.commit()

    cur.execute(
        """CREATE TABLE IF NOT EXISTS result (
            result_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student text,
            nisn text,
            study text,
            kkm text,
            mark text
            )"""
    )
    con.commit()

    con.close()


create_db()
