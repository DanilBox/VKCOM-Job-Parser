import datetime
from pathlib import Path

from bs4 import BeautifulSoup

import database
from job_model import Job


def parse_html(date: str) -> list[Job]:
    html_file = Path(f"jobs/jobs-{date}.html")
    html_data = html_file.read_text(encoding="utf-8")

    soup = BeautifulSoup(html_data, "lxml")

    html_jobs = soup.find_all("a", attrs={"class": "JobThumb"})

    jobs: list[Job] = []
    for html_job in html_jobs:
        job = Job(
            href=html_job.attrs["href"],
            title=html_job.find("h3", attrs={"class": "JobThumb__title"}).text,
            category=html_job.find("p", attrs={"class": "JobThumb__category"}).text,
            description=html_job.find("p", attrs={"class": "JobThumb__description"}).text,
        )
        jobs.append(job)

    return jobs


def main(date: str = str(datetime.date.today())) -> None:
    database.prepare()

    jobs = parse_html(date)
    database.save_db(jobs)
    print(f"Вакансии за {date} успешно спарсены")
