import math

def is_triangle(a, b, c):
    if c < a + b:
        print('YES')
    else:
        print('NO')

a = float(input('Side a: '))
print('Value of a:',a)


b = float(input('Side b: '))
print('Value of b:',b)


c = float(input('Side c: '))
print('Value of c:',c)

is_triangle(a,b,c)