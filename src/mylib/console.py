# coding: utf-8

import os

# メッセージ表示
def print_message(msg):
    title = os.path.basename(__file__)
    print(f'<<<{title}>>>\n{msg}\n')

def print_title(title):
    print(f'\n【{title}】')
    
# データ出力
def print_data(title, data):
    if title:
        print_title(title)
    print(f'{len(data):>8,} Records')
    print(f'{data}')

# 統計量を出力する
def print_describe(title, data):
    if title:
        print_title(title)
    print(f'{data.describe()}')

# データ型を出力する
def print_datatype(title, data):
    if title:
        print_title(title)
    print(f'{data.dtypes}')
 
# 件数を出力する
def print_count(title, data):
    if title:
        print_title(title)
    print(f'{data.count()}')
  
# 平均値を出力する
def print_mean(title, data):
    if title:
        print_title(title)
    print(f'{data.mean()}')

