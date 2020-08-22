from math import sqrt

def isPrime(n):
    if n == 1:
        return 0
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return 0
    return 1


t = int(input())
for i in range(t):
    n = int(input())
    check = isPrime(n)
    print('Prime' if check == 1 else 'Not prime')
