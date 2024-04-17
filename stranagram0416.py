# Write a function to check if two given strings are anagrams of each other. Anagrams are words or phrases formed by rearranging the letters of another word or phrase, using all the original letters exactly once.
# Date : 17th April, 2024
# Author : Parmod Kumar

st1= "ParmoD"
st2 = "pAmodR"

print(f"Given strings are : \n1st String : {st1}\n2nd String : {st2}")

def str_anagram(st1,st2):
    if len(st1) != len(st2):
        print("Sorry! strings are not annagram ... ")
    else:
        s1= st1.lower()
        s2= st2.lower()
        str1=''.join(sorted(s1))
        str2=''.join(sorted(s2))
        
        if str1 == str2:
            print(f"\nCongratulation! your strings are anagram as {str1} is same as {str2}\n")
        else:
            print(f"\nSorry! your strings are NOT anagram as {str1} is not same as {str2}\n")


str_anagram(st1,st2)