import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = list()

for i in range(1, 10):
    if (i < 8):
        for j in range(1, i * 1000):
            d = np.random.uniform(10) + i
            data.append(d)
    else:
        for j in range(1, i * 200):
            d = np.random.uniform(10) - 2
            data.append(d)

plt.hist(data, 100, density=True, facecolor='b', alpha=1.0)
plt.show()

s = pd.Series(data)
print("----------------------------------------")
print("此负偏移分布的 Skewness 的值为：", round(s.skew(), 10))
print("此负偏移分布的 Kurtosis 的值为：", round(s.kurt(), 10))
print("----------------------------------------")
