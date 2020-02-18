# -*- coding:utf-8 -*-

'''
get sentences vectors by pre-train model
'''

from gensim import models
import jieba
import numpy as np


class word2sv():
    def __init__(self):
        jieba.set_dictionary('dict/dict.txt.big')
        jieba.load_userdict('dict/my_dict')
        jieba.initialize()
        self.model = models.Word2Vec.load('w2vmodel/word2vec.model')

    def getSenVec(self, sentence):
        '''
        get words' vectors
        words' vectors weights average, then return sentences' vector
        '''
        senCut = list(jieba.cut(sentence))
        lenOfCut = len(senCut)
        vecSum = np.zeros(200)
        for i in senCut:
            try:
                vec = self.model.wv.__getitem__(i)
                vecSum = np.add(vecSum, vec)
            except Exception as e:
                # print(e)
                lenOfCut -= 1
                continue
        if (lenOfCut == 0):
            return np.array([0] * 200)
        divisor = np.array([lenOfCut] * 200)
        return np.divide(vecSum, divisor)