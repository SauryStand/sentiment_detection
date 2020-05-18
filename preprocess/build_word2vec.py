# -*- coding:utf-8 -*-


from preprocess.w2v.w2v_sv import w2sv
import pickle
import csv
from utils.config import Config

if __name__ == "__main__":
    config = Config()
    w2vs = w2sv()
    sentencesDict = {}
    with open(config.waimai_cn_path, newline='', encoding='UTF-8') as f:
        rows = csv.reader(f)
        for i, row in enumerate(rows):
            if (row[0] == 'label'):
                continue
            line = row[1].strip('\n')
            sVec = w2vs.getSenVec(line)
            # sentencesDict.append(sVec)
            sentencesDict[str(i - 1)] = (sVec, row[0])
    with open(config.waimai_cn_pkl_path, 'wb') as f:
        pickle.dump(sentencesDict, f)
    print("finish packing waimai_10k_zh.pkl")
