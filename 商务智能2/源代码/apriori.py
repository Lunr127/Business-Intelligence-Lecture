def create_C1():
    C1 = set()
    for transaction in dataSet:
        for item in transaction:
            C1.add(frozenset([item]))
    return C1


def create_Ck(Lk, k):
    Ck = set()
    len_Lk = len(Lk)
    list_Lk = list(Lk)
    for i in range(len_Lk):
        for j in range(1, len_Lk):
            L1 = list(list_Lk[i])
            L2 = list(list_Lk[j])
            L1.sort()
            L2.sort()
            if L1[0:k - 2] == L2[0:k - 2]:
                Ck_item = list_Lk[i] | list_Lk[j]
                if is_apriori(Ck_item, Lk):
                    Ck.add(Ck_item)
    return Ck


def is_apriori(Ck_item, Lk):
    for item in Ck_item:
        sub_Ck = Ck_item - frozenset([item])
        if sub_Ck not in Lk:
            return False
    return True


def generate_Lk_by_Ck(Ck, minSupport=0.5):
    Lk = set()
    item_count = {}

    for t in dataSet:
        for item in Ck:
            if item.issubset(t):
                if item not in item_count:
                    item_count[item] = 1
                else:
                    item_count[item] += 1
    for item in item_count:
        support = item_count[item] / float(len(dataSet))
        if support >= minSupport:
            Lk.add(item)
            supportData[item] = support

    return Lk


def generate_L(minSupport):
    C1 = create_C1()
    L1 = generate_Lk_by_Ck(C1, minSupport)

    L = []
    Lksub1 = L1.copy()
    L.append(Lksub1)
    for lk in Lksub1:
        freq_itemsets.append((lk, supportData[lk]))
    i = 2

    while True:
        Ci = create_Ck(Lksub1, i)
        Li = generate_Lk_by_Ck(Ci, minSupport)
        Lksub1 = Li.copy()
        if len(Lksub1) == 0:
            break
        L.append(Lksub1)
        for lk in Lksub1:
            freq_itemsets.append((lk, supportData[lk]))
        i += 1

    return L, freq_itemsets


def generate_rules(L, minConf):
    big_rule_list = []
    sub_set_list = []
    for i in range(0, len(L)):
        for freq_set in L[i]:
            for sub_set in sub_set_list:
                if sub_set.issubset(freq_set):
                    support = supportData[freq_set] / supportData[freq_set - sub_set]
                    big_rule = (freq_set - sub_set, sub_set, support)
                    if support >= minConf and big_rule not in big_rule_list:
                        big_rule_list.append(big_rule)
            sub_set_list.append(freq_set)
    return big_rule_list


supportData = {}
freq_itemsets = []
dataSet = [('尿布', '啤酒', '奶粉', '洋葱'), ('尿布', '啤酒', '奶粉', '洋葱'), ('尿布', '啤酒', '苹果', '洋葱'), ('尿布', '啤酒', '苹果'), ('尿布', '啤酒', '奶粉'),
           ('尿布', '啤酒', '奶粉'), ('尿布', '啤酒', '苹果'), ('尿布', '啤酒', '苹果'), ('尿布', '奶粉', '洋葱'), ('奶粉', '洋葱')]

if __name__ == "__main__":
    L, _ = generate_L(minSupport=0.6)
    big_rule_list = generate_rules(L, minConf=1)

    for Lk in L:
        print("-" * 60)
        print("元素数 k=" + str(len(list(Lk)[0])))
        print("-" * 60)
        for freq_set in Lk:
            s = str(freq_set)
            s = s[10:len(s) - 1]
            print("频繁项集:", s, " 支持度:", round(supportData[freq_set], 3))

    print("-" * 60)
    print("关联规则")
    for item in big_rule_list:
        s1 = str(item[0])
        s2 = str(item[1])
        s1 = s1[10:len(s1) - 1]
        s2 = s2[10:len(s2) - 1]
        print(s1, " ---> ", s2, " 置信度:", item[2])
