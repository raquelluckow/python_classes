#import time 
# Curiosidade :B
#while True: 
#    time.sleep(1)
#    print("sleeped.")


# while <condition>: 
#   ...
'''
n = 10 
while n > 0: 
    print("{}".format(n))
    n -= 1
'''

'''
n = 10
while n > 0: 
    print("{}".format(n))
    n -= 1
    if n == 5:
        break
''' 

while True:
    name = input()
    if name == 'raquel':
        continue
    if name == 'bernardo':
        print("Cai fora")
        break
    print("Hello, {} ".format(name))



