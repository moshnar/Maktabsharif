lloyd = {
    "field": "Computer",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}

alice = {
    "field": "Civil",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}

tyler = {
    "field": "Mechanics",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}


def Average(lst):  # return a average of a list items
    return sum(lst) / len(lst)


def get_data(key):  # return the values for a certain key
    return {'lloyd': lloyd.get(key), 'tyler': tyler.get(key), 'alice': alice.get(key)}


def get_averages(key='homework'):  # return average value of the certain key
    return {'lloyd': Average(lloyd.get(key)), 'tyler': Average(tyler.get(key)), 'alice': Average(alice.get(key))}


def get_class_average(key='homework',
                      names=None):  # return all average if no names specified or for a certain list of names
    if names == None:
        return {'all': f'The average value for {key} is {Average(get_averages(key).values())}'}
    else:

        return [Average(i.get(key)) for i in names]


name = [lloyd, alice]
print(get_class_average('homework', name))
print(get_averages('quizzes'))
# print(get_data('tests'))
