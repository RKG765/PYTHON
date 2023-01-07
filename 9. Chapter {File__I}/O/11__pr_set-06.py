with open('log.txt') as l:
    file = l.read()

if 'python' in file.lower():
    print('it is present')
else:
    print('sorry,it is not')
