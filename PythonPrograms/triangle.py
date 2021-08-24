#input for both programs
integer= int(input("Please enter a number 1 or greater: "))
#triangle
if integer == 1:
  print("*")
else:
  print('*') #the starting triangle always only has 1 *
  for x in range(0,integer-2): # this for loop prints all the hollow chucks and to ensure inputting 1 and 2 don't make *'s I subtract 2
      print('*' + " " * x + '*')
  print('*'*integer) # closing the triangle
