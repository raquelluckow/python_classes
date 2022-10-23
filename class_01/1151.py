n = int(input())
i = 0
j = 1

for a in range(n):
    if a == n-1:
        print(i)
    else:
        #print(f'{i} ')
        print(i, end= " ")
    k = i + j
    i = j
    j = k

