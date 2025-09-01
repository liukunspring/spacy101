# spacy101
spacy的ner实践工作。
## todo搞一个个简单的ner
2025-0901
基于json的数据集搭建好了，要晚上一下数据集的代码，数据集比较小一共才55个，流程跑通了。
然后基于大模型去帮忙生成数据集

2025-07-29
label搭建起来了，假设可以生成不错的数据集。
然后我们应该可以训练一个ner了。
1. 完成基于json的训练数据集处理。

2025-4-11

2025-4-9
安装label-studio-ml
pip install git+https://github.com/HumanSignal/label-studio-ml-backend@master
label-studio-ml create my_ml_backend

label_studio_sdk

单纯的安装label-studio-ml有点问题。
---------------------------
按照一下label-studio
创建用户名字
label-studio start  --username dream@163.com --password test.com
2025-3-26：
准备建立数据集了，以后再把文件名给抽取出来。
如下所示
还有离散的状态给取出来： true false on off等。
W HwLockScreenReporter: report result = falsereport type:162 msg:{picture: Deepwater-05-2.3.001-bigpicture_05_8.jpg, channelId: 05}

```
还是选用fastapiserver服务，集成daoccano的自动标注服务了

pip install fastapi[standard]

```

2025-3-18
现在要把，ip地址，浮点数，数字这些内容都抽取出来。
1. 要解决实体冲突的问题。
2. 要建立一些数据集，确保新的规则可以有准确性。
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