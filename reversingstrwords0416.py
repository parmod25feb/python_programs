# This program to reverse the string - "This is a test sentence" like "sentence test a is This"  
# Date : 16th April, 2024
# Author : Parmod Kumar

st1="This is a test sentence"
ls= st1.split(" ")

# Function definition for string reverse
def str_reverse(ls):
    new_st=""
    for i in range(len(ls)-1,-1,-1):
        new_st=new_st + ls[i]
        new_st +=' '
    print(new_st)

# Calling the function to reverse the string by passing the list with words
str_reverse(ls)

# Output : sentence test a is This 