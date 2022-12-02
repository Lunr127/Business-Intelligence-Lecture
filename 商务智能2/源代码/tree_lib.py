from sklearn.datasets import load_wine  # 红酒数据集
from sklearn import tree  # 决策树
from sklearn.model_selection import train_test_split  # 划分训练集和测试集

wine = load_wine()  # 实例化数据集
print('-' * 50)
print("shape")
print(wine.data.shape)  # 特征矩阵

Xtrain, Xtest, Ytrain, Ytest = train_test_split(wine.data, wine.target, test_size=0.3)  # 将数据集的30%划分为测试集，其他的划分为训练集
clf = tree.DecisionTreeClassifier(criterion="entropy")  # 实例化树模型
clf = clf.fit(Xtrain, Ytrain)  # 训练树模型
score = clf.score(Xtest, Ytest)  # 准确度得分
print('-' * 50)
print("score")
print(score)
print('-' * 50)
print("feature importances")
print(clf.feature_importances_)  # 特征重要性
print('-' * 50)
