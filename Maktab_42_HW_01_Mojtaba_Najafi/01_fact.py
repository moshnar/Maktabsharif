import math
n =10
print("using math "+str(math.factorial(n)))

def factorial(f):
    if f==1: return f
    else:return f * factorial(f-1)


print("recursive factorial is: " +str(factorial(10)))

def factorial2(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

print("using loop "+str(factorial2(10)))
