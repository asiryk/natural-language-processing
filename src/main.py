from io import open

from conllu import parse_tree_incr

from src.model import map_token_tree
from src.paths import UK_TOKENS_PATH


def main():
    data_file = open(UK_TOKENS_PATH, "r", encoding="utf-8")
    conllu_trees = list(parse_tree_incr(data_file))

    for sentence_tree in map(map_token_tree, conllu_trees):
        print(sentence_tree.metadata.get("text"), "\n")
        for node in sentence_tree.to_list():
            print("{:25}{}".format(node.token.get("form"), node.signature))

        print("-" * 100, "\n")

    print("Total trees processed: ", len(conllu_trees))


if __name__ == "__main__":
    main()
