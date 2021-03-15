# https://www.acmicpc.net/problem/2475

a, b, c, d, e = input().split(' ')

a = eval(a)
b = eval(b)
c = eval(c)
d = eval(d)
e = eval(e)

a = a*a
b = b*b
c = c*c
d = d*d
e = e*e

print((a+b+c+d+e)%10)