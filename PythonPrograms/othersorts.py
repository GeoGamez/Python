def insertionsort(x):
    if len(x) == 0:
        return x
    else:
        sorted = []
        sorted.append(x[0])
        del x[0]
        for j in range(0, len(x)):
            store = min(x)
            for i in range(0,len(x)):
                if store == x[i]:
                    spot = i
                    break
            if sorted[-1] > store:
                sortedstore = sorted[-1]
                del sorted[-1]
                sorted.append(store)
                x.append(sortedstore)
                del x[spot]
                sorted.append(x[0])
                del x[0]
            else:
                sorted.append(x[0])
                del x[0]

    return sorted;




#def newsort(x):
 #   for j in range (1,len(x)-1):
  #      i = 0
   #     while(x[j] < x[j]-1):
    #        i += 1
     #   save = x[j]
      #  del x[j]
       # x.insert(i,save)
    #return x;
def selectionsort(x):
    for j in range(1, len(x)):
        i = 1
        if x[j] < x[j-1]:
            while x[i] < x[i-1]:
                i += 1
            save = x[j]
            del x[j]
            x.insert(i, save)
            i = 1
        else:
            print(x)

    return x;

list = [5,2,1,6,4]
sorteds = selectionsort(list)
print(sorteds)
