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
def Average(lst):
    return sum(lst) / len(lst)

def get_data(key):
    return {'lloyd': lloyd.get(key), 'tyler': tyler.get(key), 'alice': alice.get(key)}


def get_avarages(key='homwork'):
    return {'lloyd': Average(lloyd.get(key)), 'tyler': Average(tyler.get(key)), 'alice': Average(alice.get(key))}


def get_class_avarage(key='homwork', names=None):
    return

print(get_avarages('homework'))