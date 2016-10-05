with open("newfile.txt", 'r') as f:
    while 1:
        line = f.readline()
        if not line: break
        print(line)