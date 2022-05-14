from typing import List, Optional, Tuple

from conllu import TokenTree
from conllu.models import Token, Metadata


class ParseTree:
    token: Token
    metadata: Optional[Metadata]
    children: List['ParseTree']

    parent: Optional['ParseTree']
    depth: int  # depth counting from the root element
    height: int  # length of the longest downward path to a leaf from that node

    def __init__(self, token_node: TokenTree, children: List['ParseTree'], depth: int, height: int):
        self.token = token_node.token
        self.metadata = token_node.metadata
        self.children = children

        self.depth = depth
        self.height = height
        self.parent = None

    def set_parent(self, parent: 'ParseTree'):
        self.parent = parent

    def get_token(self, key: str):
        return self.token.get(key)


def traverse(root: TokenTree, depth: int = 0) -> Tuple[ParseTree, int]:
    children = []
    height = 0

    for node in root.children:
        data_node, node_subtree_depth = traverse(node, depth + 1)
        height = max(height, node_subtree_depth + 1)
        children.append(data_node)

    data_root = ParseTree(root, children, depth, height)
    for node in children:
        node.set_parent(data_root)

    return data_root, height
