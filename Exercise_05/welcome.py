#!/usr/bin/env python3
import sys

if len(sys.argv) < 3:
    print('invalid')
elif type(eval(sys.argv[3])) == int:
    print(f'welcome,{sys.argv[1]},{sys.argv[2]},with age : {sys.argv[3]}')
else:
    print('age must be an integer', type(eval(sys.argv[3])))
