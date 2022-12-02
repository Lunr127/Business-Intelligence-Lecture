from collections import Counter


# 遍历数据，进行计数
def countitem(array):
    temp = []
    for item in array:
        for value in item:
            temp.append(value)

    # 写入字典
    dict = {}
    for key in Counter(temp).keys():
        dict[key] = Counter(temp)[key]

    return dict


# 删除支持度不够的key
def deletekey(dict, support):
    temp = dict.copy()
    detele = []
    for key in dict.keys():
        if dict[key] < support:
            temp.pop(key)
            detele.append(key)
    return temp, detele


# 得到从大到小排序的数组
def sorfarray(array, dict, delect):
    newarray = []
    # 删除支持度不够的元素
    for item in array:
        temp = {}
        for value in item:
            if value in delect:
                pass
            else:
                temp[value] = dict[value]
        temp = sorted(temp.items(), key=lambda d: d[1], reverse=True)
        tem = []
        for tuple in temp:
            tem.append(tuple[0])
        newarray.append(tem)
    return newarray


# info里面元素的种类
def getkinds(array):
    temp = []
    for item in array:
        for value in item:
            if value in temp:
                pass
            else:
                temp.append(value)
    return sorted(temp)


# 得到每一个种类的所有路径
def getrootpath(kinds, newinfo, dict):
    allinfo = {}
    for kind in kinds:
        kindarr = []
        for item in newinfo:
            # 如果这一条路径包含某个种类
            itemarr = []
            if kind in item:
                for value in item:
                    if kind == value:
                        break
                    else:
                        itemarr.append(value)
            if itemarr:
                kindarr.append(itemarr)
        allinfo[kind] = kindarr

    return allinfo


# 得到所有组合的字典
def getrange(rootpath):
    alldict = {}
    for key in rootpath.keys():
        root = rootpath[key]
        # 一个元素的路径
        onearr = []
        dict = {}

        # 实现一个元素路径
        for item in root:
            for value in item:
                onearr.append(value)
                dict[value] = onearr.count(value)
        alldict[key] = dict

        # 实现两个元素路径
        for item1 in root:
            tempdict = {}
            for item2 in root:
                if item1 == item2:
                    if len(item1) > 1:
                        x = "".join(item1)
                        if x in tempdict.keys():
                            tempdict[x] += 1
                        else:
                            tempdict[x] = 1
            if tempdict:
                for x in tempdict:
                    alldict[key][x] = tempdict[x]

    return alldict


# 得到每个种类的置信度
def confidence(alldict, support, newinfo):
    newdict = {}
    for kind in alldict:
        copydict = alldict[kind].copy()
        for key in alldict[kind]:
            if alldict[kind][key] < support:
                copydict.pop(key)
        if copydict:
            newdict[kind] = copydict

    # 计算置信度
    for kind in newdict:
        for key in newdict[kind].keys():
            tempnum = newdict[kind][key]
            denominator = 0
            for item in newinfo:
                if len(key) == 1:
                    if key in item:
                        denominator += 1
                elif len(key) == 2:
                    if key[0] in item and key[1] in item:
                        denominator += 1
                elif len(key) == 3:
                    if key[0] in item and key[1] in item and key[2] in item:
                        denominator += 1

            newdict[kind][key] = str(tempnum) + "/" + str(denominator)
    return newdict


if __name__ == '__main__':
    support = 3
    info = [('尿布', '啤酒', '奶粉', '洋葱'), ('尿布', '啤酒', '奶粉', '洋葱'), ('尿布', '啤酒', '苹果', '洋葱'), ('尿布', '啤酒', '苹果'),
            ('尿布', '啤酒', '奶粉'), ('尿布', '啤酒', '奶粉'), ('尿布', '啤酒', '苹果'), ('尿布', '啤酒', '苹果'), ('尿布', '奶粉', '洋葱'), ('奶粉', '洋葱')]
    # 遍历数据，进行计数
    dict = countitem(info)
    # 删除支持度不够的key
    dict, delete = deletekey(dict, support)
    # 得到从大到小排序的数组
    newinfo = sorfarray(info, dict, delete)
    # info里面元素的种类
    kinds = getkinds(newinfo)
    # 得到每一个种类的所有路径
    rootpath = getrootpath(kinds, newinfo, dict)
    # 得到所有组合的字典
    alldict = getrange(rootpath)
    # 得到每个种类的置信度
    confidence(alldict, support, newinfo)

print('-' * 50)
print("dict")
print(dict)
print('-' * 50)
print("alldict")
print(alldict)
print('-' * 50)
print("confidence")
print(confidence(alldict, support, newinfo))
print('-' * 50)
