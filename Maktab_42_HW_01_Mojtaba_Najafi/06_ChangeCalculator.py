M = int(input("Enter the sum "))
first = M // 1000
a = M % 1000
second = a // 500
b = a % 500
third = b // 200
c = b % 200
forth = c // 100

print(str(first) + " 1000 bill " + str(second) + " 500 bill " + str(third) + " 200 bill " + str(forth) + " 100 bill ")
