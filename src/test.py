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
    #    ├── композитором
    #    │  ├── ,
    #    │  ├── є
    #    │  ├── своєрідним
    #    │  └── того
    #    │     └── втілиться
    #    │        ├── ,
    #    │        ├── що
    #    │        └── твір
    #    │            ├── як
    #    │            └── мистецький
    #    └── .
    tree = map_token_tree(parse_tree(CONLLU_SENTENCE)[0])

    def test_D_signatures_should_be_serialized_correctly(self):
        tree = ModelTest.tree

        більше = str(tree.children[0].signature)
        побачене = str(tree.children[2].signature)
        того = str(tree.children[3].children[3].signature)

        self.assertEqual(більше, "d(advmod+ADV, advmod+ADV, 1, 1, d, 2hkl)")
        self.assertEqual(побачене, "d(obj+NOUN, conj+NOUN, 2, 1, d, 2hkl)")
        self.assertEqual(того, "d(nmod+PRON, acl:relcl+VERB, 3, 2, w, 2hkl)")

    def test_W_signatures_should_be_serialized_correctly(self):
        tree = ModelTest.tree

        відтворюю = str(tree.signature)
        композитором = str(tree.children[3].signature)
        втілиться = str(tree.children[3].children[3].children[0].signature)
        твір = str(tree.children[3].children[3].children[0].children[2].signature)

        self.assertEqual(відтворюю,
                         "w(root+VERB, advmod+ADV, nsubj+PRON, obj+NOUN, conj+NOUN, punct+PUNCT, 5, 0, 5, 2hkl)")
        self.assertEqual(композитором, "w(conj+NOUN, punct+PUNCT, cop+AUX, amod+ADJ, nmod+PRON, 4, 1, 4, 2hkl)")
        self.assertEqual(втілиться, "w(acl:relcl+VERB, punct+PUNCT, mark+SCONJ, xcomp:sp+NOUN, 2, 3, 3, 2hkl)")
        self.assertEqual(твір, "w(xcomp:sp+NOUN, mark+SCONJ, amod+ADJ, 1, 4, 2, 2hkl)")
