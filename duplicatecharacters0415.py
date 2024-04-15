# This program to find the duplicate characters in the string  
# Date : 15th April, 2024
# Author : Parmod Kumar

st1 = input("pls enter your string : ")

def duplicate_characters_in_string(st):
    dic={}
    for ch in st:
        if ch in dic:
            dic[ch] +=1
        else:
            dic[ch] =1
    return dic


final_dic= duplicate_characters_in_string(st1)

for key in final_dic:
    if final_dic[key] >1:
        print(f"{key} character occurres : {final_dic[key]} times")

    
