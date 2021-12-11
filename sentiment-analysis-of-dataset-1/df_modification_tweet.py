import pandas as pd
from sklearn.utils import shuffle
from ast import literal_eval

df = pd.read_csv('modified_csv.csv', encoding='ISO-8859-1',converters={"1": literal_eval},dtype={'t':'string'})

#print(df.dtypes)
df.drop(df.columns[0], axis=1)
#df = df[len(df.t) < 77]

lis = []

for i in df.index:
    # print(i)
    if len(df['t'][i])>=77:
        lis.append(i)

lis = set(range(df.shape[0])) - set(lis)
df = df.take(list(lis))

df.reset_index(inplace=True, drop=True)
df.rename(columns={df.columns[0]: "0"}, inplace=True)
df.rename(columns={df.columns[1]: "1"}, inplace=True)

df=df.head(20000)
df.to_csv('modified_csv-77.csv')