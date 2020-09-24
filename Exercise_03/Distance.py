#in1 = list(input("Please eneter a list of numbers :  ").split(',')),key=lambda x : abs(l[i]-l[j])
l = [0,10,25,13.5,40,5]

def func(x):
    return abs(x[0]-x[1])


for i in range(len(l)):
    for j in range(1 , len(l)-1):
        dict= {}
        dict.setdefault(j , []).append(l[j])

print(dict.items())




