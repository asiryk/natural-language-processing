from io import open

from conllu import parse_incr

from src.paths import UK_TOKENS_PATH


def print_parsed():
    data_file = open(UK_TOKENS_PATH, "r", encoding="utf-8")
    parsed_file = list(parse_incr(data_file))
    print(parsed_file[:3])


if __name__ == '__main__':
    print_parsed()
