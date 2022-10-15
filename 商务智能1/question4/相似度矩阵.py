import numpy as np
import pandas as pd
import math


def get_max_min_value(martix):
    res_list_max = []
    res_list_min = []
    for j in range(len(martix[0])):
        one_list = []
        for i in range(len(martix)):
            one_list.append(martix[i][j])
        res_list_max.append(np.max(one_list))
        res_list_min.append(np.min(one_list))
    return res_list_max, res_list_min


z_dict = {'完美': 1, '优秀': 0.75, '良好': 0.5, '一般': 0.25, '差': 0}

df = pd.read_excel('E:\\大学作业\\大三作业\\商务智能\\商务智能1\\question4\\Student.xlsx',
                   nrows=5)
data = np.array(df)
row_num = data.shape[0]
column_num = data.shape[1]
max_value, min_value = get_max_min_value(data[:, 1:6])


def calculate_diff(array1, array2):
    diff = 0
    indicator = 0
    for index in range(0, len(array1)):
        if array1[index] == np.nan or array2[index] == np.nan:
            continue
        if index in [1, 2, 3, 4, 5]:
            diff += math.fabs(array1[index] - array2[index]) / (
                max_value[index - 1] - min_value[index - 1])
            indicator += 1
        if index == 7:
            diff += math.sqrt(
                pow(z_dict[array1[index]] - z_dict[array2[index]], 2))
            indicator += 1
        if index in [6, 8]:
            indicator += 1
            if array1[index] == array2[index]:
                diff += 0
            else:
                diff += 1
        if index == 9:
            if array1[index] != array2[index]:
                diff += 1
                indicator += 1
            else:
                if array1[index] != 'N':
                    indicator += 1
    return diff / indicator


def calculate_diff_matrix():

    diff_matrix = np.zeros((row_num, row_num))
    for index1 in range(0, row_num):
        for index2 in range(index1 + 1, row_num):
            diff_matrix[index2][index1] = calculate_diff(
                data[index1], data[index2])
            diff_matrix[index1][index2] = diff_matrix[index2][index1]
    return diff_matrix


print(1 - calculate_diff_matrix())
