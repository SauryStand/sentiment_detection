# -*- coding:utf-8 -*-

'''
torch neural network model
'''
import torch
import torch.nn as nn
import torch.nn.functionalas as functionals

class JWP(nn.Module):
    def __init__(self, n_feature, n_hidden, n_hidden2, n_output):
        super(JWP, self).__init__()
        self.hidden = nn.Linear(n_feature, n_hidden)
        self.hidden2 = nn.Linear(n_hidden, n_hidden2)
        self.n_output = nn.Linear(n_hidden2, n_output)

    def forward(self, x, apply_sigmod = True):
        x = functionals.relu(self.hidden(x).squeeze())
        x = functionals.relu(self.hidden2(x).squeeze())
        if apply_sigmod:
            x =torch.sigmod(self.n_output(x))
        else:
            x = self.n_output(x)
        return x

