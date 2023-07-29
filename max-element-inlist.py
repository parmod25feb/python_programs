ls = [104,15,9,0,16,18]

print("Your list is : ", ls)

print("\n Maximum list element is : ", end="")

mx = ls[0]
ln = len(ls)
for i in range(1,ln):
    if mx < ls[i] :
        temp = mx
        mx = ls[i]
        ls[i]= temp

print(mx)