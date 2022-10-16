n = input().split(" ") 
# n = ["7", "14", "106"] 
n_1 = int(n[0]) # 7
n_2 = int(n[1]) # 14
n_3 = int(n[2]) # 106 

if n_1 > n_2 and n_1 > n_3: 
    print("{} eh o maior".format(n_1)) 
elif n_2 > n_1 and n_2 > n_3:
    print("{} eh o maior".format(n_2)) 
else:
    print("{} eh o maior".format(n_3)) 

