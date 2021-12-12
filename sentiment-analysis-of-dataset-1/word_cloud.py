import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pandas as pd
df = pd.read_csv('sentiment2.csv')
plt.imshow(WordCloud().generate(str(df['1'].values)))
plt.axis("off")
plt.show()