def isPrime(n):
    # checking all numbers between 2 and square root + 1 of the n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


for i in range(2, 100):
    if isPrime(i):
        print(f" {i}", end='\t')
