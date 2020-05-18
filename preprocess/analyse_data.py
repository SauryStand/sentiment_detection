# -*- coding:utf-8 -*-

import pandas as pd

train = pd.read_csv('../data/kaggle/train.tsv', sep="\t")

print(train.head(5))