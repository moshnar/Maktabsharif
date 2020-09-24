def stats(str):
    with open(str) as file:
        longest_line = max(file, key=len)
    print(f'longest line : {len(longest_line)}')
    print(longest_line)

stats('sample.txt')