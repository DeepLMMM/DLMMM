import torch
import torch.nn as nn


from DataStruct.globalConfig import GlobalConfig
from DataStruct.flatOperatorMap import FlatOperatorMap
from DataStruct.operation import Operator

class edge:
    fromIndex = 0
    toIndex = 0
    # 为了方便格式转化，且涉及的操作仅为基本操作，故只保留操作号，不保留层号
    operator = 0
    index = ""
    def __init__(self, FromIndex, ToIndex, Operator):
        self.fromIndex = FromIndex
        self.toIndex = ToIndex
        self.operator = Operator


def parse_Type(Type):
    if Type in GlobalConfig.basicOps:
        res = GlobalConfig.basicOps.index(Type) - 1
    else:
        res = -1
    return res

def Decode(type, ch):
    res = 1
    same_channel_operators = [-1, 2, 4, 5, 8, 9, 10, 11, 12, 13, 14]
    if type in same_channel_operators:
        res = ch

    return res

def search_zero(in_degree, size):
    for i in range(size):
        if in_degree[i] == 0:
            return i
    return -1

def decodeChannel(f):
    global mainPath
    global branches
    #注：输入类型为flatOperaotrMap

    #先把f.chanels扩大
    f.channels = [0]*f.size
    f.channels[0] = 1
    in_degree = [0]*f.size
    for j in range(f.size):
        for i in range(f.size):
            if f.Map[i][j].m != 0:
                in_degree[j] += 1

    #最多拓扑f.size轮
    for times in range(f.size):
        # 找到入度为0的点
        target = search_zero(in_degree, f.size)
        if target < 0:
            print("Error! Circle exits!")
            return


        in_degree[target] = -1
        for j in range(f.size):
            if f.Map[target][j].m != 0:

                in_degree[j] -= 1
                f.channels[j] += Decode(f.Map[target][j].m, f.channels[target])
                Operation = f.Map[target][j].m
    return

def count_operator(model_str):
    # 统计模型基本信息（e.g., channels）
    if model_str.find("  ")!=-1:
        operators = model_str.split("  ")
    elif model_str.find(",")!=-1:
        operators = model_str.split(" ")
    operatornum = 0
    for each_operator in operators:
        if each_operator == '\n' or each_operator.find(",,")!=-1:
            continue
        if each_operator.find(" ")!=-1:
            each_operator=each_operator.split(" ")
        elif each_operator.find(",")!=-1:
            each_operator=each_operator.split(",")
        this_operator=each_operator[-1][9:]
        if this_operator!="identity":
            operatornum+=1

    return operatornum

f1 = open('./muffin_model.csv', encoding = 'utf-8')
model_num = 0
total_operator_num = 0
while True:
    print(model_num)
    model_num += 1
    this_model_str = f1.readline()
    if this_model_str=="":
        break
    operatornum = count_operator(this_model_str)
    total_operator_num += operatornum
average_operator_num = total_operator_num/model_num
print(average_operator_num)