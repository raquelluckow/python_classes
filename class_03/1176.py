test = int(input())
x1 = 0
x2 = 1
f = [0,1]

for i in range(test+1):
    n = int(input())
    print('Fib({}) = {}'.format(n,f[n]))
    x3 = x1 + x2
    x1 = x2
    x2 = x3
    f.append(x3)
    #print('Fib({}) = {}'.format(n,f[n]))
for i in range(test+1):
    