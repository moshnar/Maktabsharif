import re

s = 'mamd mammad mammadd'
pattern = re.match(r'[a-z A-Z]*', s)

print(pattern.group())
