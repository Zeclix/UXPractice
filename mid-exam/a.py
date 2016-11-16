'''
개인과제1 파일 입출력 및 분석
개인과제 1 ; 주어진 파일을 기반으로 다음의 출력을 도출하고 그래프로 그려라.
           Input Average                      Output Average
1          20.66666667 5                      5
2          15.66666667 12.5                12.5
...
파일 "A"를 읽어,
(完) 1. Input Average의 총 합과, Input Average의 평균을 구하라
(完) 2.  Output Average의 총 합과, Output Average의 평균을 구하라
(完) 3. 만약 Input Average의 값이 Output Average의 값보다 작으면 이는 데이터 손실이 발생한 경우이므로, 위 평균을 구할때 이 값을 제외한 나머지 값으로만 평균을 구해야만 한다.
(完) 4. 전체 input에 대한 output의 수신률과 위치(번호)을 구하라.
(完) 5. 가장 input이 많은(큰) 값과 가장 input이 적은 값과 위치(번호)을 구하라
(完) 6. 가장 output이 많은(큰) 값과 가장 output이 적은 값과 위치(번호)을 구하라
(完) 7. 수신률이 가장 좋은 값과 위치(번호)과 가장 나쁜 값과 위치(번호)을 구하라.
(完) 8. 최근 10개의 input average 가장 많은 구간(번호)을 구하라
(完) 9. 최근 10개의 output average가 가장 많은 구간(번호)을 구하라
10. 위에 대한 모든 정답을 "A_Result.txt" 파일에 저장하고 "A_Result"를 기반으로 9개의 그래프(엑셀)로 그려라.

'''

firstFlag=1
receptionRateDict={}
inputDict={}
outputDict={}
filterList=[]

