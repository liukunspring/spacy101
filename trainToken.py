import os
import config
from tokenizers import (
    decoders,
    models,
    normalizers,
    pre_tokenizers,
    processors,
    trainers,
    Tokenizer,
)

tokenizer = Tokenizer(models.WordPiece(unk_token="[UNK]"))
tokenizer.normalizer = normalizers.BertNormalizer(lowercase=True)
tokenizer.pre_tokenizer = pre_tokenizers.BertPreTokenizer()
tokenizer.pre_tokenizer.pre_tokenize_str("Let's test my pre-tokenizer.")
special_tokens = ["[UNK]", "[PAD]", "[CLS]", "[SEP]", "[MASK]"]
trainer = trainers.WordPieceTrainer(vocab_size=5000, special_tokens=special_tokens)
tokenizer.model = models.WordPiece(unk_token="[UNK]")
tokenizer.train([os.path.join(config.TOKEN_DATA_PATH,'applogcat-1.log'),
                os.path.join(config.TOKEN_DATA_PATH,'applogcat-2.log'),
                os.path.join(config.TOKEN_DATA_PATH,'applogcat-3.log'),
                os.path.join(config.TOKEN_DATA_PATH,'applogcat-4.log'),
                os.path.join(config.TOKEN_DATA_PATH,'applogcat-5.log')
                ], trainer=trainer)
tokenizer.save('applog-tokenizer.json')

