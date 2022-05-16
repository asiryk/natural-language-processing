from io import open

from conllu import parse_tree_incr

from src.model import map_token_tree
from src.paths import UK_TOKENS_PATH


def main():
    data_file = open(UK_TOKENS_PATH, "r", encoding="utf-8")
    conllu_trees = list(parse_tree_incr(data_file))
    print(len(conllu_trees))

    tree = map_token_tree(conllu_trees[0])
    print(tree.signature)


if __name__ == "__main__":
    main()
