# -*- coding: UTF-8 -*-
from gensim import models
import jieba
import numpy as np

class W2VS():
    def __init__(self):
        jieba.set_dictionary('../../data/dict/dict.txt.big')
        jieba.load_userdict('../../data/dict/my_dict')
        jieba.initialize()
        self.model = models.Word2Vec.load('../../model/w2v/word2vec.model')

    def getSentenceVectors(self, sentence):
        senCut = list(jieba.cut(sentence))
        lenOfCut = len(senCut)
        vecSum = np.zeros(200)
        for i in senCut:
            try:
                vec = self.model.wv.__getitem__(i)
                vecSum = np.add(vecSum, vec)
            except Exception as e:
                lenOfCut -= 1
                continue
        if lenOfCut == 0:
            return np.array([0] * 200)
        divisor = np.array([lenOfCut] * 200)
        return np.divide(vecSum, divisor)


if __name__ == "__main__":
    w2vs = W2VS()
    # fanti
    print(w2vs.getSentenceVectors("今天天氣很好"))