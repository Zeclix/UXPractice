with open("newfile.txt", 'r') as f:
    lines = f.readlines()
    for line in lines:
        print(line)
        