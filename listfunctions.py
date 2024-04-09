# This is python program to show how list functions work
# Date : 9th April, 2024
# Owner : Parmod Kumar

#Here we have to lists
ls1 = [2,6,9,1,4]
ls2 = [11,34,10]

# Sorting the first list
ls1.sort()
print(ls1)

# Reversing the first list
ls1.reverse()
print(ls1)

# Length of the first list 
print(f"Length of the first list : {len(ls1)}")

# Adding an element at the end of the list1 
ls1.append(55)
print(ls1)

# Print the index of last element 
try:
    print(f"List element at 2nd index : {ls1.index(15)}")
except:
    print("Index out of range")