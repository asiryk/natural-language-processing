import io
import os
from typing import List

import numpy as np
import pandas as pd
from conllu import parse_tree_incr

from src.model import map_token_tree, SigType, Signature

UK_TOKENS_PATH = "./ud_ukrainian/uk_iu-ud-dev.conllu"
DIST_IMAGES_PATH = "./article/images/"


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
    return pd.DataFrame(values, index=names).sort_values(by=0, ascending=False)


def sig_sentence(sentence: List[Signature]):
    types = {}
    for sig in sentence:
        amount = types.get(sig.type, 0)
        types[sig.type] = amount + 1

    return f"w{types.get(SigType.W, 0)},d{types.get(SigType.D, 0)},n{types.get(SigType.N)}"


def main():
    data_file = io.open(UK_TOKENS_PATH, "r", encoding="utf-8")
    token_trees = map(map_token_tree, list(parse_tree_incr(data_file)))
    sentences = [[tree.signature for tree in sentence_tree.to_list()] for sentence_tree in token_trees]
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

    chart_deprel = freq_deprel.plot(legend=False, kind="bar")
    chart_upos = freq_upos.plot(legend=False, kind="bar")
    chart_deprel_upos = freq_deprel_upos.plot(legend=False, xticks=[],
        xlabel=f"Розподіл deprel+upos. Всього: {len(deprel_upos)}. Унікальних: {len(freq_deprel_upos)}")
    chart_type_w = freq_type_w.plot(legend=False, xticks=[],
        xlabel=f"Розподіл типу w. Всього: {len(type_w)}. Унікальних: {len(freq_type_w)}")
    chart_type_d = freq_type_d.plot(legend=False, xticks=[],
        xlabel=f"Розподіл типу d. Всього: {len(type_d)}. Унікальних: {len(freq_type_d)}")
    chart_type_upos = freq_type_upos.plot(legend=False, xticks=[],
        xlabel=f"Розподіл Тип + Частина мови. Всього: {len(type_upos)}. Унікальних: {len(freq_type_upos)}")
    chart_sent_d_w_n = freq_sent_d_w_n.plot(legend=False, xticks=[],
        xlabel=f"Розподіл сигнатур реченнь. Всього: {len(sent_d_w_n)}. Унікальних: {len(freq_sent_d_w_n)}")

    save_chart(chart_deprel, "chart_deprel.pdf")
    save_chart(chart_upos, "chart_upos.pdf")
    save_chart(chart_deprel_upos, "chart_deprel_upos.pdf")
    save_chart(chart_type_w, "chart_type_w.pdf")
    save_chart(chart_type_d, "chart_type_d.pdf")
    save_chart(chart_type_upos, "chart_type_upos.pdf")
    save_chart(chart_sent_d_w_n, "chart_sent_d_w_n.pdf")


if __name__ == "__main__":
    main()
