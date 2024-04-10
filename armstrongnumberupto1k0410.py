# This program will print the armstrong numbers upto 1000 
# Date : 9th April, 2024
# Owner : Parmod Kumar

# Function definition to calculate and print the armstrong number
def checkarmstrong(num):
    n=num
    rem=arm=0
    while n !=0:
        rem=n%10
        arm=arm+ rem**3
        n=n//10

    if arm == num:
        print(f"{num} is armstrong number")

# Running loop to pass the nubmber starting from 0 until 1000 to the function respectively
for num in range(1000):
    checkarmstrong(num)

