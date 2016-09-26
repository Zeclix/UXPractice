#입력에서 프로세스를 이름(int)입력받고 프로세스이름보다 2가 많은 프로세스 시간을 할당하는 프로그램을 list로 생성하여 이를 적용하시오
class process:
    processTime = 0
    processName = 0
    def __init__(self, processName):
        self.processName = processName
        self.processTime = processName+2
    def getProcessTime(self):
        return self.processTime
    def getProcessName(self):
        return self.processName
    def getProcessList(self):
        return [self.processName, self.processTime]


processName = int(input("Enter process time(int) : "))

a = process(processName)

processList=a.getProcessList()

print(processList)