def fibonacci(a):
    f = [0,1]
    for i in range(a):
        f.append(f[a-2]+f[a-1])
        