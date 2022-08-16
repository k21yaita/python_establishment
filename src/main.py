import pandas as pd
import os
from common import constants as const

cur = os.getcwd()

path = os.path.join(os.getcwd(), const.PATH_RELATIVE_FOLDER_DATA, const.FILENAME_ESTABLISHMENTS)
print(path)
n_employees = pd.read_csv(path, encoding='shift_jis', header=const.FILE_ESTABLISHMENTS_HEADER_LINE_NUMBER)
print(len(n_employees))
print(f'{n_employees}')

path = os.path.join(os.getcwd(), const.PATH_RELATIVE_FOLDER_DATA, const.FILENAME_EMPLOYEES)
print(path)
n_employees = pd.read_csv(path, encoding='shift_jis', header=const.FILE_EMPLOYEES_HEADER_LINE_NUMBER)
print(len(n_employees))
print(f'{n_employees}')
