import spacy
from spacy.tokens import Doc
# class WhitespaceTokenizer:
#     def __init__(self, vocab):
#         self.vocab = vocab

#     def __call__(self, text):
#         words = text.split(" ")
#         spaces = [True] * len(words)
#         # Avoid zero-length tokens
#         for i, word in enumerate(words):
#             if word == "":
#                 words[i] = " "
#                 spaces[i] = False
#         # Remove the final trailing space
#         if words[-1] == " ":
#             words = words[0:-1]
#             spaces = spaces[0:-1]
#         else:
#            spaces[-1] = False

#         return Doc(self.vocab, words=words, spaces=spaces)

# # nlp = spacy.blank("en")
# nlp.tokenizer = WhitespaceTokenizer(nlp.vocab)
# doc = nlp("What's happened to me? he thought.  It wasn't a dream. ")
# print([token.text for token in doc])

from tokenizers import BertWordPieceTokenizer

import spacy
import os 
from __init__ import PROJECT_ROOT
from tokenizers import (
    decoders,
    models,
    normalizers,
    pre_tokenizers,
    processors,
    trainers,
    Tokenizer,
)
class BertTokenizer:
    def __init__(self, vocab, vocab_file, lowercase=True):
        self.vocab = vocab
        self._tokenizer = Tokenizer.from_file(vocab_file)

    def __call__(self, text):
        tokens = self._tokenizer.encode(text)
        words = []
        spaces = []
        for i, (text, (start, end)) in enumerate(zip(tokens.tokens, tokens.offsets)):
            if text.startswith("##"):
                text=text[2:]
            words.append(text)
            if i < len(tokens.tokens) - 1:
                # If next start != current end we assume a space in between
                next_start, next_end = tokens.offsets[i + 1]
                spaces.append(next_start > end)
            else:
                spaces.append(True)
        return Doc(self.vocab, words=words, spaces=spaces)



from spacy.language import Language
from spacy.tokens import Span
import re 
nlp = spacy.blank("en")
ner=nlp.add_pipe('ner')
ner.add_label("TID")
ner.add_label("ORG")
ner.add_label("LOCATION")
nlp.initialize()
@Language.component("thread_tid_entities")
def expand_person_entities(doc:Doc):
    tid_thread_regex=r'watchthread\{(\d+)\}'
    match = re.search(tid_thread_regex, doc.text)
    print('text',doc.text)
    print('match',match)
    new_ents=[]
    if match:
        start,end=match.span(1)
        span = doc.char_span(start, end,label='TID')
        print(span)
        new_ents.append(span)
        thread_id = match.group(1)
    doc.ents = new_ents
    print(new_ents)
    return doc


nlp.tokenizer = BertTokenizer(nlp.vocab,os.path.join(PROJECT_ROOT, "applog-tokenizer.json"))
nlp.add_pipe("thread_tid_entities", before="ner")

doc = nlp("12-17 19:31:36.314 31949 31967 I eSpaceService: WatchThread{4786} TcpCirChannel.shutdown(TcpCirChannel.java:257) Login_By_Step-> shut down now connect")
print(doc.text, [token.text for token in doc])
print([(ent.text, ent.label_) for ent in doc.ents])

