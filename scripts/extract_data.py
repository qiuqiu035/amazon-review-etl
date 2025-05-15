import pandas as pd
df = pd.read_csv('F:/amazon-review-etl/data/Reviews.csv')
print(df.head())
print(df.info())

df = df.drop_duplicates(subset=['ProductId', 'UserId', 'Text'])
df = df.dropna(subset=['ProfileName', 'Summary'])
df['Time'] = pd.to_datetime(df['Time'], unit='s')
df['Review_length'] = df['Text'].apply(len)
df['Word_count'] = df['Text'].apply(lambda x:len(str(x).split()))

df_clean = df[['ProductId', 'UserId', 'ProfileName', 'Score', 'Time', 'Summary', 'Text', 'Review_length', 'Word_count']]
print(df_clean.head())
print(df_clean.info())

df_clean.to_csv('data/clean_reviews.csv', index=False)