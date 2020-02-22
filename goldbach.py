def isPrime(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True 

number = 10**5
for i in range(2, number):
    if isPrime(i):
        if isPrime(number - i):
            print(str(i) + " : " + str(number - i))
