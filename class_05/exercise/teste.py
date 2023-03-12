
def print_line(line, num_elements): 
    line_list = line.split(";")
    s = "{:<20}"*num_elements
    s = s.format(*line_list)
    print(s)

bank = open("C://Users/ferre/Documents/python_classes/class_05/exercise/transaction.csv", "r") 

lines = bank.readlines() 

header = lines[0].split(";")

header_size = len(header)

count = 0

###QUESTION 0 AND 1
for j in range(header_size):
    if header[j] == 'operation':
        for i in lines:
            count += 1
            line_1 = i.split(';')[j]
            #line_2 = count.split(';')[j]
            #if line_2 != line_1:
                #print(line_2)
        #print(f"How many transactions were made? {count}")
    #print(i.split(';')[0])
    #if header[i] == 'operation':
        #for i in range(1,20):
            #line_1 = lines[i].split(';')
            #line_2 = lines[i+1].split(';')
            #if line_2[4] != line_1[4]:
                #print(line_1[4] + ', ' + line_2[4])
#for i in lines: 
    #print_line(i[:-1], 3) #pq não posso escrever só i?

###QUESTION 2: ACCOUNT THAT MOVED MORE MONEY
for j in range(header_size):
    if header[j] == 'account_id':
        for i in lines:
            account = i.split(';')[j]
            
    


