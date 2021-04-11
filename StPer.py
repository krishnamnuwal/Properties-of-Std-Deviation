##Importing all the required modules
import plotly
import csv
import plotly.figure_factory as ff 
import pandas as pd 
import statistics

##storing the data of the file studentPerformance in file var
file=pd.read_csv("StudentsPerformance.csv")

 ## Graph of score of all three subjects(maths,writing,reading) ##

# mathScore=(file["math score"])
# readScore=(file["reading score"])
# writScore=(file["writing score"])

# hist_data=[mathScore,readScore,writScore]
# group_labels=['math','read','write']

# figure=ff.create_distplot(hist_data,group_labels,show_hist=False)
# plotly.offline.plot(figure)


##creating a empty list for storing the data of math
histData=[]

##storing the data of all math score in to the math var
math=(file["math score"].tolist())

##adding data to the histData list
histData.append(math)

##label for graph
label=['result']

# print(math)

##command to display the normal distribution graph
fig=ff.create_distplot(histData,label,show_hist=False)
plotly.offline.plot(fig)


##calculating the mean
mean=sum(math)/len(math)
print("mean=",mean)

##calculating the median
medi=statistics.median(math)
print("median=",medi)

##calculating the mode
moad=statistics.mode(math)
print("mode=",moad)

##calculating the standard deviation
std=statistics.stdev(math)
print("stanadard deviation=",std)


##storing the values of subtrated and added standard deviaton to  mean
first_std_dev_strt=mean-std
first_std_dev_nd=mean+std


##storing the values of subtrated and added double of standard deviaton to  mean
# first_ std_dev_strt=mean-2*std
# first_std_dev_nd=mean+2*std

##storing the values of subtrated and added triple of standard deviaton to  mean
# first_std_dev_strt=mean-3*std
# first_std_dev_nd=mean+3*std



data=[result for result in math if result>first_std_dev_strt and result<first_std_dev_nd]
print("% of data lies is",format(len(data)*100.0/len(math)))








































