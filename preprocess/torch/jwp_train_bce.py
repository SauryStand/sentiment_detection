# -*- coding:utf-8 -*-

import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import pickle
from model.torch.jwp import JWP
from utils.config import torch_learning_rate
from utils.config import torch_min_learning_rate

with open('../../data/github/waimai_10k_tw.pkl', 'rb') as f:
    comment10k = pickle.load(f)

'''
training data 3k
'''
positive_comment_start = 0
negative_comment_start = 4000
positive_ans = torch.ones([3000,1], dtype=torch.float)
negative_ans = torch.ones([3000,1], dtype=torch.float)
positive_comments = []
negative_comments = []

#we choose 3k for training
for i in range(positive_comment_start, positive_comment_start + 3000):
    vec, ans = comment10k[str(i)]
    positive_comments.append(vec)
positive_comments = torch.FloatTensor(positive_comments)

for i in range(negative_comment_start, negative_comment_start + 3000):
    vec, ans = comment10k[str(i)]
    negative_comments.append(vec)
negative_comments = torch.FloatTensor(negative_comments)

train_data = torch.cat((positive_comments, negative_comments))
train_data_ans = torch.cat((positive_ans, negative_ans))

#testing data is 1k
test_positive_comment_start = 3000
test_negative_comment_start = 7000
test_positive_ans = torch.ones([1000,1], dtype=torch.float)
test_negative_ans = torch.ones([1000,1], dtype=torch.float)
test_positive_comments = []
test_negative_comments = []

for i in range(test_positive_comment_start, test_positive_comment_start + 1000):
    vec, ans = comment10k[str(i)]
    test_positive_comments.append(vec)
test_positive_comments = torch.FloatTensor(test_positive_comments)

for i in range(test_negative_comment_start, test_negative_comment_start + 1000):
    vec, ans = comment10k[str(i)]
    test_negative_comments.append(vec)
test_negative_comments = torch.FloatTensor(test_negative_comments)

test_data = torch.cat((test_positive_comments, test_negative_comments))
test_data_ans = torch.cat((test_positive_ans, test_negative_ans))

def adjust_lr(optimizer, epoch):
    # adjust learning rate
    lr = torch_learning_rate
    min_lr = torch_min_learning_rate
    if epoch % 30 == 0 and epoch != 0:
        lr = lr * 0.9
        if lr < min_lr:
            lr = min_lr
        for parameter in optimizer.param_groups:
            parameter['lr'] = lr


if __name__ == "__main__":
    net = JWP(200,150,100,1)
    print("net config: ", net)
    lr = torch_learning_rate
    optimizer = torch.optim.Adam(net.parameters(), lr=lr)
    loss_function = torch.nn.BCEWithLogitsLoss()
    for t in range(70): # why 70?
        # randomise data
        adjust_lr(optimizer, t)
        torch.manual_seed(t)
        train_data = train_data[torch.randperm(train_data.size()[0])]
        torch.manual_seed(t)
        train_data_ans = train_data_ans[torch.randperm(train_data_ans.size()[0])]

        # train phase
        net.train()
        optimizer.zero_grad()
        output = net(train_data)
        output_as_ans = output.clone().detach().numpy()
        output_as_ans = np.where([output_as_ans > 0.5], 1.0, 0.0)
        loss = loss_function(output, train_data_ans)
        loss.backward()
        optimizer.step()

        #eval phase
        net.eval()
        e_output = net(test_data)
        test_output_as_ans = e_output.clone().detach().numpy()
        test_output_as_ans = np.where([test_output_as_ans > 0.5], 1.0, 0.0)
        test_loss = loss_function(e_output, test_data_ans)

        print(
            "epoch:", t + 1,
            "train_loss:", round(loss.item(), 3),
            "train_acc:", round(np.mean(output_as_ans == train_data_ans.numpy()), 3),
            "test_loss:", round(test_loss.item(), 3),
            "test_acc:", round(np.mean(test_output_as_ans == test_data_ans.numpy()), 3),
            "LR:", lr
        )

        torch.save(net, 'model/torch/pytorch.bce.model')
        print("model save")

