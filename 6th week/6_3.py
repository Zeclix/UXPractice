def inputNum(a):
    cnt=0
    while cnt<10:
       temp = float(input("%d번째 값을 입력하세요:" %(cnt+1)))
       a.append(temp)
       cnt = cnt+1

def MAX(a):
    MAX = a[0]
    for i in a:
        if i>MAX:
            MAX = i
    print("최대값 : %.2f" % MAX)

def MIN(a):
    MIN = a[0]
    for i in a:
        if i<MIN:
            MIN = i
    print("최소값 : %.2f" % a[0])


def AVG(a):
    SUM=0
    for i in a:
        SUM = SUM + i
    average = SUM/len(a)
    print("평균 : %.2f" % average)


a=[]
inputNum(a)
MAX(a)
MIN(a)
AVG(a)








