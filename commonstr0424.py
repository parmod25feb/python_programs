#Longest Common Prefix: Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string.
# Date : 24th April, 2024
# Author : Parmod

#This is the list of strings in which we are going to find the longest prefix
strs = ["flower","flight","flow"]

#Function definition to return either empty string or the longest prefix
def longest_common_prefix(st):
    if not st:
        return " "
    
    prefix=""
    st.sort()
    for i in range(len(st[0])):
        if st[0][i] == st[-1][i]:
            prefix +=st[0][i]
        else:
            break
    return prefix
#Calling the function by passing the string and storing the results in the result variable
result = longest_common_prefix(strs)

#Printing the longest common prefix string using f string
print(f"\nLongest common prefix is : {result}\n")