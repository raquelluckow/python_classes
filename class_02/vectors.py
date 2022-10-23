a = [10,24,33] 
#print(a[0])     # 10
#print(a[-1])    # 33
#print(a[2])     # 33


""" 
LIST SLICE 
"""

a = [1,2,3,4,5,6]
sliced_a = a[2:] # [3,4,5,6]
sliced_b = a[2:5] # [3,4,5]

"""
LIST FUNCTIONS 
"""

# LEN  ======
list_size = len(a)   # 6
sliced_c = a[2:list_size]    # [3,4,5,6]

# DEL  =====
del a[1]    
#print(a) # [1,3,4,5,6]

raquel_esta = "raquel" in ["raquel", "bernardo", "lalau"]
#print(raquel_esta)     # True 

one_is_in = 1 in [3,4,5]
#print(one_is_in)        # False 

# APPEND =====
miau = ["raquel", "bernardo", "lalau"]
miau.append("juliane") # ["raquel", "bernardo", "lalau", "juliane"]

# SUM OF LISTS =====
miau = [miau[0]] + ["juliane"] + miau[1:] # ['raquel', 'juliane', 'bernardo', 'lalau', 'juliane']
#print(miau)

# SORT ==== 
# print(miau.sort()) the sort returns nothing, but changes the miau
c = sorted(miau)    # the c is sorted but not miau.
#print(c)
#print(miau)

# SUM ====== 
sum([1,2,3,4])  # 10 


"""
FOR LOOPS WITH LISTS 
"""

b = [2,6,10]
#for i in b: 
#    print(i)

c = ["raquel", "bernardo", "lalau"]
#for i in c:
#    print(i)

d = ["raquel", "bernardo", "lalau"]
e = list(enumerate(d))  # [(0, 'raquel'), (1, 'bernardo'), (2, 'lalau')] 
#for i, name in enumerate(d):
#    print(i)
#    print(name)