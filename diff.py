import database


def main(date_from: str, date_to: str) -> None:
    print(f"Разница между: '{date_from}' и '{date_to}'")

    jobs_from = set(database.get_jobs_from_date(date_from))
    jobs_to = set(database.get_jobs_from_date(date_to))

    print("> Удалённые вакансии <")
    for del_job in jobs_from - jobs_to:
        print("DEL", del_job)

    print()

    print("> Новые вакансии <")
    for new_job in jobs_to - jobs_from:
        print("NEW", new_job)
