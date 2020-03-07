# -*- coding: utf-8 -*-

import jieba
import logging
from utils.config import Config
import json

def w2v_main():
    config = Config()
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    #jieba customorised setting
    jieba.set_dictionary(config.dict_big_txt)
    jieba.load_userdict(config.dict_my_dict)
    #load stopwords
    stop_words = set()
    output = open(config.tw_seg_txt, 'a', encoding='utf-8')
    with open(config.tw_wiki_txt, 'r', encoding='utf-8') as content:
        for text_num, line in enumerate(content):
            line =line.strip('\n')
            words =jieba.cut(line, cut_all=False)
            for word in words:
                if word not in stop_words:
                    output.write(word.join(" "))
            output.write('\n')
            if(text_num + 1) % 100000 == 0:
                logging.info("finished %d rows for stop_words" % (text_num + 1))
    output.close()

def w2v_main_zh():
    config = Config()
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


def json2txt():
    with open("D:\source_codes\python\Sentiment\sentiment_detection\data\\f_wikidata\wiki_zh\AA\wiki_00", encoding='utf-8') as json_file:
        jsonobj = json.load(json_file)
        print(jsonobj)


if __name__ == "__main__":
    #w2v_main()
    json2txt()