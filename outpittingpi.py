import math

sin = math.sin
pi  = math.pi

n = int(input('How many steps?'))

for i in range(n):
    x = float(i) / 30.0 * 2 * pi
    print (sin(x))