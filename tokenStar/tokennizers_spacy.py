import spacy
from spacy.tokens import Doc
import os 
from __init__ import PROJECT_ROOT
from spacy.language import Language
import re 
from tokenizers import (
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

@Language.component("thread_tid_entities")
def expand_person_entities(doc:Doc):
    tid_thread_regex=r'\{(\d+)\}'
    match = re.search(tid_thread_regex, doc.text)
    #print('text',doc.text)
    #print('match',match)
    new_ents=list(doc.ents)
    if match:
        start,end=match.span(1)
        span = doc.char_span(start, end,label='TID')
        print(span)
        new_ents.append(span)
        thread_id = match.group(1)
    doc.ents = new_ents
    print(new_ents)
    return doc

@Language.component("ip_address_entity")
def expand_ip_address_entity(doc:Doc):
    tid_thread_regex=r'(\d+\.\d+\.\d+\.\d+)'
    match = re.search(tid_thread_regex, doc.text)
    print('text',doc.text)
    #print('match',match)
    new_ents=list(doc.ents)
    if match:
        start,end=match.span(1)
        span = doc.char_span(start, end,label='IP_ADDRESS')
        print(span)
        new_ents.append(span)
        thread_id = match.group(1)
    doc.ents = new_ents
    print(new_ents)
    return doc

@Language.component("float_number_entity")
def expand_float_number__entity(doc:Doc):
    # 正则式提取number;
    float_number_regex=r'[: ](\d\.\d+)'
    match = re.search(float_number_regex, doc.text)    
    print('text',doc.text)
    #print('match',match)
    new_ents=list(doc.ents)
    for match in re.finditer(float_number_regex, doc.text): 
        if match:
            print(match)
            start,end=match.span(1)
            span = doc.char_span(start, end,label='FLOAT_NUMER')
            #print(span)
            new_ents.append(span)
    doc.ents = new_ents
    print(new_ents)
    return doc
