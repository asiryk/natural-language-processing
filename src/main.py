from io import open

from conllu import parse_incr

from src.model import traverse
from src.paths import UK_TOKENS_PATH


def main():
    data_file = open(UK_TOKENS_PATH, "r", encoding="utf-8")
    parsed_file = list(parse_incr(data_file))
    print(len(parsed_file))

    tree = traverse(parsed_file[0].to_tree())
    print(tree.signature)


if __name__ == "__main__":
    main()
