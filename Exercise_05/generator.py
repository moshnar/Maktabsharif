import csv


def csv_reader(filename):
    with open(filename, 'r') as csv1:
        reader = csv.reader(csv1)
        for row in reader:
            yield row


for line in csv_reader('addresses.csv'):
    print(line)
