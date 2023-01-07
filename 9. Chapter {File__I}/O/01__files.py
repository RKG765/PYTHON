# reading files by their names
# a = open('sample.txt', 'r') # by dedfault the mode it will take is r
a = open('sample.txt', 'r')
# data = a.read()
data = a.read(6)  # it reads only first 6 chracters from the file 
print(data)
a.close()