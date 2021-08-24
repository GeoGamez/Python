def bubblesort(x):
    scan = len(x)-1
    for j in range(0,len(x)-1):
        for passnum in range(0,scan):
            if x[passnum] > x[passnum+1]:
                store = x[passnum]
                x[passnum] = x[passnum+1]
                x[passnum+1] = store
        scan -= 1;
    return x;


list = [5,2,3,6,7]
list1 = [5,2,3,6,7,2,4,5,6,3,6,2,36,23,6,2,3,6,7,2,34,6,2,67,6,3,4,64,2,35,3,2,53,54,43,63,3,45,2]
list2 = []
list3 = [0]
list4 = [12,23]
sorteds = bubblesort(list)
sorteds1 = bubblesort(list1)
sorteds2= bubblesort(list2)
sorteds3= bubblesort(list3)
sorteds4 = bubblesort(list4)
print (sorteds)
print (sorteds1)
print (sorteds2)
print (sorteds3)
print (sorteds4)

