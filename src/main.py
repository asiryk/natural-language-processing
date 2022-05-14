from io import open

from conllu import parse_incr

from src.model import traverse
from src.paths import UK_TOKENS_PATH


def print_parsed():
    data_file = open(UK_TOKENS_PATH, "r", encoding="utf-8")
    parsed_file = list(parse_incr(data_file))
    print(len(parsed_file))

    tree, _ = traverse(parsed_file[0].to_tree())
    print(tree.get_token("upos"), tree.depth, tree.height)


if __name__ == "__main__":
    print_parsed()
