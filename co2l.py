# This is python program to print the string like cool as co2l
# Date : 9th April, 2024
# Owner : Parmod Kumar

st = "cool"

#function definition
def coolfunction(s):
    dic={}
    for ch in s:
        if ch in dic:
            dic[ch]= dic[ch]+1
        else:
            dic[ch]=1
    return dic

# function calling
d = coolfunction(st)

# printing the string in the required format
for key in d.keys():
    if d[key] == 1:
        print(key,end='')
    if d[key]>1:
        print(f"{key}{d[key]}",end='')