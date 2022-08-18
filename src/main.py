# import pandas as pd
# import os
from common import constants as const
from mylib import faccess as facs
from mylib import console as con

# データファイルの読み込み
def read_datas():
    path = facs.gen_absolute_path(const.PATH_RELATIVE_FOLDER_DATA, const.FILENAME_ESTABLISHMENTS)
    n_establishments = facs.read_csvfile(path, 'shift_jis', const.FILE_ESTABLISHMENTS_HEADER_LINE_NUMBER)
    con.print_data('事業所数', n_establishments)

    path = facs.gen_absolute_path(const.PATH_RELATIVE_FOLDER_DATA, const.FILENAME_EMPLOYEES)
    n_employees = facs.read_csvfile(path, 'shift_jis', const.FILE_EMPLOYEES_HEADER_LINE_NUMBER)
    con.print_data('従業員数', n_employees)

    return n_establishments, n_employees

# ====================================================================
# main routine
# ====================================================================
# ファイルを読み込む
read_datas()
