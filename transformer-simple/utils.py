import copy
import torch.nn as nn
import numpy as np
import torch


def clones(module, N):
    return nn.ModuleList([copy.deepcopy(module) for _ in range(N)])


# 处理测试数据
def seq_padding(X, padding=0):
    L = [len(x) for x in X]
    ML = max(L)
    return np.array([
        np.concatenate([x, [padding] * (ML - len(x))]) if len(x) < ML else x for x in X
    ])

def subsequent_mask(size):
    "Mask out subsequent positions."
    attn_shape = (1, size, size)
    # np.triu函数生成一个对角线位置上移一位的上三角矩阵（k=1代表按对角线方向上移），矩阵大小为attn_shape
    subsequent_mask = np.triu(np.ones(attn_shape), k=1).astype('uint8')
    # 返回布尔矩阵，subsequent_mask上三角矩阵中0的位置对应True
    return torch.from_numpy(subsequent_mask) == 0