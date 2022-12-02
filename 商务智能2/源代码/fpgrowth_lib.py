import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import fpgrowth
from mlxtend.frequent_patterns import association_rules  # 生成强关联规则


def create_data():
    dataset = [('尿布', '啤酒', '奶粉', '洋葱'), ('尿布', '啤酒', '奶粉', '洋葱'), ('尿布', '啤酒', '苹果', '洋葱'), ('尿布', '啤酒', '苹果'),
               ('尿布', '啤酒', '奶粉'), ('尿布', '啤酒', '奶粉'), ('尿布', '啤酒', '苹果'), ('尿布', '啤酒', '苹果'), ('尿布', '奶粉', '洋葱'), ('奶粉', '洋葱')]
    return dataset


def main():
    dataset = create_data()
    te = TransactionEncoder()
    # 进行 one-hot 编码
    te_ary = te.fit(dataset).transform(dataset)
    df = pd.DataFrame(te_ary, columns=te.columns_)
    frequent_itemsets = fpgrowth(df, min_support=0.8, use_colnames=True)  # 最小支持度为0.8
    print('频繁项集：')
    print(frequent_itemsets)  # 频繁项集

    # 评估指标的最小阈值为min_threshold=1
    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=1)  # 关联规则
    print('关联规则：')
    print(rules)


if __name__ == '__main__':
    main()
