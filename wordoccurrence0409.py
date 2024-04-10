# This is python program to print the string like cool as co2l
# Date : 9th April, 2024
# Owner : Parmod Kumar

# This string can be asked to the end user to enter here by using the input function
st = "parmod kumar sharma rashmi sharma ayansh sharma prisha sharma ayansh"

# Function definition to count the words in the dictionary
def countingtheoccurrenceofwords(st):
    ls=st.split(" ")
    dic={}
    for wd in ls:
        if wd in dic.keys():
            dic[wd]=dic[wd]+1
        else:
            dic[wd]=1
    return dic
# Calling the fuction and the storing the return value in dic1
dic1= countingtheoccurrenceofwords(st)

# Traversing through the dictionary to print the words and the occurrences
for key in dic1.keys():
    print(f"{key} occurres : {dic1[key]} times")


# Output : 
# parmod occurres : 1 times
# kumar occurres : 1 times
# sharma occurres : 4 times
# rashmi occurres : 1 times
# ayansh occurres : 2 times
# prisha occurres : 1 times