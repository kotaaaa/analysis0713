# coding: UTF-8
# Dataframe.to_excel()テスト
import pandas as pd
import xlrd
import openpyxl

# データフレームを用意
dataframe1 = pd.DataFrame([['aa', 'bb'], ['cc', 'dd']], columns = ['columnA', 'columnB'])
dataframe2 = pd.DataFrame([[1, 2], [3, 4]], columns = ['columnA', 'columnB'])

# 出力ファイル名を指定
excel_writer = pd.ExcelWriter('output.xlsx')
print(type(excel_writer))

# シート名を指定してデータフレームを書き出す
dataframe1.to_excel(excel_writer, 'hogefuga sheet')
dataframe2.to_excel(excel_writer, 'number sheet')
print(type(dataframe1))
print(type(dataframe2))
exit()
# 書き出した内容を保存する
excel_writer.save()
