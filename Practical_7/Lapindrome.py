# Aim: Lapindrome is defined as a string which when split in the middle, gives two halves having the same characters and same frequency of each character. If there are odd number of characters in the string, we ignore the middle character and check for lapindrome. For example gaga is a lapindrome, since the two halves ga and ga have the same characters with same frequency. Also, abccab, rotor and xyzxy are a few examples of lapindromes. Note that abbaab is NOT a lapindrome. The two halves contain the same characters but their frequencies do not match. Your task is simple. Given a string, you need to tell if it is a lapindrome. 

# Name: Aksh k Desai
# Id: 20CE020
# Github Repository Link: https://github.com/AKSHDESAI1/CE259_Python_Practicals.git
a = int(input())
arr = []
ans = []
for i in range(a):
    b = input()
    arr.append(b)

for j in arr:
    if len(j) % 2 == 0:
        arr1 = []
        arr2 = []
        for i in range(len(j)):
            if i <= ((len(j)/2)-1):
                arr1.append(j[i])
            else:
                arr2.append(j[i])
        for k in arr1:
            if k in arr2:
                arr1.remove(k)
                arr2.remove(k)
        for k in arr1:
            if k in arr2:
                arr1.remove(k)
                arr2.remove(k)
        if arr1 == []:
            ans.append("yes")
        else:
            ans.append("no")
    else:
        a1 = []
        for i in j:
            a1.append(i)
        q = int(len(j)/2)
        a1.remove(a1[q])

        str = ""
        for k in a1:
            str += k

        arr1 = []
        arr2 = []
        for i in range(len(str)):
            if i <= ((len(str)/2)-1):
                arr1.append(str[i])
            else:
                arr2.append(str[i])

        for k in arr1:
            if k in arr2:
                arr1.remove(k)

        for k in arr1:
            if k in arr2:
                arr1.remove(k)

        if arr1 == []:
            ans.append("yes")
        else:
            ans.append("no")

for k in ans:
    print(k)
