import pandas as pd 

# 1 Column
data = [1,2,3,7,5]  # array, list, vector. 
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
#print(x)

# Series 
data = {'one': pd.Series([1,2,4], index=[4,6,8])}
x = pd.DataFrame(data)
#print(x)


# Head => 5 first lines 
data = [['Eduardo', 22, 123], ['Francico', 2, 456], ['Josefina', 99, 789], ['miau', 7, 1011]]
x = pd.DataFrame(data, columns=['Name', 'Age','NIF'])
#print(x)
#print(x[x["NIF"].isin([123,456])])

#x.iat[2,1]= 0
#x.at[2,"Age"] = 0
x.loc[x["Name"] == "Josefina", "Age"] = 0
##rint(x)




#print(x.head(2))
#print(x.tail(2))
#print(x.columns)
#print(x.iloc[1:2].describe())

#print(x['Name'].to_list())

cols = x.columns#
#print(x[0:3])
# LOC
#print(x.loc[1:2, cols[0]:cols[1]])
#print(x.loc[x['Age'] > 22])
#print(x.loc[:, ['Name', 'NIF']])
#print(x.loc[[0,2], ['Name', 'NIF']])
#print(x.loc[1])
#print(x.iloc[1])
#print(x.iloc[:, 0:2])


data = [["Marcela", 123456], ["Josefina", ], ["Raquel", 42], ["Juliane", ]]
x = pd.DataFrame(data, columns=["Name", "NIF"])

#x = x.dropna()
print(pd.isna(x))