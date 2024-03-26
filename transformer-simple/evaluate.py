import torch
import numpy as np
import time

from parser import args
from torch.autograd import Variable
from utils import subsequent_mask


def log(data, timestamp):
    file = open(f'log/log-{timestamp}.txt', 'a')
    file.write(data)
    file.write('\n')
    file.close()


def greedy_decode(model, src, src_mask, max_len, start_symbol):
    # 这个函数使用了贪心策略来生成输出序列，即在每个时间选择概率最大的输出符号

    # 调用编码器，将源序列和源序列掩码编码成一个向量序列，作为decoder的输入
    memory = model.encode(src, src_mask)
    # 初始化输出序列ys为一个包含单个元素的一维张量
    ys = torch.ones(1, 1).fill_(start_symbol).type_as(src.data)
    for i in range(max_len-1):
        out = model.decode(memory, src_mask, 
                           Variable(ys), 
                           Variable(subsequent_mask(ys.size(1))
                                    .type_as(src.data)))
        prob = model.generator(out[:, -1])
        _, next_word = torch.max(prob, dim = 1)  # 获得下一个输出符号。
        next_word = next_word.data[0]
        ys = torch.cat([ys, 
                        torch.ones(1, 1).type_as(src.data).fill_(next_word)], dim=1)  # 将输出符号添加到输出序列的末尾
    return ys


def evaluate(data, model):
    timestamp = time.time()
    with torch.no_grad():
        for i in range(len(data.dev_en)):
            en_sent = " ".join([data.en_index_dict[w] for w in data.dev_en[i]])
            print("\n" + en_sent)
            log(en_sent, timestamp)
            cn_sent = " ".join([data.cn_index_dict[w] for w in data.dev_cn[i]])
            print("".join(cn_sent))
            log(cn_sent, timestamp)

            src = torch.from_numpy(np.array(data.dev_en[i])).long().to(args.device)
            src = src.unsqueeze(0)
            src_mask = (src != 0).unsqueeze(-2)

            out = greedy_decode(model, src, src_mask, max_len = args.max_length, start_symbol = data.cn_word_dict["BOS"])

            translation = []
            for j in range(1, out.size(1)):
                sym = data.cn_index_dict[out[0, j].item()]
                if sym != 'EOS':
                    translation.append(sym)
                else:
                    break
            print("translation: %s" % " ".join(translation))
            log("translation: " + " ".join(translation) + "\n", timestamp)

            

