MIN = 0
SUM = 0
cnt = 0
a=[]
while cnt<10:
   temp = float(input("%d번째 값을 입력하세요:" %(cnt+1)))
   a.append(temp)
   cnt = cnt+1

MAX = a[0]
for i in a:
    if i>MAX:
        MAX = i
print("최대값 : %f" % MAX)

MIN = a[0]
for i in a:
    if i<MIN:
        MIN = i
print("최소값 : %f" % a[0])
for i in a:
    SUM = SUM + i
print("합 : %f" % SUM)
print("평균 : %f" % (SUM/len(a)))

