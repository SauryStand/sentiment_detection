# -*- coding: utf-8 -*-

import jieba
import logging

def w2v_main():
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    #jieba customorised setting
    jieba.set_dictionary('../../data/dict/dict.text.big')
    jieba.load_userdict('../../data/dict/my_dict')
    #load stopwords
    stop_words = set()
    output = open('../../data/f_wikidata/wiki_seg.txt', 'w', encoding=True)
    with open('../../data/f__wikidata/wiki_zh_tw.txt', 'r', encoding=True) as content:
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


if __name__ == "__main__":
    w2v_main()