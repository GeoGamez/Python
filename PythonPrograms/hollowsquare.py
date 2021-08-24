
integer= int(input("Please enter a number 1 or greater: "))

#square
if integer == 1:
    print("*")
else:
    count = integer -2; # this is to make the hollow gap fit into the square
    print('*'*integer) # top of square
    for x in range(2,integer): # middle of square
        print('*'+ " "*count +'*')
    print('*'*integer) # bottom of square



