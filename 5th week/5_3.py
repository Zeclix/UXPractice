#FILe I/O 예제
try:
    with open("./newfile.txt", 'w') as f:
        data = "Hello File I/O!"
        f.write(data)

    with open("./newfile.txt", 'w') as f:
        for i in range(1, 11):
            data = "%d line \n" % i
            f.write(data)
except Exception as e:
    print(str(e))