#coding:utf-8


from gensim.corpora import WikiCorpus
from utils.config import Config
from utils.langconv import *
from utils.zh_wiki import *
from opencc import OpenCC
'''
this dataset contains simple and tradictional chinese
'''

def get_text_from_wiki():
    config = Config()
    wiki_corpus = WikiCorpus(config.get_wiki_text_path, dictionary={})
    text_index = 0

    cc = OpenCC('t2s')  # convert from Simplified Chinese to Traditional Chinese
    # can also set conversion by calling set_conversion
    # cc.set_conversion('s2tw')

    with open(config.zh_wiki_text, 'w', encoding='utf-8') as output:
        for text in wiki_corpus.get_texts():
            #text = Converter('zh-hans').convert(text.decode('utf-8'))
            #print(text)
            #text = text.encode('utf-8')
            converted = []
            for t in text:
                converted.append(cc.convert(t))
            #print(converted)
            output.write(' '.join(converted) + '\n')
            text_index += 1
            if text_index % 1000 == 0:
                print('It had processed ' + str(text_index) + ' articles')

if __name__ == "__main__":
    get_text_from_wiki()
