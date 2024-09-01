class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        #방법 1 (다중 상속 사용 시 적절하지 못함. 다중 상속 중 맨 앞 클래스만 호출하기 때문)
        super().__init__()

        #방법 2
        Unit.__init__(self)
        Flyable.__init__(self)

dropship = FlyableUnit()