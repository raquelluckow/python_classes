def print_line(line, num_elements): 
    line_list = line.split(",")
    s = "{:<20}"*num_elements
    s = s.format(*line_list)
    print(s)

f = open("./tweets.csv", "r") 

lines = f.readlines(); 
header = lines[0].split(",")
header_size = len(header)

for i in lines: 
    print_line(i[:-1], header_size)

