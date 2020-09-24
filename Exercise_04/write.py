import string
def remove_lowercase(input_,out):
    input_file = open(input_)
    out_file = open(out, 'w')
    for line in input_file:
        if not line[0].islower():
            out_file.write(line)
    input_file.close()
    out_file.close()
    return out_file


remove_lowercase('sample.txt','out.txt')


