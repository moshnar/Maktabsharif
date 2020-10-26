import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('name', type=str)
    parser.add_argument('lastname', type=str)
    parser.add_argument('--age', type=int)
    args = parser.parse_args()

    print(f'welcome{args.name} {args.lastname} with age {args.age}')
