# This program is to get the reverse of the number

num = eval(input("Pls enter your number : "))

def getreverse(num):
    print(num)
    rem=total=0
    while num !=0:
        rem = num%10
        total = total*10 + rem
        num=num//10
    return total


rev = getreverse(num)
print("The reverse of {} is : {}".format(num,rev))