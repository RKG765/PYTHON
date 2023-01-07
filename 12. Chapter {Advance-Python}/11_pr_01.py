def readFile(filename):
    try:
        with open(filename,'r') as f:
            print(f.read())
    except FileNotFoundError:
        print(f'File {filename} Not Found...')

readFile('poems.txt')
readFile('tetx.txt')
readFile('sample.txt')