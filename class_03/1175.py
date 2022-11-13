leng = 20
n = [0]*leng

for i in range(leng):
    n[i] = int(input())

#f = []
#for i in range(leng-1,-1,-1):
    #f.append(n[i])
n.reverse()
for i in range(leng):
   
    print('N[{}] = {}'.format(i,n[i]))
