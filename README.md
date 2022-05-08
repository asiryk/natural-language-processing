# universal_dependencies

## CoNLL-U Format

**CoNLL-X** is an annotation schema for describing linguistic features across diverse languages.  
[CoNLL-U](https://universaldependencies.org/format.html) is a further development of this annotation schema
for the Universal Dependencies formalism.

The annotation files contain three types of lines: **comment lines**, **word lines** and **blank lines**.

**Comment lines** precede word lines and start with a hash character `#`.
These lines can be used to provide metadata about the word lines that follow.

Each **word line** contains annotations for a single word or token. Larger linguistic units are represented
by subsequent word lines.

The annotations for a **word line**:

| **Field** | **Description**                                                                                    |
|-----------|----------------------------------------------------------------------------------------------------|
| ID        | Index of the word in sequence                                                                      |
| FORM      | The form of a word or punctuation symbol                                                           |
| LEMMA     | Lemma or the base form of a word                                                                   |
| UPOS      | [Universal part-of-speech tag](https://universaldependencies.org/u/pos/)                           |
| XPOS      | Language-specific part-of-speech tag                                                               |
| FEATS     | [Morphological features](https://universaldependencies.org/u/feat/index.html)                      |
| HEAD      | Syntactic head of the current word                                                                 |
| DEPREL    | Universal dependency relation to the `HEAD`                                                        |
| DEPS      | [Enhanced dependency relations](https://universaldependencies.org/u/overview/enhanced-syntax.html) |
| MISC      | Any additional annotations                                                                         |

Finally, a **blank line** after word lines is used to separate sentences.
