import statistics as stats

#ejercicios medidas de dispersion
'''
1.1 What is the range for the data set?
1.2 How does the standard deviation change when 6 is replaced with 12? Does it increase, or decrease, or it remains the same?
1.3 Is is possible to have a dataset with 0 standard deviation or variance? 
If yes, can you think of any dataset with 6 data points that have 0 standard deviation?
1.4 We know that standard deviation is a measure of spread in the dataset. What is meant by deviation here?
What is the formula for calculating deviation? Can deviation be negative?
1.5 What is the deviation from the mean for each of the points in the list? Write a for loop and print each of the values.
1.6 How is standard deviation different than variance?
'''
#1.1
points = [-4, 17, 25, 19, 6, 11, 7]
range = max(points)- min(points)
print('El rango es '+ str(range))

#1.2
data = [2,4,7,1,6,8]
b=stats.stdev(data)
print(b)
data[-2] = 12
a = stats.stdev(data)
print(a)

#1.3
'''
Yes, it is posible.
'''
c = [2,2,2,2,2,2]
dc = stats.stdev(c)
print(dc)

#1.4
'''
the variation between values. The formula would be sum of (xi - mean(x))^2/N and a standard desviation cant be negative.
'''
#1.5  no he sido capaz de sacarlo

data = [23, 12, 34, 65, 34, 81]

for item in data:
    print("Deviation for item: ", item, "is: ", item - stats.mean(data))

#1.6
'''
Even though both variance and standard deviation are measures of spread/dispersion, there is a difference in the units of the two things.
Unit of variance is squared of the unit of the original data while unit of standard deviation is same as the unit of the original data. 
Therefore for practical purposes, sometimes people prefer to use standard deviation instead of variance.
Also since variance is square of standard deviation, if the value of standard deviation is large then the magnitude of variance becomes larger. 
Sometimes it is prefereable to work with numbers of lesser magnitudes
'''












