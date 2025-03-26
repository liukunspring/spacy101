import spacy
from spacy.language import Language
from spacy.tokens import Doc
import json
import os 
from tokenStar import tokennizers_spacy
from config import PROJECT_ROOT
def build_nlp_instance()->Language:
    nlp = spacy.blank("en")
    ner=nlp.add_pipe('ner')
    ner.add_label("TID")
    ner.add_label("ORG")
    ner.add_label("IP_ADDRESS")
    ner.add_label("LOCATION")
    ner.add_label("FLOAT_NUMER")
    ner.add_label("COMMON_NUMER")
    nlp.initialize()
    nlp.tokenizer = tokennizers_spacy.BertTokenizer(nlp.vocab,os.path.join(PROJECT_ROOT, "applog-tokenizer.json"))
    nlp.add_pipe("thread_tid_entities", before="ner")
    nlp.add_pipe("ip_address_entity",before="thread_tid_entities")
    nlp.add_pipe("float_number_entity",before="ip_address_entity")
    nlp.add_pipe("common_number_entity",before="ip_address_entity")
    return nlp

class Ner:
    def __init__(self):
        pass
def dump_ner(text,nlp:Language):
    doc=nlp(text)
    ner_ret={
        'text':text,
        'entites':[]
    }
    for ent in doc.ents:
        ent.label_
        ner_ret['entites'].append(
            {
                'entity_type':ent.label_,
                'start_char':ent.start_char,
                'end_char':ent.end_char,
                'value':ent.text
            }
        )
    return ner_ret
if __name__=='__main__':
    nlp=build_nlp_instance()
    text="I eSpaceService: WatchThread {4786} TcpCirChannel.shutdown(TcpCirChannel.java:257) Login_By_Step-> shut down now connec"
    ret=dump_ner(text,nlp)
    print(json.dumps(ret,indent=4,ensure_ascii=False))