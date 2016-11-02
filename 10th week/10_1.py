import os

list1 = [1,2,3,4,6,7,8,9,10,""]

selectNum='a'

print(list1)

while(1):
    selectNum=input("Select insert, delete, quit : ")
    if(selectNum=='insert' or selectNum=='i'):
        current=0
        dest=0
        cntNotNone=0
        for i in list1:
            if(i!=""):
                cntNotNone=cntNotNone+1
        if(cntNotNone==10): #리스트가 꽉 찬 경우
            print("List is full")
            continue

        insertNum=int(input("Enter the number : "))
        for i in list1:
            if(i==""):
                break
            elif(i==insertNum):
                temp = insertNum
                dest = current
                for j in range(current, 10):
                    temp2 = list1[dest]
                    list1[dest]=temp
                    temp = temp2
                    dest=dest+1
                break
            elif(i<insertNum):
                if(list1[current+1]==""):
                    list1[current+1]=insertNum
                    break
                if(insertNum<=list1[current+1]):
                    temp = insertNum
                    dest = current+1
                    for j in range(current+1, 10):
                        temp2 = list1[dest]
                        list1[dest]=temp
                        temp = temp2
                        dest=dest+1
                    break

            current=current+1
        print(list1)

    elif(selectNum=='delete' or selectNum=='d'):
        current = 0
        dest = 0
        cntNone=0
        for i in list1:
            if(i==""):
                cntNone=cntNone+1

        if(cntNone==10):
            print("List is empty")
            continue

        deleteNum = int(input("Enter the number : "))


        for i in list1:
            #print("test1")
            if(i==deleteNum):
                dest = current
                for j in range(current, 10):
                    if(dest<9):
                        list1[dest] = list1[dest+1]
                        dest=dest+1
                    elif(dest==9):
                        list1[9]=""
            current = current+1
        print(list1)


    elif(selectNum=='quit'):
        print("Quit program")
        os._exit(1)
    else:
        continue