# This is the matrix operation program
# Date : 23rd April, 2024
# Author : Parmod Kumar

matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

def sumofmetrix(m1,m2):
    result=[]
    if len(m1) != len(m2):
        print("Sorry sum is not possible.....")
    else:
        for i in range(len(m1)):
            row=[]
            for j in range(len(m1[0])):
                row.append(m1[i][j] + m2[i][j])
            result.append(row)
    return result
res = sumofmetrix(matrix1,matrix2)

print(f"\nHere is the result metrics :")
for i in res:
    print(i)



