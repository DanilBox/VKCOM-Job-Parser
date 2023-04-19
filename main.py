import argparse
import sys

import diff
import download
import parse


def main(argv: list[str]) -> None:
    parser = argparse.ArgumentParser(description="Парсер вакансий ВКонтакте")
    subparsers = parser.add_subparsers()

    download_parser = subparsers.add_parser("download", help="Скачать список вакансий")
    download_parser.set_defaults(func=download.main)

    parse_parser = subparsers.add_parser("parse", help="Спарсить список вакансий")
    parse_parser.set_defaults(func=parse.main)

    diff_parser = subparsers.add_parser("diff", help="Найти разницу в вакансиях")
    diff_parser.add_argument("--from", dest="date_from", type=str, required=True, help="первая дата")
    diff_parser.add_argument("--to", dest="date_to", type=str, required=True, help="вторая дата")
    diff_parser.set_defaults(func=diff.main)

    if len(argv) == 0:
        parser.print_help()
        exit()

    args = parser.parse_args(argv)
    attr = {k: v for k, v in vars(args).items() if not callable(v)}
    if len(attr) == 0:
        args.func()
    else:
        args.func(**attr)


if __name__ == "__main__":
    main(sys.argv[1::])
