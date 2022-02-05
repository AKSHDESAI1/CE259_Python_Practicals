# Aim: You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa. 
# Sample Input: HackerRank.com presents "Pythonist 2".
# Sample Output: hACKERrANK.COM PRESENTS "pYTHONIST 2".

# Name: Aksh k Desai
# Id: 20CE020
# Github Repository Link: https://github.com/AKSHDESAI1/CE259_Practical-2_Assignment.git

user_input = input()
str = ''
for i in user_input:
    if i == i.upper():
        str += i.lower()
    elif i == i.lower():
        str += i.upper()
    else:
        str += i
print(str)

