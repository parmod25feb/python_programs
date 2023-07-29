ls = [11,7,88,91,3,10,12,33,-1]

def mnelement(l):
    min=l[0]
    for i in range(1,len(l)):
        if min > l[i]:
            temp = min
            min = l[i]
    txt = "Mininum array element is : {}"
    print(txt.format(min))

mnelement(ls)