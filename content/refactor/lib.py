import os
from typing import Iterable, Generator


class Config:
    def __init__(self, query: str, file_path: str, ignore_case: bool):
        self.query = query
        self.file_path = file_path
        self.ignore_case = ignore_case


def parse_config(argv: list[str]) -> Config:
    try:
        query = argv[1]
    except IndexError:
        raise IndexError("Didn't get a query string")

    try:
        file_path = argv[2]
    except IndexError:
        raise IndexError("Didn't get a file path")

    ignore_case = bool(os.environ.get("IGNORE_CASE", ""))
    return Config(query, file_path, ignore_case)


def search(query: str, contents: Iterable) -> Generator[str, None, None]:
    for line in contents:
        line = line.rstrip("\r\n")
        if query in line:
            yield line


def search_case_insensitive(
    query: str, contents: Iterable
) -> Generator[str, None, None]:
    query = query.lower()
    for line in contents:
        line = line.rstrip("\r\n")
        if query in line.lower():
            yield line


def run(config: Config):
    with open(config.file_path) as f:
        if config.ignore_case:
            result = search_case_insensitive(config.query, f)
        else:
            result = search(config.query, f)

        for line in result:
            print(line)
