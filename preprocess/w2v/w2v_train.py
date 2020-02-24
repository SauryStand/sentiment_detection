# -*- coding:utf-8 -*-

import logging
from gensim.models import word2vec

def w2v_make_model():
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    sentences = word2vec.LineSentence("../../data/f_wikidata/wiki_seg.txt")
    model = word2vec.Word2Vec(sentences, size=200)
    model.save("model/w2v/word2vec.model")

if __name__ == "__main__":
    w2v_make_model()