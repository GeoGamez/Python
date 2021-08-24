def myfact(n):
    if (n==0):
        return 1 #base case
    elif(n>0):
        return(n* myfact(n-1))
    else:
        return -1

#print(myfact(996))

def myfactw(n):
    print(n)
    return (n * myfactw(n - 1))



#print(myfactw(10))
def myFib(n):
    if (n==0):
        return 0
    elif (n==1):
        return 1
    elif (n>1):
        return (myFib(n-1) + myFib(n-2))
    else:
        return -1
print(myFib(33))