# This is the python program to convert a list of characters into the String
# Date : 08 April, 2024
# Author : Parmod 

lst = ['P','a','r','m','o','d']

def chartostring(ls):
    st = ''.join(ls)
    return st

s = chartostring(lst)
print(f"Here is your string : {s} \nCreated from the list : {lst}")