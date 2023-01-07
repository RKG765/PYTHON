file = True
i = 1
with open('log.txt') as l:
    while file:

        file = l.readline()

        if 'python' in file.lower():
            print(file)
            print(f'it is present in line {i}')
        i+=1