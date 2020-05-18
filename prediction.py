# -*- coding:utf-8 -*-

import torch
import numpy as np
from preprocess.w2v.w2v_sv import w2sv
from utils.config import Config
from gensim import models
import jieba
import numpy as np

config = Config()



if __name__ == "__main__":
    print("Initialising model...")
    w2vs = w2sv()
    net = torch.load(config.torch_bce_model_zh)
    net.eval()
    # test_data
    while True:
        ts = input("Input:")
        v1 = w2vs.getSentenceVectors(ts)
        res = net(torch.FloatTensor(v1), apply_sigmoid = True)
        out = res
        res = res.clone().detach().numpy()[0]
        print(round(res,3))

        if res > 0.6:
            print("Positive sentence.")
        elif res > 0.45 and res <= 0.6:
            print("Neutral sentence.")
        else:
            print("Negative sentence.")