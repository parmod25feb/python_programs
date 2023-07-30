# This program is to find the armstrong numbers between 100 to 999

start_number = 100
end_number = 999

for num in range(start_number,end_number):
    num1=num
    rev=rem=0
    newnum=0
    while num != 0:
        rem = num%10
        newnum = newnum + rem**3
        num = num//10
    
    if newnum==num1:
        print(num1)
