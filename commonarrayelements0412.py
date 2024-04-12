# This program will find the common elements in the two arrays
# Date : 12th April, 2024
# Author : Parmod Kumar

arr1 = [12,13,14,5,9]
arr2 = [7,4,13,8,2]

def common_array_elements(ar1,ar2):
    ls=[]
    if len(ar1) != len(ar2):
        print("Sorry, array size should be equal")
    else:
        for i in range(len(ar1)):
            for j in range(len(ar2)):
                if ar1[i]==ar2[j]:
                    ls.append(ar1[i])
                else:
                    continue

    return ls
     
lst = common_array_elements(arr1,arr2)
if len(lst) > 0:
    print(f"Common array elements are : {lst}")
else:
    print("Sorry there are no common elements")