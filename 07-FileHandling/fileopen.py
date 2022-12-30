file = open('countries.txt','r') 
file_content = file.read() 
for count, line in file:
    count =+ 1
    print("Line{}: {}".format(count, line.strip())) 
file.close() 
