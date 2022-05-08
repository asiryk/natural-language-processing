from io import open
from conllu import parse_incr


def print_parsed():
    data_file = open("../ud_ukrainian/uk_iu-ud-dev.conllu", "r", encoding="utf-8")
    parsed_file = list(parse_incr(data_file))
    print(parsed_file[:3])


if __name__ == '__main__':
    print_parsed()
