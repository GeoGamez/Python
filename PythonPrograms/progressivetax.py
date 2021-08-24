state = True #starting the loop to be true ( I know i could have just set it to true then used break)
while state:  # while loop
    userint = input("Do you want to calculate an income tax?  Y or y for yes, anything else for no:  ") #input
    if userint == "Y" or userint == "y": # checking input and starting the program
        tax = 0 # total tax
        income = int(input("Enter the gross (before tax) income without a $:  ")) # input for income
        overflow = income #I was going to do it a different way however realized it was harder to code and so I just stuck using this instead of income
        repeat = 0 # Once it finds the starting bracket it will use this variable instead to locate the next bracket
        if income > 100000.00: # biggest bracket
            overflow -= 100000
            tax += (overflow * 0.22)
            repeat = 1 # It will send it to the next bracket and subtract the max value instead of the min value
        if 30000.00 < income <= 100000.00:
            tax += ((overflow - 30000) * 0.175)
            repeat = 2
        if repeat == 1: # the biggest repeat bracket
            tax += (70000*0.175)
            repeat = 2 # sends it down to the next repeat bracket
        if 10000.00 < income <= 30000.00:
            tax += ((overflow-10000) * 0.15)
            repeat = 3
        if repeat == 2:
            tax += (20000*0.15)
            repeat = 3
        if 0 < income <= 10000.00:
            tax += (overflow * 0.1)
        if repeat == 3:
            tax += (10000 * 0.1)
        print(tax)
    else: # Once you input something not Y or y it changes the state to False ending the loop
        state = False
# Final Thoughts Could have cleaned up the code to have all the starting brackets together then all the repeats together
# Tried doing it a different way with elif and a lot less statement but ran into problems with the varible not having the right value at the right time
# So i changed it :)

