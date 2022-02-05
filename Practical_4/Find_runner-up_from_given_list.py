# Aim: Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.
# Name: Aksh k Desai
# Id: 20CE020
# Github Repository Link: https://github.com/AKSHDESAI1/CE259_Python_Practicals.git

user_input = int(input())
lis1 = list(map(int, input().split(' ')))
if len(lis1) == user_input:
    set1 = set(lis1)
    lis1 = list(set1)
    lis1.sort()
    lis1.reverse()
    print(lis1[1])
else:
    print(f'You input digit is {user_input} and you take {len(lis1)} input.')
