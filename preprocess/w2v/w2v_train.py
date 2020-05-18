# -*- coding:utf-8 -*-

import logging
from gensim.models import word2vec
from utils.config import Config

def w2v_make_model():
    config = Config()
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    sentences = word2vec.LineSentence(config.zh_seg_txt)
    model = word2vec.Word2Vec(sentences, size=200)
    model.save(config.word2vec_model_zh)

if __name__ == "__main__":
    w2v_make_model()