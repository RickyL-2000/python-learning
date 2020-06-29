import random
import numpy as np

tc = set((
    (i // 10, i % 10, j // 10, j % 10),     # time code
    i + j / 60 if i > 0 else 24 + j / 60)   # 标注
    for i in range(24) for j in range(60))
# 划分训练集与验证集
tc_train = random.sample(tc, int(len(tc) * 0.8))    # 80%的时间码为训练集
tc_val = tc - set(tc_train)     # 20%的时间码为测试集
# 数据增强
train_count = 50000
X_train, Y_train = [], []
for i in range(train_count):
    t = random.choice(tc_train)
    X_train.append(t[0])
    Y_train.append(t[1])
X_train = np.array(X_train)
Y_train += np.random.normal(0, 1e-2, (train_count,))    # 添加噪声
X_val = np.array([list(t[0]) for t in tc_val])
Y_val = np.array([t[1] for t in tc_val])
