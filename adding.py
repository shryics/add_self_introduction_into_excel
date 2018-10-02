import pandas as pd
import os

books = ['main.xlsx']
df = pd.DataFrame()
for book in books:
    file = pd.ExcelFile(book) # bookを読む
    for sheet in file.sheet_names:
        df = df.append(file.parse(sheet)) # シートを順々にデータフレーム化

path = 'text_folders/'
for filename in os.listdir(path):
    f = open(path + filename)
    comment = f.read()
    f.close()
    df["自己紹介文"][df["社員番号"] == int(filename.split('.')[0])] = comment

df.to_excel("added_main.xlsx", index=None)
print(df)