import jieba
from preprocess.w2v.w2v_sv import w2v_sv_class

jieba.set_dictionary('../../data/dict/dict.txt.big')
jieba.load_userdict('../../data/dict/my_dict')

jieba.initialize()
w2v_sv = w2v_sv_class()

while True:
    s = input("testing input:")
    list = list(jieba.cut(s))
    print(list)
    print(w2v_sv.getSentenceVectors(s))