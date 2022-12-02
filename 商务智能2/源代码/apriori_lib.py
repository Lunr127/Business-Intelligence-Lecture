from efficient_apriori import apriori

# 设置数据集
data = [('尿布', '啤酒', '奶粉', '洋葱'), ('尿布', '啤酒', '奶粉', '洋葱'), ('尿布', '啤酒', '苹果', '洋葱'), ('尿布', '啤酒', '苹果'), ('尿布', '啤酒', '奶粉'),
        ('尿布', '啤酒', '奶粉'), ('尿布', '啤酒', '苹果'), ('尿布', '啤酒', '苹果'), ('尿布', '奶粉', '洋葱'), ('奶粉', '洋葱')]
# 挖掘频繁项集和规则
itemsets, rules = apriori(data, min_support=0.6, min_confidence=1)  # 最小支持度为0.6，最小置信度为1
print('-' * 50)
print('频繁项集:')
print(itemsets)
print('-' * 50)
print('规则:')
print(rules)
print('-' * 50)
