def sumList(list):
    sum = 0
    for i in list:
        sum += list[i]
    return sum


lis = [1, 2, 3, 4]

print(sumList(lis))
print(sum(lis))
