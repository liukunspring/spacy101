import spacy
nlp = spacy.blank("en")


import spacy
from spacy.tokens import Doc

class WhitespaceTokenizer:
    def __init__(self, vocab):
        self.vocab = vocab

    def __call__(self, text):
        words = text.split(" ")
        spaces = [True] * len(words)
        # Avoid zero-length tokens
        for i, word in enumerate(words):
            if word == "":
                words[i] = " "
                spaces[i] = False
        # Remove the final trailing space
        if words[-1] == " ":
            words = words[0:-1]
            spaces = spaces[0:-1]
        else:
           spaces[-1] = False

        return Doc(self.vocab, words=words, spaces=spaces)

nlp = spacy.blank("en")
nlp.tokenizer = WhitespaceTokenizer(nlp.vocab)
doc = nlp("What's happened to me? he thought.  It wasn't a dream. ")
print([token.text for token in doc])

from tokenizers import BertWordPieceTokenizer
from spacy.tokens import Doc
import spacy
import os 
from __init__ import BERT_PATH


class BertTokenizer:
    def __init__(self, vocab, vocab_file, lowercase=True):
        self.vocab = vocab
        self._tokenizer = BertWordPieceTokenizer(vocab_file, lowercase=lowercase)

    def __call__(self, text):
        tokens = self._tokenizer.encode(text)
        words = []
        spaces = []
        for i, (text, (start, end)) in enumerate(zip(tokens.tokens, tokens.offsets)):
            words.append(text)
            if i < len(tokens.tokens) - 1:
                # If next start != current end we assume a space in between
                next_start, next_end = tokens.offsets[i + 1]
                spaces.append(next_start > end)
            else:
                spaces.append(True)
        return Doc(self.vocab, words=words, spaces=spaces)

nlp = spacy.blank("en")
nlp.tokenizer = BertTokenizer(nlp.vocab,os.path.join(BERT_PATH, "vocab.txt"))
doc = nlp("Justin Drew Bieber is a Canadian singer, songwriter, and actor.")
print(doc.text, [token.text for token in doc])