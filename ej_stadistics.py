import statistics as stats

'''
1.1 We saw that a dataset can have more than one mode. But can a dataset have more than one median? True or False.
1.2What is the mean, median, and mode of the dataset.
Create a new dictionary called data_dictionary and store the above answers as key value pairs in the dictionary.
1.3 To find which statistic do you have to arrange the data in an ascending order?
1.4 How do you find the median when there are even number of data points?
1.5 What are outliers in a dataset? Which of the three - Mean, Median, and Mode -
is more susceptible to change with presence of outliers in the data?
'''
#1.1
'''
The anserw is False, there´s only one median in each dataset.
'''
#1.2
data = [4, 7, 5, 9, 8, 6, 7, 7, 8, 5, 6, 9, 8, 5, 8, 7, 4, 7, 3, 6, 8, 9, 7, 6, 9]

mean_data = stats.mean(data)
median_data = stats.median(data)
mode_data = stats.mode(data)
data_dictionary = {}
data_dictionary['mean_data'] = mean_data
data_dictionary['median_data'] = median_data
data_dictionary['mode_data'] = mode_data
#1.3
'''
You need de median.
'''
#1.4
'''
If the number of data points is even Median is the arithematic mean of (N/2)th term and (N/2 + 1)th term
'''
#1.5
'''
An outlier is an observation that lies an abnormal distance from other values in a random sample from a population or datasets. 
the mean is the stadistc that`s susceptible to outliers.
'''