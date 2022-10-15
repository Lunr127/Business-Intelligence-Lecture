import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = list(np.random.randn(10000))

plt.hist(data, 100, density=True, facecolor='r', alpha=0.9)
plt.show()

s = pd.Series(data)

print("----------------------------------------")
print("此正态分布的 Skewness 的值为：", round(s.skew(), 10))
print("此正态分布的 Kurtosis 的值为：", round(s.kurt(), 10))
print("----------------------------------------")
