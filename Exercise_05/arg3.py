import argparse

parser = argparse.ArgumentParser()
parser.add_argument('NUM1', type=float, help='number 1 to operation')
parser.add_argument('NUM2', type=float, help='number 2 to operation')
parser.add_argument('-o', '--operation', type=str, help='OPERATION', choices=['add', '-', '/', '*'], required=True)

args = parser.parse_args()

operations = {
    'add': args.NUM1 + args.NUM2,
    '-': args.NUM1 - args.NUM2,
    '/': args.NUM1 / args.NUM2,
    '*': args.NUM1 * args.NUM2,
}

print(operations[args.operation])