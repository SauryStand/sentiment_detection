# -*- coding:utf-8 -*-


from preprocess.word2vec_sentence_vec import word2sv
import pickle
import csv

if __name__ == "__main__":
    w2vs = word2sv()
    sentencesDict = {}
    with open('dataset/waimai_10k_tw.csv', newline='', encoding='UTF-8') as f:
        rows = csv.reader(f)
        for i, row in enumerate(rows):
            if (row[0] == 'label'):
                continue
            line = row[1].strip('\n')
            sVec = w2vs.getSenVec(line)
            # sentencesDict.append(sVec)
            sentencesDict[str(i - 1)] = (sVec, row[0])
    with open('dataset/waimai_10k_tw.pkl', 'wb') as f:
        pickle.dump(sentencesDict, f)
    print("finish packing waimai_10k_tw.pkl")
