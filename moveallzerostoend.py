# Program to moves all zeros to end

num = input("Enter your number including zeros : ")
# Function definition
def movesallzerostoend(num):
    st1=st2=""
    for i in num:
        if int(i) > 0:
            st1=st1+i
        else:
            st2=st2+i

    return st1+st2
# Calling the function
s= movesallzerostoend(num)
print("Here is your result string after moving all zeros to end : ",s)
