# AIM: Write a Python script to check whether a given key already exists in a dictionary.
# Name: Aksh K Desai 
# Id: 20CE020 
# Github Repository Link: https://github.com/AKSHDESAI1/CE259_Practical-2_Assignment.git

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


def is_key_present(x):
    if x in d :
        print('Key is present in the dictionary')
    else:
        print('Key is not present in the dictionary')


is_key_present(10)
is_key_present(9)
