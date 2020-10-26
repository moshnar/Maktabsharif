import time

pills_count = 10

m = time.mktime((2020, 10, 20, 6, 0, 0, 0, 0, -1))

s = time.localtime(m)

print(s)

hour = 8 * 3600

while pills_count !=0:
    m+= hour
    pills_count -= 1
    print(time.localtime(m)[2:4],pills_count)
