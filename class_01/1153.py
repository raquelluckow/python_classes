n = int(input())
fac = n
while n-1 > 1:
    fac *= (n-1)
    n -= 1
print(fac)