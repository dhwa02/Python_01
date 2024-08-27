customer = "A"
coffee = 5
while coffee >= 1:
    print(f"{customer}, 커피가 준비 되었습니다. {coffee}분 후 폐기처분 하겠습니다.")
    coffee -= 1
    if coffee == 0:
        print("폐기처분 되었습니다.")

customer_2 = "B"
num = 1
while True:
    print(f"{customer_2}, 커피가 준비 되었습니다. 호출 {num}회")
    num += 1
    
# 무한 루프 해제 : ctrl + c
