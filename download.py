import datetime
from pathlib import Path

import requests


def download_jobs_html() -> dict:
    url = "https://vk.com/jobs"
    params = {
        "category": "jobs_cat_all",
        "list_only": 1,
    }
    data = {
        "al": 1,
    }
    headers = {"x-requested-with": "XMLHttpRequest"}

    r = requests.post(url, params=params, data=data, headers=headers)

    return r.json()


def parse_jobs_html(response: dict) -> str:
    return response["payload"][1][0]


def html_unescape(html_raw: str) -> str:
    replace = [
        ("\\n", "\n"),
        ("</a><a", "</a>\n<a"),
        ('\\"', '"'),
        ("&#8203;", " "),
        ('>"', ">"),
        ('"<', "<"),
    ]

    for old, new in replace:
        html_raw = html_raw.replace(old, new)

    return html_raw


def main() -> None:
    path = Path(f"jobs/jobs-{datetime.date.today()}.html")
    if path.exists():
        exit(f"Файл '{path.name}' уже существует")

    response = download_jobs_html()
    html_jobs = parse_jobs_html(response)
    html_jobs = html_unescape(html_jobs)

    path.write_text(html_jobs, encoding="utf-8")
    print(f"Файл '{path.name}' успешно скачен")
