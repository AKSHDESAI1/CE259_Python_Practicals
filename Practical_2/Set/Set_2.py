# AIM: Write a Python program to remove an item from a set if it is present in the set.
# Name: Aksh K Desai 
# Id: 20CE020 
# Github Repository Link: https://github.com/AKSHDESAI1/CE259_Practical-2_Assignment.git

def isRemove(element):
    if element in a:
        a.discard(element)
        return a
    else:
        return 'This element does not exist in set'


a = set([1, 2, 3, 4])
print(isRemove(200))
