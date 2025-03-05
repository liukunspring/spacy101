import os
from . import config
from tokenizers import (
    decoders,
    models,
    normalizers,
    pre_tokenizers,
    processors,
    trainers,
    Tokenizer,
)

"""_summary_
获取所有的训练tokenizer的语料
"""
def get_token_files()->list:
    
    file_list=[]
    for file_name in os.listdir(config.TOKEN_DATA_PATH):
        if 'log' not in file_name:
            continue
        file_list.append(
            os.path.join(config.TOKEN_DATA_PATH,file_name)
        )
    return file_list
def tain_tokenizer():
    tokenizer = Tokenizer(models.WordPiece(unk_token="[UNK]"))
    tokenizer.normalizer = normalizers.BertNormalizer(lowercase=True)
    tokenizer.pre_tokenizer = pre_tokenizers.BertPreTokenizer()
    tokenizer.pre_tokenizer.pre_tokenize_str("Let's test my pre-tokenizer.")
    special_tokens = ["[UNK]", "[PAD]", "[CLS]", "[SEP]", "[MASK]"]
    trainer = trainers.WordPieceTrainer(vocab_size=6000, special_tokens=special_tokens)
    tokenizer.model = models.WordPiece(unk_token="[UNK]")
    tokenizer.train(get_token_files() , trainer=trainer)
    tokenizer.save('applog-tokenizer.json')
def load_tokenizer():
    tokenizer = Tokenizer(models.WordPiece(unk_token="[UNK]"))
    tokenizer.normalizer = normalizers.BertNormalizer(lowercase=True)
    tokenizer.pre_tokenizer = pre_tokenizers.BertPreTokenizer()
    tokenizer=Tokenizer.from_file('applog-tokenizer.json')
    encode_result=tokenizer.encode('12-19 12:01:42.234 21614 21614 D HwCust  : Create obj success use class com.huawei.mms.util.HwCustUpdateUserBehaviorImpl')
    print(encode_result.tokens)
    

if __name__=='__main__':
    #tain_tokenizer()
    load_tokenizer()


