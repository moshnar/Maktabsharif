''' two list are equal only when length and items on them are equal'''
import functools
from statistics import mean


@functools.total_ordering
class Mylist(list):

    def __lt__(self, other):
        return mean(self) < mean(other)



    def __eq__(self, other):
        return mean(self) == mean(other)



class Mylist2(list):
    def __gt__(self, other):
        return mean(self) < mean(other)

    def __eq__(self, other):
        return mean(self) == mean(other)


li = [[0, 100, 100], [1, 2], [2.1, 5.4, 3], [1, 4], [100, 100, 100], [90,90, 90, 90, 90]]

li = [Mylist(item) for item in li]
print(sorted(li))

l1 = Mylist([0, 100, 100])
l2 = Mylist([101, 0])
l3 = Mylist([100, 0, 100])
print(f' l1 : {mean(l1)}, l2 : {mean(l2)}, l3 : {mean(l3)}')
#print(f' l1 : {sum(l1)/len(l1)}, l2 : {sum(l2)/len(l2)}, l3 : {sum(l3)/len(l3)}')
print(l1 < l2)
print(l1 > l2)
print(l1 <= l2)
print(l1 >= l2)
print(l1 == l3)
print(l1 != l3)
print(sorted(Mylist2(x) for x in [l1, l2, l3]))
