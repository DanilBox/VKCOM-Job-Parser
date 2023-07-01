import sqlite3
from functools import cache
from pathlib import Path
from sqlite3 import Connection

from job_model import Job

DATABASE_NAME = "job_database.db"
SQL_FOLDER = "sql"


def get_sql_from_file(filename: str) -> str:
    sql_file = Path.cwd() / SQL_FOLDER / f"{filename}.sql"
    return sql_file.read_text(encoding="utf-8")


@cache
def get_connect() -> Connection:
    return sqlite3.connect(DATABASE_NAME)


def prepare() -> None:
    conn = get_connect()
    cursor = conn.cursor()

    sql = get_sql_from_file("create_table_jobs")
    cursor.execute(sql)


def save_db(jobs: list[Job]) -> None:
    conn = get_connect()
    cursor = conn.cursor()

    sql = get_sql_from_file("insert_new_jobs")
    cursor.executemany(sql, jobs)
    conn.commit()


def get_jobs_from_date(date: str) -> list[Job]:
    conn = get_connect()
    cursor = conn.cursor()

    sql = get_sql_from_file("select_jobs")
    cursor.execute(sql, (date,))

    jobs = cursor.fetchall()
    return [Job(*job) for job in jobs]
