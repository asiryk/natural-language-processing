from io import open

from conllu import parse_incr

from src.paths import UK_TOKENS_PATH


def print_parsed():
    data_file = open(UK_TOKENS_PATH, "r", encoding="utf-8")
    parsed_file = list(parse_incr(data_file))
    sentence_tokens = parsed_file[0]
    word_token = sentence_tokens[0]
    print(word_token["upos"])


if __name__ == "__main__":
    print_parsed()
