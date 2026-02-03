import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("D:\\Agentic_Course\\test_data\\data.csv")
#print(df)

df_extr = df.copy()
#print(df_extr)

#print(len(df_extr))
#print(df_extr.loc[df_extr["age"] == 29])
#print(df_extr.loc[1])
df_extr.loc[len(df_extr)] = [7,"India",44,50,5000]
print(df_extr.loc[6])

plt.hist(df_extr["spend"].dropna(),bins=10)
plt.show()