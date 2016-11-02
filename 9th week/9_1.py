class Radio:
    def __init__(self):
        print("라디오가 생성되었습니다")
        pass
    def turn_on(self):
        print("라디오를 켭니다")
    def turn_off(self):
        print("라디오를 끕니다")
    def __del__(self):
        print("라디오가 종료되었습니다")
class Car:
    def __init__(self):
        self._speed=0
        print("자동차가 생성되었습니다")
        self._radio=Radio()
    def getspeed(self):
        return self._speed
    def start(self):
        self._speed=20
        print("자동차가 출발합니다")
    def accelerate(self):
        self._speed=self._speed + 30
        print("자동차가 가속합니다")
    def stop(self):
        self._speed=0
        print("자동차가 정지합니다")


myCar = Car()
myCar.start()
print("속도:", myCar.getspeed())
myCar.accelerate()
print("속도:", myCar.getspeed())
myCar.stop()
print("속도", myCar.getspeed())

