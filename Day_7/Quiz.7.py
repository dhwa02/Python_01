class SoldOutError(Exception):
    pass
    
chicken = 10
waiting = 1
while(True):
    try:
        print(f"[남은 치킨 : {chicken}]")
        order = int(input("치킨 몇 마리 주문하시겠습니까 ? "))
        if order > chicken:
            print("재료가 부족합니다.")
        elif chicken - order == 0:
            raise SoldOutError("재고가 소진되어 더 이상 주문을 받지 않습니다.")
        elif order < 1:
            raise ValueError
        else:
            print(f"[대기번호 {waiting}] {order} 마리 주문이 완료되었습니다.")
            waiting += 1
            chicken -= order

    except ValueError:
        print("잘못된 값을 입력하였습니다.")

    except SoldOutError as err:
        print(err)
        break