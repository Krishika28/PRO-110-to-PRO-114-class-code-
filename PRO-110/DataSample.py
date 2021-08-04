import pandas as p
import statistics as s
import plotly.figure_factory as ff
import random 

#reading the csv data into Dataframe and converting into list
df = p.read_csv("newdata.csv")
df_list = df["average"].tolist()

def find_mean_stdev(dataList):
    mean = s.mean(dataList)
    stdev = s.stdev(dataList)

    return mean,stdev

mean, stdev = find_mean_stdev(df_list)
print(f"population mean of the data is {mean} and its standard deviation is {stdev}")


def create_fig(list_data):
    fig = ff.create_distplot([list_data],["average"], show_hist= False)
    fig.show()


def sampling(list_data, number_of_items):
    sample_datalist=[]
    for i in range(0,number_of_items):
        random_index = random.randint(0, len(list_data)-1)
        value = list_data[random_index]
        sample_datalist.append(value)
        
    mean_sample = s.mean(sample_datalist)
    stdev_sample = s.stdev(sample_datalist)

    return mean_sample


def main():
    sample_meanList=[]
    for i in range(0,2000):
       
        sampleMean = sampling(df_list, 200)
        #1000 means of the 1000 sample of 100 items each
        sample_meanList.append(sampleMean)

    mean_sample, stdev = find_mean_stdev(sample_meanList)
    print(f"mean of the sampling distributin is {mean} and its standard deviation is {stdev}")

    #Sampling mean distributin
    create_fig(sample_meanList)

main()