import statistics as s
import pandas as p
import plotly.figure_factory as ff
import plotly.graph_objects as go
import random as r

school1 = p.read_csv("School1.csv")
df = p.read_csv("data1.csv")
df2 = p.read_csv("data2.csv")
df3 = p.read_csv("data3.csv")

print(df[0:5])
print(df.columns)

school1_data = df["Math_score"].tolist()
list = df["Math_score"].tolist()
list2 = df2["Math_score"].tolist()
list3 = df3["Math_score"].tolist()

mean = s.mean(list)
mean2 = s.mean(list2)
mean3 = s.mean(list3)
std = s.stdev(list)

print("mean of interventation1: ",mean)
print("Standard Devation of interventation1: ",std)

def random_sample():
    data = []
    for i in range(0,100):
        random_index = r.randint(0,len(school1_data)-1)
        value = school1_data[random_index]
        data.append(value)
    mean = s.mean(data)
    return mean

mean_list = []

for i in range(0,1000):
    m = random_sample()
    mean_list.append(m)

sample_mean = s.mean(mean_list)
stdev = s.stdev(mean_list)

print("mean of sampling distribution: ",sample_mean)
print("Standard Devation of sampling distribution: ",stdev)

zScore = (sample_mean-mean)/stdev
print("Z Score of inteventation1",zScore)

zScore2 = (sample_mean-mean2)/stdev
print("Z Score of inteventation2",zScore2)

zScore3 = (sample_mean-mean3)/stdev
print("Z Score of inteventation3",zScore3)

fig = ff.create_distplot([mean_list],["Student Marks"], show_hist = False)
fig.add_trace(go.Scatter(x = [sample_mean, sample_mean], y = [0,0.17], mode = "lines", name = "Sample Mean"))

fig.add_trace(go.Scatter(x = [mean, mean], y = [0,0.17], mode = "lines", name = "Mean of students with interventation1"))
fig.add_trace(go.Scatter(x = [mean2, mean2], y = [0,0.17], mode = "lines", name = "Mean of students with interventation2"))
fig.add_trace(go.Scatter(x = [mean3, mean3], y = [0,0.17], mode = "lines", name = "Mean of students with interventation3"))

fig.show()