# This program will show how we can reverse a string using different methods 
# Date : 10th April, 2024
# Owner : Parmod Kumar

st = input("Pls enter your string : ")

# String reverse using slice method
s= st[::-1]
print(s)

# String reverse using for loop
st1=""
for i in range(len(st)-1,-1,-1):
    st1=st1+st[i]
print(st1)