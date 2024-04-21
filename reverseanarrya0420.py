# The program is to reverse an array - Reverse an array of 9 elements on an interval of 3 - [1,2,3,4,5,6,7,8,9] = [3,2,1,6,5,4,9,8,7] 
# Date : 20th April, 2024
# Author : Parmod Kumar

ar =  [1,2,3,4,5,6,7,8,9]\

# print the original array
print(f"\nOriginal array is : {ar}")

# Definied the function to reverse the array in the interval of 3 and then print the output
def arr_reverse(ar):
    ls=[]
    start= 0 
    end = 3
    for i in range(1,4):
        for l in range(end-1,start-1,-1):
            ls.append(ar[l])
        start +=3
        end +=3

    print(f"\nFinal arrya is : {ls}\n")

# Calling the function to get the reverse
arr_reverse(ar)


