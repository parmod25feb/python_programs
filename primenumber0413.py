# This program will print the prime number < 20
# Date : 13th April, 2024
# Author : Parmod Kumar

def primenumbers(max):
    ls=[]
    for num in range(max):
        if num ==1:
            # print(f"{num} is not prime")
            continue
        elif num>1:
            for i in range(2,num):
                #print(num%i)
                if (num%i) == 0:
                    # print(f"{num} is not prime")
                    break
            else:
                ls.append(num)
    print(f"Here is the list of the prime numbers : {ls}")

flag = True
while flag:
    mx = eval(input("Enter your max number : "))
    primenumbers(mx)
    bl = eval(input("\nPress 1 to continue and 0 to exit : "))
    print(type(bl))
    if bl==1:
        flag= True
    else:
        flag= False

