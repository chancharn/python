# 지역변수 : 함수내에서만 사용 / 함수가 끝나면 사라지는 함수
# 전역변수 : 프로그램 내에서 모두 사용 가능 / 자주 사용하면 복잡해져 지양함

gun = 10

# def checkpoint(soldiers): # 경계근무 나간 군인 수
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))

# print("전체 총 : {0}".format(gun))
# checkpoint(2) # 2명이 경계근무 나감
# print("남은 총 : {0}".format(gun))
# (6~12줄)이렇게하면 오류가 나온다. 
# 4번 줄의 gun은 gun = gun - soldiers에서 앞의 gun에 대한 값이고, 두번째 gun은 함수 내의 지역변수인데 값이 지정되지 않았기 때문이다.

# # 해결방법 1.
# def checkpoint(soldiers):
#     gun = 10 # 이렇게 지역변수를 직접 지정을 해 주기
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))

# print("전체 총 : {0}".format(gun))
# checkpoint(2) # 2명이 경계근무 나감
# print("남은 총 : {0}".format(gun))


# # 해결방법 2.
# def checkpoint(soldiers):
#     global gun # 전역 변수를 사용하면, gun = gun - soldiers에서 두번째 gun이 global gun 값을 할당받기 때문에 오류안남.
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint(soldiers):
    global gun # 전역 변수를 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_return(gun, soldiers): # 매개변수의 gun은 지역변수이지만 global gun 값을 받기 때문에, 39번째 줄의 두번째 gun 값이 있음.
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun
# 이해가 쉽도록 윗 줄의 'gun = 10'의 gun은 gun1, 지역변수 gun은 gun2라고 명기
# return gun으로 해줌으로서, gun 값이 함수 밖에서도 영향을 미치기 때문에, 48번째 줄에서 함수를 실행하면 8이 나오게 된다.

print("전체 총 : {0}".format(gun))
# checkpoint(2) # 2명이 경계근무 나감
gun = checkpoint_return(gun, 2)
print("남은 총 : {0}".format(gun))