intlist = [11,33,50]
s =""
for i in intlist:
    s = s + str(i)
s = int(s)
print(s)

result = 0
for i in intlist:
    result = result*100 + i
print(result)