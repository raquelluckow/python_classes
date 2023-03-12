import csv

with open("C://Users/ferre/Documents/python_classes/class_05/exercise/transaction.csv", "r") as file:
    #o bicho não reconheceu o arquivo ser dizer onde ele tá
    bank = csv.reader(file)
    count = 0
    list = []

    for line in bank:
        count += 1
        print(line[4])
        if count > 13:
            break

