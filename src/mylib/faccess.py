# coding: utf-8

import os
import pandas as pd


# 絶対パスの生成
def gen_absolute_path(folder_path, file_path):
    absolute_path = os.path.join(os.getcwd(), folder_path, file_path)
    return absolute_path

# CSVファイルの読み込み
def read_csvfile(path, encoding, header):
    records = pd.read_csv(path, encoding=encoding, header=header)
    return records

