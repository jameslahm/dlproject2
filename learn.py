import os, time, pickle, argparse, networks, utils
import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt
from torchvision import transforms
from edge_promoting import edge_promoting

tgt_transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize(mean=(0.5, 0.5, 0.5), std=(0.5, 0.5, 0.5))
])
train_loader_tgt = utils.data_load(os.path.join('data', 'tgt_data'), 'pair', tgt_transform, 4, shuffle=True, drop_last=True)

for (y, _) in train_loader_tgt:
    print(y.size())
    e = y[:, :, :, 256:]
    y = y[:, :, :, :256]