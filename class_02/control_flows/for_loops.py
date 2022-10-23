# for ... in ...
# The basic for loop
# range(<inicio> = 0, fim, <intervalo> = 1)
for number in range(3):
    print(number)
    # i = i+1

i = 0 
while i < 3: 
    print(i)
    i += 1 
# range(3) == range(0,3)


# Interval [2,10)
# range(<inicio> = 0, fim, <intervalo> = 1)
for i in range(2,10):
    print(i)

# Interval of 2 (only even) 
for i in range(2,10,2):
    print(i)
    # i = i+2

# Decreasing sequence
for i in range(10, -1, -1):
    # i = 10
    # i = i - 1
    print(i)

# With vectors (iterate over the vector)
n = [1,10,32,40]
for i in n:
    print(i)


# With string (iterate over strings)
name = "raquel"
for i in name: 
    print(i)

# (1,1) => (10,1)  
for i in range(1,11):
    # i = 1; j = [1,10]
    for j in range(1,11):
        print("({},{})".format(i,j))


# Transforming things into lists.
name = "raquel"
name_list = list(name)
ran = list(range(9))
