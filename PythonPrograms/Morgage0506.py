balance = float(input("Enter the balance without a $ sign"))
payment = float(input("Enter the yearly payment without a $ sign"))
interest = float(input("Enter the interest rate  without a % sign"))
interest /= 100
year = 1
interestcost=0
totalinterest=0
while(balance > payment):
    print("At the end of the year ", year)
    year += 1
    balance = balance - payment
    print("Your payments totaled", payment)
    print("Balance after payment before interest", balance)
    interestcost = interest * balance
    totalinterest += interestcost
    print("Interest is ", interestcost)
    balance = balance + (interest * balance)
    print("Remaining balance is", balance)
    print("")
print("You've paid", totalinterest ,"in interest")
print("Goodbye!")
