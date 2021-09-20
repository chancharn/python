# Quiz) 50명의 승객과 매칭 기회가 있을 경우, 총 탑승 승객 수를 구하는 프로그램
# 조건 1 : 승객별 운행 소요 시간은 5 ~ 50분 사이의 난수로 정해진다.
# 조건 2 : 당신은 소요시간 5 ~ 15분 사이의 승객만 태울 수 있다.

from random import *

customer = 0 # 총 탑승한 승객
# time = randrange(5, 51)
# 반드시 for문 안에 작성을 해주어야 한다. 그렇지 않으면 이미 time라는 하나의 변수가 생성되고, 그 하나의 변수 값만을 가지고 함수를 실행한다
for i in range(1, 51): # 1 ~ 50까지의 승객
    time = randrange(5, 51) # 5 ~ 50분 사이의 임의의 소요시간
    if 15 >= time >= 5: # 매칭 성공된 승객, 승객 수 증가 처리
        print("[O] {0}번째 손님(소요시간 : {1}분".format(i, time))
        customer += 1
    else: # 매칭 실패한 승객
        print("[ ] {0}번째 손님(소요시간 : {1}분".format(i, time))

print("총 탑승 승객 : {0}명".format(customer))