n = int(input())
j = [0]*n
j = input().split(' ')
k = False

for i in range(n):
    if i+1 < n:
        if j[i+1] < j[i]:
            print(i+2)
            k = True
            break
if k == False:
    print(0)
