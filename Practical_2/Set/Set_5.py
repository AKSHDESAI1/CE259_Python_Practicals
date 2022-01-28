# AIM: Write a Python program to find the most common elements and their counts from list, tuple, dictionary.
# Name: Aksh K Desai 
# Id: 20CE020 
# Github Repository Link: https://github.com/AKSHDESAI1/CE259_Practical-2_Assignment.git

# Program to find most frequent
# element in a list

def most_CommonList(List):
    counter = 0
    num = List[0]

    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency > counter):
            counter = curr_frequency
            num = i

    return num, counter


List = [2, 1, 2, 2, 2, 1, 3]
ans = most_CommonList(List)
print(f'Your most common Elements in list is {ans[0]} and this is repeat {ans[1]} times.')

# element in a tuple


def commonElement_tuple(List):
    counter = 0
    num = List[0]

    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency > counter):
            counter = curr_frequency
            num = i

    return num, counter


List = (3, 4, 5, 4, 3, 2, 1, 2, 3)
ans1 = commonElement_tuple(List)
print(f'Your most common Elements in tuple is {ans1[0]} and this is repeat {ans1[1]} times.')


# most common elements in dictionary
a = {'a': 1, 'b': 2, 'c': 1, 'd': 2, 'e': 2}
lis = []
for i in a.values():
    lis.append(i)


def most_CommonDictionary(List):
    counter = 0
    num = List[0]

    for j in List:
        curr_frequency = List.count(j)
        if(curr_frequency > counter):
            counter = curr_frequency
            num = j

    return num, counter


ans2 = most_CommonDictionary(lis)
print(f'Your most common Elements in Dicionary is {ans2[0]} and this is repeat {ans2[1]} times.')
