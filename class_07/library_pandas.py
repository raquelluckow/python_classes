import pandas as pd 

# 1 Column
data = [1,2,3,7,5]
x = pd.DataFrame(data)
#print(x)

# 2 Columns
data = [['Eduardo', 22], ['Francico', 25], ['Josefina', 99]]
x = pd.DataFrame(data, columns=['Name', 'Age'])
#print(x)

# Dictionarie, all the columns need to have the same number of elements.
data = {'one': [1,2,3,4], 'two': [1,2,4,7]}
x = pd.DataFrame(data)
#print(x)
#print(x['one']) # Print just one column
del x['one']
print(x)

# Series 
data = {'one': pd.Series([1,2,3], index=['a','b','c'])}
x = pd.DataFrame(data)
#print(x)


