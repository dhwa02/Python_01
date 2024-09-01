name = "마린"
hp = 40
damage = 5

print(f"{name} 유닛이 생성되었습니다.")
print(f"체력 {hp}, 공격력 {damage}\n")

tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print(f"{tank_name} 유닛이 생성되었습니다.")
print(f"체력 {tank_hp}, 공격력 {tank_damage}\n")

tank2_name = "탱크"
tank2_hp = 150
tank2_damage = 35

print(f"{tank2_name} 유닛이 생성되었습니다.")
print(f"체력 {tank2_hp}, 공격력 {tank2_damage}\n")

def attack(name, location, damage):
    print(f"{name} : {location} 방향으로 적군을 공격합니다. [공격력 : {damage}]")

attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)
attack(tank2_name, "1시", tank2_damage)

# 유닛을 하나하나 설정하는것은 한계가 있음. 따라서 클래스 사용