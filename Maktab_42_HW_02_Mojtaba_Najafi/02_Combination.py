def Combination(n,k):
    if n==0 or n<0: return
    elif k==0 or n==k: return 1
    else:
        return Combination(n-1,k-1)+Combination(n-1,k)



n = int(input("Please enter n : "))
k = int(input("Please enter k : "))
print(Combination(n,k))

