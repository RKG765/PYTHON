words = ['donkey','kaddu','kuta','kamina','kutta']


with open('sample.txt') as i:
    a = i.read()
for word in words:
    a = a.replace(word,'##@#@$')
    with open('sample.txt','w') as i:
        i.write(a)