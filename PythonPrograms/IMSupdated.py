ids = ["sfp", "lk"]  # item IDs
descs = ["small frying pan", "large kettle"]  # item descriptions
stock = [0, 7]  # amount we have for each item
prices = [11.95, 27.50]  # selling price for each item
# SID is a input of a id
# Nstock is a new stock amount
# Nprice is new price
# Ndescs is new desc
# error is for invaild input or potential data override
while True:
    print(
        "")  # instead of putting an empty line at the end of each possible outcome I put a empty line at the start of the program
    print("Welcome to the ICS3U0-D Kitchen Supply Store!(Development mode)")
    command = input("What would you like to do?  H or h to list all the commands.")
    error = ""  # make sure error is cleared
    if command == "N" or command == "n":
        print("You have chosen to add a new item")
        SID = input("Please enter a new ID")
        count = 0;
        for i in range(0, len(ids)):
            if SID == ids[i]:
                count += 1 #if any ids match increase count by 1
        if count > 0: #there is any matching ids
            print("This ID is already in use please enter a new ID")
        elif SID.isalpha():
            Nstock = input("Please enter how much stock we have as an integer")
            if Nstock.isnumeric():
                Nprices = input("Please enter the price for each item without a $ sign")
                if len(Nprices) <= 3:
                    print("Error: You must have a .00 to indicate cents")
                elif Nprices[len(Nprices) - 3] == ".":
                    count = 0;
                    for j in range(0, (len(Nprices) - 3)):
                        if Nprices[j].isnumeric():
                            count += 1
                    if count == (len(Nprices) - 3):
                        if Nprices[-1].isnumeric() and Nprices[-2].isnumeric():
                            Ndescs = input("Please enter a short description of the item")
                            prices.append(Nprices)
                            descs.append(Ndescs)
                            ids.append(SID)
                            stock.append(Nstock)
                        else:
                            print("Error: Numbers after . are not integers")
                    else:
                        print("Error: You must use numbers only")
                else:
                    print("Error: You must have a .00 to indicate cents")
            else:
                print("Invalid Input, only whole numbers allowed")
        else:
            print("Invalid Input, only letters allowed")
    elif command == "S" or command == "s":
        print("You have chosen to change the stock value")
        SID = input("Please enter stock ID")
        for i in range(0, len(ids)):
            if SID == ids[i]:
                error = ""
                NStock = input("Please enter new amount of stock")
                if NStock.isnumeric():
                    stock[i] = NStock
                    break
                else:
                    print("Error: You must use numbers only")
                    break
            else:
                error = "Failed"
        if error == "Failed":
            print("ID not found please try again or use command L or l to check inventory")
    elif command == "P" or command == "p":
        print("You have chosen to change the price")
        SID = input("Please enter stock ID")
        for i in range(0, len(ids)):
            if SID == ids[i]:
                error = ""
                Nprices = input("Please enter new price")
                if len(Nprices) <= 3:
                    print("Error: You must have a .00 to indicate cents")
                elif Nprices[len(Nprices) - 3] == ".":
                    count = 0;
                    for j in range(0, (len(Nprices) - 3)):
                        if Nprices[j].isnumeric():
                            count += 1
                    if count == (len(Nprices) - 3):
                        if Nprices[-1].isnumeric() and Nprices[-2].isnumeric():
                            prices[i] = Nprices
                            print("The new price is: ", prices[i])
                            break
                        else:
                            print("Error: Numbers after . are not integers")
                            break
                    else:
                        print("Error: You must use numbers only")
                        break
                else:
                    print("Error: You must have a .00 to indicate cents")
                    break
            else:
                error = "Failed"
        if error == "Failed":
            print("ID not found please try again or use command L or l to check inventory")
    elif command == "R" or command == "r":
        print("You have chosen to remove an item completely")
        SID = input("Please enter stock ID")
        for i in range(0, len(ids)):
            if SID == ids[i]:
                print("You have chosen to remove:", ids[i], "Desc:", descs[i], "QTY:", stock[i], "Cost:", prices[i])
                confirm = True
                while confirm:
                    YN = input("Please confirm Y for yes N for no")
                    if YN == "Y":
                        del ids[i]
                        del descs[i]
                        del prices[i]
                        del stock[i]
                        confirm = False
                        break
                    else:
                        break
            else:
                error = "Failed"
            if error == "Failed":
                print("ID not found please try again or use command L or l to check inventory")
    elif command == "H" or command == "h":
        print("Here are all of the commands")
        print("N or n -> Add a new item to our store.")
        print("S or s -> Change the stock value for an item.")
        print("P or p -> Change the price value for an item.")
        print("R or r -> Remove an item from the system.")
        print("H or h -> This is the prompt you are reading")
        print("L or l -> List all of the IDs their descriptions for the user")
        print("I or i -> All the info on a specific item.")
        print("C or c -> To enter customer mode")
        print("D or D -> To enter development mode")
        print("Q or q --> Quit the system.")
    elif command == "L" or command == "l":
        print("Here are all of the items so far:")
        for i in range(0, len(ids)):
            print("ID: ", ids[i], " Description: ", descs[i], " Stock: ", stock[i], " Price: ", prices[i])
    elif command == "I" or command == "i":
        print("You have chosen the advanced search option")
        advsearch = input("Please enter how you would like to search by (ID,Desc,Stock,Price): ")
        if advsearch == "ID":
            SID = input("Please enter the ID: ")
            for i in range(0, len(ids)):
                if SID == ids[i]:
                    print("ID: ", ids[i], " Description: ", descs[i], " Stock: ", stock[i], " Price: ", prices[i])
        elif advsearch == "Desc":
            Ndescs = input("Please enter the Description: (Case sensitive)")
            for i in range(0, len(ids)):
                if Ndescs == descs[i]:
                    print("ID: ", ids[i], " Description: ", descs[i], " Stock: ", stock[i], " Price: ", prices[i])
        elif advsearch == "Stock":
            Nstock = input("Please enter how much stock there is: ")
            for i in range(0, len(ids)):
                if Nstock == stock[i]:
                    print("ID: ", ids[i], " Description: ", descs[i], " Stock: ", stock[i], " Price: ", prices[i])
        elif advsearch == "Price":
            Nprices = input("Please enter the price of the item: ")
            for i in range(0, len(ids)):
                if Nprices == prices[i]:
                    print("ID: ", ids[i], " Description: ", descs[i], " Stock: ", stock[i], " Price: ", prices[i])
        else:
            print("Invalid option. (Case Sensitive)")
    elif command == "Q" or command == "q":
        break
    elif command == "C" or command == "c":
        print("Entering Customer mode")
        while True:
            print("Welcome to the ICS3U0-D Kitchen Supply Store!")
            print("Here are all the items for sale")
            for i in range(0,len(ids)):
                if stock > 0:
                    print("ID: ", ids[i], " Description: ", descs[i], " Stock: ", stock[i], " Price: ", prices[i])
                else:
                    print("ID: ", ids[i], " Description: ", descs[i], " Stock: SOLD OUT Price: ", prices[i])
    elif command == "d" or command == "D":
        print("You are already in Developer mode type H or h to see all commands")
    else:
        print("Invalid command please refer to Help page by typing H or h")

print("Goodbye!")
