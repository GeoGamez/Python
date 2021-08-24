#write a program that makes a grid of * from imput
integer= int(input("Please enter a number 1 or greater: "))
easy (i don't think this works in java
for x in range(1,integer+1):
   print("*" * integer)

#nestedforloop (cool?)
for x in range(1, integer+1):
    for y in range(1, integer+1):
        print("*", end='')
    print(" ")

#List? (really dumb way)
horizontal =list()
for x in range(1,integer+1):
    horizontal.append("*")
for x in range(1,integer+1):
    print(''.join(horizontal))


