a = open('sample.txt')
# it reads only one line 
data = a.readline() 
print(data)
# reads second line  
data = a.readline() 
print(data)
# reads third line
data = a.readline() 
print(data)
# reads fourth line
data = a.readline() 
print(data)
a.close()