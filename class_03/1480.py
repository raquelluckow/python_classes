n = int(input())
nums = [0]*n
out = [0]*n

for i in range(n):
    x = int(input())
    nums[i] = x
for i in range(n):
    out[i] = nums[i] + nums[i+1]
print(out)
#NÃO SEI RS