import argparse

parser = argparse.ArgumentParser()
parser.add_argument("NAME_FILE", type=str, help='our file name')
parser.add_argument('-n', help='our optional mode', action='store_true')

args = parser.parse_args()

with open(args.NAME_FILE) as f:
    if args.n:
        lines = f.readlines()
        print(len(lines))
    else:
        for line in f:
            print(line)
