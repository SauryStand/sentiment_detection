# -*- coding:utf-8 -*-

import torch
import numpy as np
from preprocess.w2v import w2v_sv

print("init...")
w2vs = w2v_sv()
net = torch.load('preprocess/torch/pytorch_bce.model')
net.eval()
# test_data
while True:
    ts = input("Input:")
    v1 = w2vs.getSenVec(ts)
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