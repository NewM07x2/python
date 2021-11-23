"""
    テンプレ諸元選択
"""
# coding=utf-8
import os
import sys
import json
import csv
import glob
import pandas as pd
import numpy as np

"""
    初期設定
"""
master_json = {
    'key': 'value'
}
os.chdir(r"/Applications/MAMP/htdocs/python/tool/dist")

def main():
    excelData = pd.read_excel('master/master.xlsx', sheet_name='マスタ', index_col=0)

    for row in excelData.values:
        key = ''
        value = row[0]
        for index in range(1,len(row)):
            key += str(row[index])  
        master_json[key] = value
    # print(master_json)
    paths = glob.glob("csv/before/*.csv")
    files = []
    for path in paths:
        files.append(os.path.basename(path))

    for fileName in files:
        print(fileName)
        csvData = pd.read_csv('csv/before/{}'.format(fileName),sep=',')
        csvList = []
        for row in csvData.values:
            key = ''
            for index in range(4,14):
                if index != 0:
                    key += str(row[index])
            csvList.append(key)

        for index, key in enumerate(csvList):
            csvData['テンプレ諸元'] = csvData['テンプレ諸元'].astype(str)
            if key in master_json:
                csvData.iat[index, 2] = master_json[key]
            else:
                csvData.iat[index, 2] = ''
                
        csvData = csvData.drop(columns=csvData.columns[4:],axis=1)

        csvData.to_csv('csv/after/{}'.format(fileName), index=False)

if __name__ == '__main__':
    print('---■ 処理開始 ■---')
    main()
    print('---■ 処理終了 ■---')
    input("何かキーを押すと終了します。")
