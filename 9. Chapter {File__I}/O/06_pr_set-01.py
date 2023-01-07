a = open('poems.txt')
b = a.read()
if 'twinkle' in b:
    print('It is present')
else:
    print('Not present')
b = a.close()