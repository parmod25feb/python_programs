# The program is to implement the stack
# Date : 22th April, 2024
# Author : Parmod Kumar

st=[]

flag=True

while flag:
    n = eval(input("\nEnter the value to add in stack : "))
    st.append(n)
    c = eval(input("\nEnter 1 to continue and 0 to exit : "))
    if c == 1:
        flag=True
    else:
        flag=False
print(f"Here is your stack : {st}")

st.pop()
print(f"Here is your stack : {st}")