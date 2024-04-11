# Will count even and odd number in the given array 
# Date : 11th April, 2024
# Owner : Parmod Kumar

ls = [4,5,10,3,9,7,6]

# Function definition to count even and odd number in the list
def countevenodd(ls):
    even=[]
    odd=[]
    ev=od=0
    for item in ls:
        if item%2 == 0:
            ev=ev+1
            even.append(item)
        else:
            od = od+1
            odd.append(item)
    print(f"My list is : {ls}")
    print(f"List has {ev} even numbers and {od} odd numbers")
    print(f"Even number list : {even}\nOdd number list: {odd}")

# Calling the function by passing the given list as an argument
countevenodd(ls)

# Output:

# My list is : [4, 5, 10, 3, 9, 7, 6]
# List has 3 even numbers and 4 odd numbers
# Even number list : [4, 10, 6]
# Odd number list: [5, 3, 9, 7]