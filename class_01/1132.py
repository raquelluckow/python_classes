a = int(input())
b = int(input())
sum = 0

if a < b:
    n_1 = a
    n_2 = b
else:
    n_1 = b
    n_2 = a

#while n_1 <= n_2:
for i in range(n_1,n_2+1,1):
    if n_1%13 != 0:
        sum += n_1
    n_1 += 1
print(sum)
