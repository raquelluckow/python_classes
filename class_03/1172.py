#x = []
#for i in range(10):
#    x.append(0)
x = [0]*10

for i in range(len(x)):
    x[i] = int(input())
    if x[i] <= 0:
        x[i] = 1
    print('X[{}] = {}'.format(i,x[i]))
print(x)
