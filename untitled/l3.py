
def TowerOfHanoi(n , from_rod, to_rod, aux_rod):
    if n == 1:
        print "Move disk 1 from rod" ,from_rod ,"to rod" ,to_rod
        return
    TowerOfHanoi( n -1, from_rod, aux_rod, to_rod)
    print "Move disk" ,n ,"from rod" ,from_rod ,"to rod" ,to_rod
    TowerOfHanoi( n -1, aux_rod, to_rod, from_rod)
n = 4
TowerOfHanoi(n, \'A\', \'C\', \'B\')




import sys
def max(a, b):
    return a if (a > b) else b
def cutRod(price, n):
    if (n <= 0):
        return 0
    max_val = -sys.maxsize - 1
    for i in range(0, n):
        max_val = max(max_val, price[i] +
                      cutRod(price, n - i - 1))
    return max_val
arr = [1, 5, 8, 9, 10, 17, 17, 20]
size = len(arr)
print("Maximum Obtainable Value is", cutRod(arr, size))


def collatz(n):
    while n > 1:
        print(n, end=' ')
        if (n % 2):
            n = n // 2
    print(1, end=' ')

n - int(input('Enter n:  '))
print('Sequence: ', end= '')
collatz(n)



def isPrime(n, i=2):
    if (n <= 2):
        return True if (n == 2) else False
    if n % i == 0:
        return False
    if i * i > n:
        return true
    return isPrime(n, i + 1)
if (isPrime(n)):
    print("yes")
else:
    print("no")


def sum(n):
    i = 1
    s = 0.0
    for I in range(1, n+ 1):
        s = s + 1 / i;
        return s;
    n = 5
    print("sum is", round(sum(n), 6))
    def sum_ of_digit(n):
        if n == 0:
            return 0
        return (n% 10 + sum_of_digit(int(n / 10)))
    num = 12345
    result = sum_of digit(num)
print(num, result)


def knapSack(W , weight , value , n):
    if n == 0 or W == 0 :
        return 0

    if (weight[n-1] > W):
        return knapSack(W , weight , value , n-1)
    else:
        return max(value[n-1] + knapSack(W-weight[n-1] , weight , value , n-1), knapSack(W , weight , value , n-1))

    value = [100, 50, 150]
    weight = [20, 10, 30]
    W = 50
    n = len(val)
print (“Maximum capacity : “,knapSack(W , weight , value , n) )



for i in range(input()):
    a = input()
    sum1=0
    for j in list(a):
        sum1+=ord(j)
    print sum1-((96)*(len(a)))


def main(t, s):
    i = 0
    while i < t:
        strr = s[i]
        count = 0
        for j in strr:
            count = count + ord(j) - 96
        print(count)
        i = i + 1


t = int(input())
s = []
while len(s) < t:
    s.append(input())
main(t, s)


