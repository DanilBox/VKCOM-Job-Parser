CREATE TABLE IF NOT EXISTS jobs
(
    href        TEXT,
    title       TEXT,
    category    TEXT,
    description TEXT,
    date        TEXT,
    UNIQUE (href, title, category, description, date)
);
