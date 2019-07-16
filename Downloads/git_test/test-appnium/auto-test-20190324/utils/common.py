import os
import csv
"""获取路径的上一级"""
def get_parent_path(current_path):
    return os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")

def get_data_csv(filename):
    numbers = []
    with open(filename,'r',encoding='utf-8') as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            numbers.append(row)
    return numbers