# This is my python program to check if a number is armstrong nubmer or not
# Date : 08 April, 2024
num = eval(input("Pls enter the number : "))

def armstrongnumbercheck(n):
    rem=num1=0
    while n!=0:
        rem = n%10
        num1= num1+ rem**3
        n=n//10
    return num1

ret = armstrongnumbercheck(num)
if num == ret:
    print(f"Since {ret} is equal to the number {num}, hence it is ARMSTRONG number")
else:
    print("Sorry")
