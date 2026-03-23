import csv

import numpy
import scipy.stats

time = []
operator_combination_variety = []
bug_detection_performance = []

with open('./gandalf_measurement.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # 跳过标题行
    for row in reader:
        time.append(float(row[0]))
        operator_combination_variety.append(float(row[1]))
        bug_detection_performance.append(float(row[2]))
    print(scipy.stats.spearmanr(time,operator_combination_variety))
    print(scipy.stats.spearmanr(time,bug_detection_performance))
    print(scipy.stats.spearmanr(operator_combination_variety,bug_detection_performance))
