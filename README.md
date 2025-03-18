# spacy101
spacy的ner实践工作。
## todo搞一个个简单的ner
2025-3-18
现在要把，ip地址，浮点数，数字这些内容都抽取出来。
要解决实体冲突的问题。
2025-3-13
现在要把关键代码拆分成两部分
tokenizer的训练部分。
ner相关的正则式提取部分。
下一步的工作要想着和drain部分结合了
2025-2-28:
做一下复盘：
1. 为什么要用bert的分词方法作为spacy的tokenizer
spacy的span机制的最小单位是token，spacy模型的原始token是不能解决xxxx.java:129单独提取129行号的问题。
所以重新训练了一个一个tokenizer。
2. 使用新的tokenizer中是否遇到了什么问题。
首先忘记tokenizer不区分大小写，导致写的正则式失效。
tokenizer分词后，word的字词，带有## 也会导致正则式失效： word 变成  wo##rd这样，正则式失效，创建的span_char也会出现问题，
需要再额外出去##。
后续还要做一些单词的index对齐工作。
3. 当前处于什么阶段，当前还是处于准备预训练数据的阶段。
2025-2-26 00:27:01 使用bert的bpe和loghub的安卓日志，训练一个分词器。