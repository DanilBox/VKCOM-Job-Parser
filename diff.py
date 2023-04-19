import database


def main(date_from: str, date_to: str) -> None:
    print(date_from, date_to)

    jobs_from = set(database.get_jobs_from_date(date_from))
    jobs_to = set(database.get_jobs_from_date(date_to))

    new_jobs = jobs_to - jobs_from
    del_jobs = jobs_from - jobs_to

    print("> Удалённые вакансии <")
    for del_job in del_jobs:
        print("DEL", del_job)

    print()

    print("> Новые вакансии <")
    for new_job in new_jobs:
        print("NEW", new_job)
