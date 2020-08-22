while True:
    n = int(input("enter first number "))
    m = int(input("enter second number "))
    if n>m or n==m:print("No prime numbers")
    else:
        for num in range(n, m + 1):
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                    print(num)