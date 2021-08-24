
from statistics import mean, median, mode


def printname(yourName):
    print("Hello " + yourName)
    print("How are you?")
#myname = input("Enter your name")
#printname(myname)

def sillyPrint(word, runlines):
    for i in range(1,runlines+1):
        print(word)
#sillyPrint("Hi", 5)

def linear(m,x,b):
    y = (m*x)+b
    return y
def squarecibe(x):
    sq= x**2;
    cb= x**3;
    return(sq,cb)

def mmCalc(x):
    x.sort()
    if (len(x) == 0):
        print("")
        print("THE INPUT LIST IS EMPTY!")
        print("")
        return 0.0, 0.0,0.0,0.0
    else:
        if len(x) % 2 == 0:
            middle = int(len(x)/2)
            total = x[middle] + x[middle-1]
            median = total/2
            total = 0
            for i in range(0,len(x)):
                total = x[i] + total
            mean = total/len(x)
            anchor = [] #parralel list with the data
            newNum = 0 #ensures that the number we are checking is new
            dupeNum = 0 #moves down the anchor list even if the numbers are the same
            for i in range(0,len(x)):  # initialization
                anchor.append(1)
            for i in range(0, len(x)-1):
                if x[i] == x[i + 1]:
                    anchor[newNum] += 1
                    dupeNum += 1
                else:
                    newNum = newNum + 1 + dupeNum
                    dupeNum = 0
            biggest = 0
            mode = 0
            for i in range(0,len(anchor)):
                if biggest < anchor[i]:
                    biggest = anchor[i]
                    mode = i
            return (mean, median, x[mode], biggest)

        else:
            medianC = (len(x)/2)
            medianC = medianC-0.5
            median = x[int(medianC)]
            total = 0
            for i in range(0,len(x)):
                total = x[i] + total
            mean = total/len(x)
            anchor = []
            newNum = 0
            for i in range(0,len(x)):  # initialization
                anchor.append(1)
            for i in range(0, len(x)-1):
                if x[i] == x[i + 1]:
                    anchor[newNum] += 1
                else:
                    newNum += 1
            biggest = 0
            mode = 0
            for i in range(0,len(anchor)):
                if biggest < anchor[i]:
                    biggest = anchor[i]
                    mode = i

            return (mean,median, x[mode], biggest)
mylist = [4, 6,6, 9, 9, 9, 11, 16,17, 22, 34,55]
print(mean(mylist), median(mylist), mode(mylist))
#mylist = []
print(mmCalc(mylist))
