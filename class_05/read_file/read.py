# rb, wb: binary versions of w and r. 
# w: write => if the file doesn't exist it creates it 
# r: read  => if the file doesn't exist it returns an error  
# a: append => if the file doesn't exit it creates 
# w+: write and read  => if the file doesn't exist it creates
# r+: write and read  => if the file doesn't exist it returns an error  
# a+: append and read => if the file doesn't exit it creates 

# R =================================== 
f = open("./doguinho.txt", "r")
lines = f.readlines()   # add each line to an array 
lines = f.read()        # read as a string

#line_1 = f.readline(2)    # read from position 0 to 2. 
#line_1 = f.readline(4)    # read from position 2 to 4. Just the first line. 

f.close() 
# W =================================== 
#f = open("./doguinho.txt", "w")
#f.write("\nDocinho")
#f.writelines(["Albert\n", "Einstein\n", "Batman\n", "Eduardo"])
#f.close() 

# A =================================== 
""" 
f = open("./doguinho.txt", "a") 
f.write("\nDocinho")
f.close()
"""
#print(line)


