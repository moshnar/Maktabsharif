import random


def random_walk(n):
    x, y = 0, 0
    for i in range(n):
        xd, yd = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        x += xd
        y += yd
    return (x, y)


number_of_walk = 25000

for walk_length in range(1, 31):
    no_transpot = 0
    for i in range(number_of_walk):
        (x, y) = random_walk(walk_length)

        distance = abs(x) + abs(y)
        if distance <= 5:
            no_transpot += 1
        no_transport_precentage = float(no_transpot) / number_of_walk

        print('walk size ', walk_length, '% of tranport', 100 * no_transport_precentage)
