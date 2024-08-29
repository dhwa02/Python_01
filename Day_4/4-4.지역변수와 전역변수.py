gun = 10

def checkpoint(soldiers):
    # gun = 20 # 지역변수
    global gun # 전역변수
    gun = gun - soldiers
    print(f"현재 총의 개수 : {gun}")

def checkpoint_return(gun, soldiers):
    gun = gun - soldiers
    print(f"현재 총의 개수 : {gun}")
    return gun

print(f"전체 총 : {gun}")
gun = checkpoint_return(gun, 2)
print(f"남은 총 : {gun}")