# AIM: Write a Python program to sum all the items in a dictionary.
# Name: Aksh K Desai 
# Id: 20CE020 
# Github Repository Link: https://github.com/AKSHDESAI1/CE259_Practical-2_Assignment.git

# Python3 Program to find sum of
# all items in a Dictionary

# Function to print sum
def returnSum(myDict):

    list = []
    for i in myDict:
        list.append(myDict[i])
    final = sum(list)

    return final


dict = {'a': 100, 'b': 200, 'c': 300, 'd': 500}
print("Sum :", returnSum(dict))
