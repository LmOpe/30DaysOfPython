import pandas as pd

df = pd.read_csv('./day_25/hacker_news.csv')

print(df.head())

print(df.tail())

title = df['title']

series = pd.Series(title)
print(series)

rows, columns = df.shape

print(f"Rows: {rows} and Columns: {columns}")

print(df[['python' in title for title in list(df['title'])]])


print(df[['JavaScript' in title for title in list(df['title'])]])