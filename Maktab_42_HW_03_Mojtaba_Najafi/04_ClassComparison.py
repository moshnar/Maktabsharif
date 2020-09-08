def print_all(list1, list2):#return all items in both lists without repetetive item
    return set(list1).union(set(list2))


def left_list(list1, list2):#return the items are in the first but not in the second list
    return set(list1).difference(set(list2))


def right_list(list1, list2):#return the items are in the second but not in the first list
    return set(list2).difference(set(list1))


def intersect_list(list1, list2):#return mutual items
    return set(list1).intersection(set(list2))


def Char_counter(list1, list2):#return size of the mutual list's items
    return [len(i) for i in list(intersect_list(list1,list2))]



def long_name(list1, list2):#return the item in the both list with the lenght longer than 10
    return [i for i in print_all(list1,list2) if len(i) > 10]


def sort_alpha(list1, list2):#return a sorted list with the items which present in the first list but not in the second
   return sorted(left_list(list1, list2))


list1 = 'Ali','Mohammad','Javad','Barbod','Saeed','Taher'#example list
list2 = 'Ali','Zahra','Sadaf','Kaveh','Saeed','Kamran','SasyMankan1'#example list 2



print(sort_alpha(list1,list2))
print(left_list(list1,list2))
print(print_all(list1,list2))
print(right_list(list1,list2))
print(intersect_list(list1,list2))
print(Char_counter(list1,list2))
print(sort_alpha(list1,list2))