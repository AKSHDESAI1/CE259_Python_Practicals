# Write a procedure to find min, max, mean, standard deviation, variance  of  number list. Example Input :  10  50  80  70  49  23  11   4output :  4  80  37. 13  27. 25  848. 70

# Name: Aksh k Desai
# Id: 20CE020
# Github Repository Link: https://github.com/AKSHDESAI1/CE259_Python_Practicals.git

import statistics

number = list(map(int,input().split()))

max_number = max(number)
min_number = min(number)
mean_number = round(statistics.mean(number),2)
standard_deviation = round(statistics.stdev(number),2)
variance_number = round(statistics.variance(number),2)

print(max_number, min_number, mean_number, standard_deviation, variance_number)
