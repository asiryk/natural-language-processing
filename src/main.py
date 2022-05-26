import os
from io import open

import numpy as np
import pandas as pd
from conllu import parse_tree_incr

from src.model import map_token_tree

UK_TOKENS_PATH = "./ud_ukrainian/uk_iu-ud-dev.conllu"
DIST_IMAGES_PATH = "./article/images/"


def create_data() -> pd.Series:
    ts = pd.Series(np.random.randn(1000), index=pd.date_range("1/1/2000", periods=1000))
    return ts


def save_chart(data: pd.Series, file_name: str = "figure.pdf"):
    fig = data.hist().get_figure()
    fig.savefig(os.path.join(DIST_IMAGES_PATH, file_name))


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
    # main()
    # save_chart(create_data())
    print(123)
