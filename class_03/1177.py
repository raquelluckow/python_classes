t = int(input())
leng = 1000
n = [0]*leng
count = t

for i in range (leng):
    n[i] = i%t
    print('N[{}] = {}'.format(i,n[i]))