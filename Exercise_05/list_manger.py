import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('FILE_NAME1', type=str, help='Name of first file')
    parser.add_argument('FILE_NAME2', type=str, help='Name of second file')

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-i', '--intersection', action='store_true')
    group.add_argument('-u', '--union', action='store_true')
    group.add_argument('-d', '--difference', action='store_true')
    group.add_argument('-s', '--symmetricdiff', action='store_true')

    parser.add_argument('-o', '--output_file', type=str)

    args = parser.parse_args()
    list1 = set()
    with open(args.FILE_NAME1) as f:
        for line in f:
            list1.add(int(line.rstrip()))
    list2 = set()
    with open(args.FILE_NAME2) as f:
        for line in f:
            list2.add(int(line.rstrip()))

    if args.intersection:
        list_out = list1.intersection(list2)
    elif args.union:
        list_out = list1.union(list2)
    elif args.difference:
        list_out = list1.difference(list2)
    elif args.symmetricdiff:
        list_out = list1.symmetric_difference(list2)

    if args.output_file:
        with open(args.output_file, 'w') as f:
            for num in list_out:
                f.write(str(num) + '\n')

    else:
        print(list_out)
