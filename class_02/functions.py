import random 

a = "raquel quer bolo"
b = ["raquel", "quer", "bolo"]
c = a.split(" ")
#print(c)

d = "money&money&money"
e = d.split("&")
#print(e) 

# FUNCTION DEFINITION =======================================================
def myFunction(name):
    print(name)
    print("Sai daqui {}".format(name)) 


#myFunction("lala")
#myFunction("Bernardo")

# ISOLATE VARIABLES IN FUNCTIONS ============================================
num1 = 3
def myOperation(num2): 
    num1 = 1            # The function isolates its variables.
    return num1 + num2 * 2 

new_number = myOperation(2)
#print(new_number)
#print(num1)

# GLOBAL SCOPE to access global variables  ================================== 
def myOperation2(num2): 
    global num1
    return num1 + num2 * 2 

#print(myOperation2(2))  # Must return 7

# RANDOM ====================================================================
#r = random.randint(1,9)
#print(r)

# LAMBDAS ===================================================================
myOperation3 = lambda num1, num2: num1 + num2
print(myOperation3(1,2))

# MAP =======================================================================
# input = 1 2 3 4 
x = list(map(int, input().split(' ')))     # ["1", "2", "3", "4"]

def myOperation4(x1):
    return x1*2 

# input = 1 2 3 4 
x = list(map(myOperation4, input().split(" "))) # ['11', '22', '33', '44']