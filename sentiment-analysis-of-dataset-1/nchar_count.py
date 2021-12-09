import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('sentiment2.csv', encoding='ISO-8859-1')
df = df.drop(df.columns[0], axis=1)

dict = {}
val = 0
print(len(df))
c1=0
c2=0


for i in df.index:
    val=len(df['1'][i])
    if(val>=280):
        continue
    if val>77:
        c1+=1
    if val<=77:
        c2+=1
    if val in dict:
        dict[val]+=1
    else:
        dict[val]=1

print(c1)
print(c2)
plt.bar(list(dict.keys()), dict.values())
plt.show()
