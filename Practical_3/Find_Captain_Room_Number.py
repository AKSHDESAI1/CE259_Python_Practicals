# Aim:-
# Input Format:-
#     => The first line consists of an integer, K , the size of each group.
#     => The second line contains the unordered elements of the room number list.
# Constraints: 1< K<1000
# Output Format: Output the Captain's room number.

# Name: Aksh K Desai
# Id: 20CE020
# Github Repository Link: https://github.com/AKSHDESAI1/CE259_Python_Practicals.git

user_input = int(input())
lis1 = list(map(int, input().split(' ')))

c = 0
for i in lis1:
    count1 = lis1.count(i)
    if count1 == 1:
        answer = i
    elif count1 == user_input:
        pass
    else:
        c = 1

if c == 1:
    print('something wrong Data.Please Try again')
else:
    print(answer)
