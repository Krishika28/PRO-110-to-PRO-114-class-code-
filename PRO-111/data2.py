import statistics as s
import pandas as p
import plotly.figure_factory as ff
import random as r

df = p.read_csv("data2.csv")

print(df[0:5])
print(df.columns)

list = df["Math_score"].tolist()

mean = s.mean(list)
std = s.stdev(list)

print("mean: ",mean)
print("Standard Devation: ",std)