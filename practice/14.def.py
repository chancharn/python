# 함수 정의
def open_account():
    print("새로운 계좌가 생성되었습니다.")

# 함수 실행
open_account()

def deposit(balance, money): # 입금 / ()사이의 값은 전달하려는 값
    print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money): # 출금
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0}원입니다".format(balance - money))
        return balance - money
    else:
        print("잔액이 부족합니다. 잔액은 {0}원 입니다.".format(balance))
        return balance

def withdraw_night(balance, money):
    commission = 100 # 야간 수수료
    return commission, balance - money - commission # 여러개의 값을 한번에 반환 가능

balance = 0 # 잔액 / balance => 변수
balance = deposit(balance, 1000) # balance라는 변수가 deposit 함수 호출
balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance, 300)
print("수수료는 {0}원이며, 잔액은 {1}원입니다.".format(commission, balance))