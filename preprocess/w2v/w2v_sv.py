# -*- coding: UTF-8 -*-
from gensim import models
import jieba
import numpy as np
from utils.config import Config

class w2sv():

    def __init__(self):
        config = Config()
        #jieba.set_dictionary(config.zh_dict_txt_big)
        #jieba.load_userdict(config.zh_my_dict)
        jieba.initialize()
        self.model = models.Word2Vec.load(config.word2vec_model_zh)

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
    w2vs = w2sv()
    # fanti
    #print(w2vs.getSentenceVectors("今天天氣很好"))
    #获取词向量
    print(w2vs.getSentenceVectors("今天天气很好"))