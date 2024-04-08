# This is the python program to print the first and last character of the string 

st = input("Pls enter your string : ")
print(f"Your string is : {st}")

def firstandlastch(s):
    s1=s[0]+s[-1]
    print(f"Here are the first and Last character of your string are : {s1}")


firstandlastch(st)