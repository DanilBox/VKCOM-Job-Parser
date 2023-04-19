import datetime
from typing import NamedTuple


class Job(NamedTuple):
    href: str
    title: str
    category: str
    description: str
    date: str = datetime.date.today()

    def __hash__(self) -> int:
        return hash((self.href, self.title, self.category, self.description))

    def __eq__(self, other) -> bool:
        return (
            self.href == other.href
            and self.title == other.title
            and self.category == other.category
            and self.description == other.description
        )

    def __str__(self) -> str:
        return f"{self.title} - {self.category} => '{self.href}' ({self.date})"
