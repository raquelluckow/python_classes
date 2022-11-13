# This is a dictionary 
d = {"raquel": "luckow", "juliane": "marubayashi", "bernardo": "vadio"}
# {key: value}
# Keys are unique 

# ACCESS ==========================
# How to get a value of a key 
# print(d["raquel"])      # Should return "luckow"
# print(d["bernardo"])  # Should give an error 

# ADD THINGS ======================
d["lalau"] = "lolow"

#print(d) 
#  {"raquel": "luckow", "juliane": "marubayashi", "bernardo": "vadio", "lalau": "lolow"}

# CHANGE THINGS ===================
d["raquel"] = "lucky"

# print(d)
#  {"raquel": "lucky", "juliane": "marubayashi", "bernardo": "vadio", "lalau": "lolow"}

# DELETE ==========================
del d["bernardo"] 

#print(d)
#  {"raquel": "lucky", "juliane": "marubayashi","lalau": "lolow"}

# REAL CASE =============================
# O(1) => dictionaries doesn't need for loop, we can access the direct position. 
purchase_list = {"computer": 100, "banana": 100}
successor_dict = {101: 102, 102: 103} 

#print(purchase_list["computer"])

# What is an array 
# O(n) => we need to create a loop and verify if the "computer" is there. 
elements = ["computer", "banana"]
values = [100, 102] 

# FOR LOOPS  ======================= 
keys = d.keys()
# ["raquel", "juliane", "lalau"]
print(list(keys))

values = d.values()
print(list(values)) 

for i in keys:
    print(d[i])     # print values 

for i in values: 
    print(i)        # print values 




