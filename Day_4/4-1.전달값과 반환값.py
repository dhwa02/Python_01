def deposit(balance, money): # 입금
    print(f"입금이 완료되었습니다. 잔액은 {balance + money}원 입니다.")
    return balance + money

def withdraw(balance, money): # 출금
    if balance >= money:
        print(f"출금이 완료되었습니다. 잔액은 {balance - money}원 입니다.")
        return balance - money
    else:
        print(f"현재 잔액이 출금 잔액보다 적습니다. 다시 시도하십시오. (현재 잔액 : {balance})")
        return balance

def withdraw_night(balance, money):
    print(f"수수료는 {commission}원 이며, 잔액은 {balance-money-commission}원 입니다.")
    return commission, balance - money - commission

balance = 0 # 잔액
commission = 100 # 수수료

balance = deposit(balance, 1000)

# balance = withdraw(balance, 5000)
# print(balance)

balance = withdraw_night(balance, 500)
