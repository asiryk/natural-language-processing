import unittest

from conllu import parse_tree

from src.model import map_token_tree
from src.resources import CONLLU_SENTENCE


# noinspection NonAsciiCharacters
class ModelTest(unittest.TestCase):
    # └── відтворюю
    #    ├── більше
    #    │  └── значно
    #    ├── я
    #    ├── побачене
    #    │  └── почуте
    #    │     └── й
    #    └── композитором
    #       ├── є
    #       ├── своєрідним
    #       └── того
    #          └── втілиться
    #             ├── що
    #             └── твір
    #                 ├── як
    #                 └── мистецький

    tree = map_token_tree(parse_tree(CONLLU_SENTENCE)[0])

    def test_signatures_should_be_serialized_correctly(self):
        tree = ModelTest.tree

        відтворюю = str(tree.signature)
        більше = str(tree.children[0].signature)
        # побачене = str(tree.children[2].signature)

        self.assertEqual(відтворюю, "w(root+VERB, advmod+ADV, nsubj+PRON, obj+NOUN, conj+NOUN, 5, 1, 4, 2hkl)")
        self.assertEqual(більше, "d(advmod+ADV, advmod+ADV, 1, 2, d, 2hkl)")
        # self.assertEqual(побачене, "d(obj+NOUN, conj+NOUN, cc, 2, 2, d, 2hkl)")
