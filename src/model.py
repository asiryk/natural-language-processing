from enum import Enum
from typing import List, Optional, Tuple

from conllu import TokenTree
from conllu.models import Token, Metadata


class SigType(Enum):
    D = "d"  # one ancestor
    W = "w"  # multiple ancestors
    N = "n"  # no ancestors


class Signature:
    type: SigType
    child_type: Optional[SigType]
    depth: int  # depth counting from the root element
    height: int  # length of the longest downward path to a leaf from that node
    node: Tuple[str, str]  # DEPREL, UPOS
    children_nodes: List[Tuple[str, str]]
    sentence_id: Optional[str]

    def __init__(self, current: 'ParseTree', children: List['ParseTree'], depth: int, height: int, sentence_id: str):
        self.node = (current.get_token("deprel"), current.get_token("upos"))
        self.children_nodes = [child.signature.node for child in children]
        self.depth = depth
        self.height = height
        self.sentence_id = sentence_id
        if len(children) == 0:
            self.type = SigType.N
        elif len(children) == 1:
            self.type = SigType.D
        else:
            self.type = SigType.W

    def __str__(self):
        def str_node(n: Tuple[str, str]):
            return f"{n[0]}+{n[1]}"

        node = str_node(self.node)
        children_nodes = ", ".join(str_node(child) for child in self.children_nodes)
        return f"{self.type.value}({node}, {children_nodes}, {self.depth}, {self.height}, {self.sentence_id})"


class ParseTree:
    token: Token
    metadata: Metadata
    children: List['ParseTree']
    signature: Signature

    def __init__(self, token_node: TokenTree, children: List['ParseTree'], depth: int, height: int,
                 metadata: Metadata):
        self.token = token_node.token
        self.metadata = metadata
        self.children = children
        self.signature = Signature(self, self.children, depth, height, metadata.get("sent_id"))

    def get_token(self, key: str):
        return self.token.get(key)


def _traverse(root: TokenTree, depth: int = 0, metadata: Optional[Metadata] = None) -> Tuple[ParseTree, int]:
    metadata = root.metadata if metadata is None else metadata
    children = []
    height = 0

    for node in root.children:
        data_node, node_subtree_depth = _traverse(node, depth + 1, metadata)
        height = max(height, node_subtree_depth + 1)
        children.append(data_node)

    data_root = ParseTree(root, children, depth, height, metadata)

    return data_root, height


def traverse(root: TokenTree) -> ParseTree:
    return _traverse(root)[0]