with open('A.txt', 'r') as f:
    for line in f:
        tempList = line.split()
        #print(tempList[0]) #for debug

        if(tempList[0]=='Input'):
            continue
        if(float(tempList[1])<float(tempList[2])):
            #print("line:%d"%int(tempList[0])) #for debug
            continue
        filterList.append([tempList[0], tempList[1], tempList[2]])

        if(float(tempList[2])==0):
            receptionRate = 0

        else:
            receptionRate = float(tempList[2])/float(tempList[1])

        #print("#%d, reception rate : %f"%(int(tempList[0]), receptionRate)) #for debug
        receptionRateDict[int(tempList[0])] = receptionRate

        if(firstFlag==1):
            sumInputAverage=0
            cntElements=0
            sumOutputAverage=0
            maxInput=float(tempList[1])
            maxInputPosition=float(tempList[0])
            minInput=float(tempList[1])
            minInputPosition=float(tempList[0])
            maxOutput=float(tempList[2])
            maxOutputPosition=float(tempList[0])
            minOutput=float(tempList[2])
            minOutputPosition=float(tempList[0])
            bestReceptionRate=receptionRate
            bestReceptionRatePosition=float(tempList[0])
            worstReceptionRate=receptionRate
            worstReceptionRatePosition=float(tempList[0])
            #print(receptionRate) #for debug
            #print("Worst Reception Rate : %f, Worst Reception Rate Position : %d"%(worstReceptionRate, worstReceptionRatePosition)) # for debug
            firstFlag=0
            #print("%d"%firstFlag) #for debug

        cntElements=cntElements+1
        sumInputAverage = sumInputAverage+float(tempList[1])
        sumOutputAverage = sumOutputAverage + float(tempList[2])
        inputDict[int(tempList[0])] = float(tempList[1])
        outputDict[int(tempList[0])] = float(tempList[2])
        if maxInput<float(tempList[1]):
            maxInput = float(tempList[1])
            maxInputPosition = float(tempList[0])
        if minInput>float(tempList[1]):
            minInput = float(tempList[1])
            minInputPosition = float(tempList[0])
        if maxOutput<float(tempList[2]):
            maxOutput = float(tempList[2])
            maxOutputPosition = float(tempList[0])
        if minOutput>float(tempList[2]):
            minOutput = float(tempList[2])
            minOutputPosition = float(tempList[0])
        if bestReceptionRate<receptionRate:
            bestReceptionRate=receptionRate
            bestReceptionRatePosition = float(tempList[0])
        if worstReceptionRate>receptionRate:
            #print("merong") # for debug
            worstReceptionRate=receptionRate
            worstReceptionRatePosition = float(tempList[0])
            #print("Worst Reception Rate : %f, Worst Reception Rate Position : %d"%(worstReceptionRate, worstReceptionRatePosition)) #for debug


    #print(cntElements) #for debug
    print("Filtered Input/Output Average")
    print("\t\tInput Average\tOutput Average")
    for i in filterList:
        print("%d\t\t%f\t\t%f"%(int(i[0]), float(i[1]), float(i[2])))

    print("Sum of Input Average : %f" % sumInputAverage)
    print("Average of Input Average : %f\n" % (sumInputAverage / cntElements))

    print("Sum of Output Average : %f" % sumOutputAverage)
    print("Average of Output Average : %f\n" % (sumOutputAverage / cntElements))

    print("Total Reception Rate : %f\n" % (sumOutputAverage / sumInputAverage))

    for i in receptionRateDict:
        print("%d Reception Rate : %f"%(i, receptionRateDict[i]))

    print("\nMax Input : %f, Max Input Position : %d" %(maxInput, maxInputPosition))
    print("Min Input : %f, Min Input Position : %d\n" %(minInput, minInputPosition))

    print("Max Output : %f, Max Output Position : %d" %(maxOutput, maxOutputPosition))
    print("Min Output : %f, Min Output Position : %d\n" %(minOutput, minOutputPosition))

    print("Best Reception Rate : %f, Best Reception Rate Position : %d"%(bestReceptionRate, bestReceptionRatePosition))
    print("Worst Reception Rate : %f, Worst Reception Rate Position : %d\n"%(worstReceptionRate, worstReceptionRatePosition))



    input10SumDict={}
    output10Sum=0
    output10SumDict={}

    #print("for debug")
    #print(inputDict)
    cnt=0
    inputKeys = list(inputDict.keys())
    inputKeys2 = inputKeys.copy()
    outputKeys = list(outputDict.keys())
    outputKeys2 = outputKeys.copy()
    '''
    print("fordebug")
    print(inputKeys)
    inputKeys.pop(0)
    print(inputKeys)
    '''
    inputEndDict={}
    outputEndDict={}
    for i in inputKeys:
        input10Sum=0
        for j in inputKeys2:
            input10Sum = input10Sum + inputDict[j]
            cnt = cnt + 1
            if(cnt==10):
                cnt=0
                inputKeys2.pop(0)
                #print(inputKeys) # FOR DEBUG
                #print(i) #for debug
                inputEndDict[i]=int(j)
                input10SumDict[i]=input10Sum
                break

    for i in outputKeys:
        output10Sum=0
        for j in outputKeys2:
            output10Sum = output10Sum + outputDict[j]
            cnt = cnt + 1
            if(cnt==10):
                cnt=0
                outputKeys2.pop(0)
                #print(inputKeys) # FOR DEBUG
                #print(i) #for debug
                outputEndDict[i]=int(j)
                output10SumDict[i]=output10Sum
                break

    maxRecentInput10 = 0
    maxRecentInput10Position = 0
    maxRecentOutput10 = 0
    maxRecentOuput10Position = 0

    for i in input10SumDict:
        if(maxRecentInput10<float(input10SumDict[i])):
            maxRecentInput10Position = int(i)
            maxRecentInput10 = float(input10SumDict[i])
    print("max recent 10 input position : %s, value : %f"%(str(maxRecentInput10Position)+"-"+str(inputEndDict[maxRecentInput10Position]), maxRecentInput10))

    for i in output10SumDict:
        if(maxRecentOutput10<float(output10SumDict[i])):
            maxRecentOutput10Position = int(i)
            maxRecentOutput10 = float(output10SumDict[i])
    print("max recent 10 output position : %s, value : %f"%(str(maxRecentOutput10Position)+"-"+str(outputEndDict[maxRecentOutput10Position]), maxRecentOutput10))

    #for debug
    #print(input10Sum)
    #print(input10SumDict)
    #print(output10SumDict)

    with open("A_Result.txt", "w") as rf:
        rf.write("Filtered Input/Output Average\n")
        rf.write("\t\tInput Average\tOutput Average\n")
        for i in filterList:
            rf.write("%d\t\t%f\t%f\n"%(int(i[0]), float(i[1]), float(i[2])))

        rf.write("\nSum of Input Average : %f\n" % sumInputAverage)
        rf.write("Average of Input Average : %f\n\n" % (sumInputAverage / cntElements))

        rf.write("Sum of Output Average : %f\n" % sumOutputAverage)
        rf.write("Average of Output Average : %f\n\n" % (sumOutputAverage / cntElements))

        rf.write("Total Reception Rate : %f\n\n" % (sumOutputAverage / sumInputAverage))

        for i in receptionRateDict:
            rf.write("%d Reception Rate %f\n"%(i, receptionRateDict[i]))

        rf.write("\n\nMax Input : %f, Max Input Position : %d\n" %(maxInput, maxInputPosition))
        rf.write("Min Input : %f, Min Input Position : %d\n\n" %(minInput, minInputPosition))

        rf.write("Max Output : %f, Max Output Position : %d\n" %(maxOutput, maxOutputPosition))
        rf.write("Min Output : %f, Min Output Position : %d\n\n" %(minOutput, minOutputPosition))

        rf.write("Best Reception Rate : %f, Best Reception Rate Position : %d\n"%(bestReceptionRate, bestReceptionRatePosition))
        rf.write("Worst Reception Rate : %f, Worst Reception Rate Position : %d\n\n"%(worstReceptionRate, worstReceptionRatePosition))

        rf.write("max recent 10 input position : %s, value : %f\n"%(str(maxRecentInput10Position)+"-"+str(inputEndDict[maxRecentInput10Position]), maxRecentInput10))
        rf.write("max recent 10 output position : %s, value : %f\n"%(str(maxRecentOutput10Position)+"-"+str(outputEndDict[maxRecentOutput10Position]), maxRecentOutput10))
