class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print(f"{name} 유닛이 생성 되었습니다.")
        print(f"체력 {hp}, 공격력 {damage}")

# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

wraith1 = Unit("레이스", 80, 5)
print(f"유닛 이름 : {wraith1.name}, 공격력 : {wraith1.damage}")

wraith2 = Unit("레이스(적)", 80, 5)
wraith2.clocking = True # class 외부에서 내가 원하는 변수 확장이 가능함 (확장시킨 객체에 한하여 적용)

if wraith2.clocking == True:
    print(f"{wraith2.name}는 현재 클로킹 상태입니다.")