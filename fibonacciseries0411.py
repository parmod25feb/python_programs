# This program is to print the fibonacci series 
# Date : 11th April, 2024
# Owner : Parmod Kumar

mx = eval(input("Pls enter the max range for the fibonnaci series : "))
# mx = 30

def fibonacciseries(mx):
    a,b=0,1
    print(f"{a},{b},",end='')
    c=a+b
    while c<=mx:
        print(f"{c},",end='')
        a=b
        b=c
        c=a+b

fibonacciseries(mx)