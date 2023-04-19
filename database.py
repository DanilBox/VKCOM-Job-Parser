import sqlite3
from pathlib import Path

from job_model import Job

DATABASE_NAME = "job_database.db"
SQL_FOLDER = "sql"


def get_sql_from_file(filename: str) -> str:
    sql_file = Path.cwd() / SQL_FOLDER / f"{filename}.sql"
    return sql_file.read_text(encoding="utf-8")


def prepare() -> None:
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    sql = get_sql_from_file("create_table_jobs")
    cursor.execute(sql)


def save_db(jobs: list[Job]) -> None:
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    sql = get_sql_from_file("insert_new_jobs")
    cursor.executemany(sql, jobs)
    conn.commit()


def get_jobs_from_date(date: str) -> list[Job]:
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    sql = get_sql_from_file("select_jobs")
    cursor.execute(sql, (date,))

    rr = cursor.fetchall()
    return [Job(*item) for item in rr]
