#Write a program to count number of vowels and consonents in the string 
# Date : 24th April, 2024
# Author : Parmod

#This is the list of strings in which we are going to find the longest prefix
strs = "PythOn programmIng"

def vowel_and_consonent_count(st):
    v_count=c_count=0
    ls=['a','e','i','o','u','A','E','I','O','U']
    for ch in st:
        if ch in ls:
            v_count +=1
        else:
            c_count +=1
    return v_count, c_count

res = vowel_and_consonent_count(strs)

print(f"\nGiven string : {strs} has : \nVowels count is :{res[0]} \nConsonents count is : {res[1]}\n\n")
