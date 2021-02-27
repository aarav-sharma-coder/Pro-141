import csv
import pandas as pd

df1 = pd.read_csv("shared.csv")
df1.head()

df2 = pd.read_csv("articles.csv")
df2.head()

content = df2["eventType"].tolist()
new_data=[]
for data in content:
    if data == "CONTENT SHARED":
        content.remove(data)
    new_data.append(content)

new_data.to_csv("articles.csv")
del df2["eventType"]

df_main = df2.sort_values('total_events',ascending = True)
print(df_main.head(20))
