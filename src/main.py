import io
import os
import re
import sys
from typing import List

import numpy as np
import pandas as pd
from conllu import parse_tree_incr

from src.model import map_token_tree, SigType, Signature, ParseTree

UK_DEV_PATH = "./ud_ukrainian/uk_iu-ud-dev.conllu"
UK_TRAIN_PATH = "./ud_ukrainian/uk_iu-ud-dev.conllu"
UK_TEST_PATH = "./ud_ukrainian/uk_iu-ud-dev.conllu"
ES_DEV_PATH = "./ud_spanish/es_gsd-ud-dev.conllu"
ES_TRAIN_PATH = "./ud_spanish/es_gsd-ud-train.conllu"
ES_TEST_PATH = "./ud_spanish/es_gsd-ud-test.conllu"
DIST_IMAGES_PATH = "./article/images/"


def get_token_trees(path_dev: str, path_train: str, path_test: str) -> List[ParseTree]:
    def file_to_trees(file) -> List[ParseTree]: return list(map(map_token_tree, list(parse_tree_incr(file))))

    dev = io.open(path_dev, "r", encoding="utf-8")
    train = io.open(path_train, "r", encoding="utf-8")
    test = io.open(path_test, "r", encoding="utf-8")

    return [*file_to_trees(dev), *file_to_trees(train), *file_to_trees(test)]


def save_chart(chart, file_name: str = "figure.pdf"):
    chart.figure.savefig(os.path.join(DIST_IMAGES_PATH, file_name))


def freq(items: List[str]) -> pd.DataFrame:
    frequencies = {}
    for i in items:
        count = frequencies.get(i, 0)
        frequencies[i] = count + 1
    for i in frequencies:
        frequencies[i] = (frequencies[i], frequencies[i] / len(items))

    values = np.array([v[0] for v in frequencies.values()])
    names = np.array([k for k in frequencies.keys()])
    df = pd.DataFrame(values, index=names).sort_values(by=0, ascending=False)
    df[1] = [df[0][0] / ind for ind in np.arange(1, len(frequencies) + 1)]
    df.columns = ["Отриманий розподіл", "Розподіл Зіпфа"]
    return df


def sig_sentence(sentence: List[Signature]):
    types = {}
    for sig in sentence:
        amount = types.get(sig.type, 0)
        types[sig.type] = amount + 1

    return f"w{types.get(SigType.W, 0)},d{types.get(SigType.D, 0)},n{types.get(SigType.N)}"


def process(treebank: List[ParseTree], lang: str):
    sentences = [[tree.signature for tree in sentence_tree.to_list()] for sentence_tree in treebank]
    signatures = [signature for signatures in sentences for signature in signatures]

    deprel = [sig.node[0] for sig in signatures]
    upos = [sig.node[1] for sig in signatures]
    deprel_upos = [f"{sig.node[0]}+{sig.node[1]}" for sig in signatures]
    type_w = [f"{sig.type},{sig.sentence_id}" for sig in signatures if sig.type == SigType.W]
    type_d = [f"{sig.type},{sig.height},{sig.subtree_type}" for sig in signatures if sig.type == SigType.D]
    type_upos = [f"{sig.type}+{sig.node[1]}" for sig in signatures]
    sent_d_w_n = [sig for sig in map(sig_sentence, sentences)]

    freq_deprel = freq(deprel)
    freq_upos = freq(upos)
    freq_deprel_upos = freq(deprel_upos)
    freq_type_w = freq(type_w)
    freq_type_d = freq(type_d)
    freq_type_upos = freq(type_upos)
    freq_sent_d_w_n = freq(sent_d_w_n)

    chart_deprel = freq_deprel.plot(kind="bar")
    chart_upos = freq_upos.plot(kind="bar")
    chart_deprel_upos = freq_deprel_upos.plot(xticks=[],
        xlabel=f"Розподіл deprel+upos. Всього: {len(deprel_upos)}. Унікальних: {len(freq_deprel_upos)}")
    chart_type_w = freq_type_w.plot(xticks=[],
        xlabel=f"Розподіл типу w. Всього: {len(type_w)}. Унікальних: {len(freq_type_w)}")
    chart_type_d = freq_type_d.plot(xticks=[],
        xlabel=f"Розподіл типу d. Всього: {len(type_d)}. Унікальних: {len(freq_type_d)}")
    chart_type_upos = freq_type_upos.plot(xticks=[], kind="bar",
        xlabel=f"Розподіл Тип + Частина мови. Всього: {len(type_upos)}. Унікальних: {len(freq_type_upos)}")
    chart_sent_d_w_n = freq_sent_d_w_n.plot(xticks=[],
        xlabel=f"Розподіл сигнатур реченнь. Всього: {len(sent_d_w_n)}. Унікальних: {len(freq_sent_d_w_n)}")

    save_chart(chart_deprel, f"chart_{lang}_deprel.pdf")
    save_chart(chart_upos, f"chart_{lang}_upos.pdf")
    save_chart(chart_deprel_upos, f"chart_{lang}_deprel_upos.pdf")
    save_chart(chart_type_w, f"chart_{lang}_type_w.pdf")
    save_chart(chart_type_d, f"chart_{lang}_type_d.pdf")
    save_chart(chart_type_upos, f"chart_{lang}_type_upos.pdf")
    save_chart(chart_sent_d_w_n, f"chart_{lang}_sent_d_w_n.pdf")


def parse_cli_args():
    args = filter(lambda txt: re.search(r"--\w+=.+", txt), sys.argv[1:])
    keys = lambda txt: txt[2:txt.index('=')]
    vals = lambda txt: txt[txt.index('=') + 1:]
    return dict((keys(v), vals(v)) for v in args)


def print_tree(tree):
    print(tree.metadata.get("text"), "\n")
    for node in tree.to_list():
        print("{:25}{}".format(node.token.get("form"), node.signature))

    print("-" * 100, "\n")


def main():
    uk_trees = get_token_trees(UK_DEV_PATH, UK_TRAIN_PATH, UK_TEST_PATH)
    # es_trees = get_token_trees(ES_DEV_PATH, ES_TRAIN_PATH, ES_TEST_PATH)

    args = parse_cli_args()
    if args.get("text") and args.get("text").lower() == "true":
        for tree in uk_trees:
            print_tree(tree)
    else:
        process(uk_trees, "uk")


if __name__ == "__main__":
    main()
