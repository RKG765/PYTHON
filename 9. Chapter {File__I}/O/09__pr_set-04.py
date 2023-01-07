with open('sample.txt') as i:
    a = i.read()

a = a.replace('donkey','##@#@$')

with open('sample.txt','w') as i:
    i.write(a)