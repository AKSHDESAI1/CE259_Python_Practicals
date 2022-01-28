# AIM: Write a Python script to add a key to a dictionary.
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}

# Name: Aksh K Desai 
# Id: 20CE020 
# Github Repository Link: https://github.com/AKSHDESAI1/CE259_Practical-2_Assignment.git

d = {0:10, 1:20}
d.update({2:30})
print(d)