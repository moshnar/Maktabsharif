def print_all(list1, list2):
    return set(list1).union(set(list2))


def left_list(list1, list2):
    return set(list1).difference(set(list2))


def right_list(list1, list2):
    return set(list2).difference(set(list1))


def intersect_list(list1, list2):
    return set(list1).intersection(set(list2))


def Char_counter(list1, list2):
    return [len(i) for i in list(intersect_list(list1,list2))]



def long_name(list1, list2):
    return [i for i in print_all(list1,list2) if len(i) > 10]


def sort_alpha(list1, list2):
   return sorted(left_list(list1, list2))


list1 = 'Ali','Mohammad','Javad','Barbod','Saeed','Taher'
list2 = 'Ali','Zahra','Sadaf','Kaveh','Saeed','Kamran','SasyMankan1'



print(sort_alpha(list1,list2))
print(left_list(list1,list2))
print(print_all(list1,list2))
print(right_list(list1,list2))
print(intersect_list(list1,list2))
print(Char_counter(list1,list2))
print(sort_alpha(list1,list2))