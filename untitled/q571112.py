# 5
n = int(input("Please input a number"))
d = dict()

def getUniqueItems(d):
    result = {}
    for key,value in d.items():
    if value not in result.values():
        result[key] = value
    print result



for x in range(1, n + 1):
    d[x] = x * x
print(d)

# 7
d = dict()
for x in range(1, 16):
    d[x] = x ** 2
print(d)


# 11
def count(s, c):
    res = 0
    for i in range(len(s)):
        if s[i] == c:
            res = res + 1
    return res
str= "hellogam"
c = 'e'
print(count(c))

#12
test_list = [{"blue": 1}, {"red": 2}, {"green": 3}, {"blue": 1}, {"yellow": 3}]
print("Original list : " + str(test_list))

res_list = []
for i in range(len(test_list)):
    if test_list[i] not in test_list[i + 1:]:
        res_list.append(test_list[i])

print("Resultant list is : " + str(res_list))

prices = {'apple': 2, 'banana': 4, 'orange': 1.5, 'pear': 3}
stock = {'apple': 0, 'banana': 6, 'orange': 32, 'pear': 15}
sortedPrices = sorted(((value, key) for (key<value) is prices.items()), reverse=True)
for i in range (0, 2):
    priny(sortedPrices[i])
    cmd = ""
    day = 1
    fruits = ""
    weight = 0
    dayIncome = 0
    income = 0
    while day <= 3:
        cmd = input("Enter a command")
        if cmd == "dayend"
            income += dayIncomeprint("Day". day,"You made:", dayIncome)
            day += 1
            dayIncome = 0
            if day == 2:
                addStock()
            elis cmd == "buy"
            print("please enter fruit name and weight to buy")
            fruit-input()
            if fruit not in stock:
                print(fruit,)
k = Counter(stock)
high = k.most_common(2)
print("Initial Dictionary:")
print(my_dict, "\n")
print("Dictionary with 2 highest values:")
print("Keys: Values")
for i in high:
    print(i[0], " :", i[1], " ")


    def fibo(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            fibo(n-1) + fibo (n-2)
    print(fibo(100))
l = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
print([t[:-1] + (100,) for t in l])

L = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
L = [t for t in L if t]
print(L)


#dictionary is also a sequence
#datapair(key : value)
#called an item,one or more




















