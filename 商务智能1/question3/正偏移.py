import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = list(np.random.gamma(2, 3, 1000))
s = pd.Series(data)
plt.hist(data, 100, density=True, facecolor='g', alpha=0.9)
plt.show()

print("----------------------------------------")
print("此正偏移分布的 Skewness 的值为：", round(s.skew(), 10))
print("此正偏移分布的 Kurtosis 的值为：", round(s.kurt(), 10))
print("----------------------------------------")
