import zipfile
import gzip
import os


# with open('test.txt','w') as f:
#     for i in range(100):
#         f.write('i')
with open('test.txt','r') as f:
    s = f.read()


# for i in s:
#     print(i)
# print(os.path.getsize('test.txt'))
# print(os.system('ls -lar'))

t = gzip.open('test.txt')
gzip.compress(t)