import pandas as pd
import os

cur = os.getcwd()

path = os.path.join(os.getcwd(), '../data/file07.csv')
print(path)
n_employees = pd.read_csv(path, encoding='shift_jis', header=7)
print(len(n_employees))
print(f'{n_employees}')

path = os.path.join(os.getcwd(), '../data/file08.csv')
print(path)
n_employees = pd.read_csv(path, encoding='shift_jis', header=7)
print(len(n_employees))
print(f'{n_employees}')
