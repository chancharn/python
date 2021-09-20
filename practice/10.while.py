# 조건이 만족할 때까지 반복 while 조건:

customer = "토르"
index = 5

while index >= 1: # index가 조건, >=1까지 계속 무한루프, 조건 충족시 stop
    print("{0}, 커피가 준비 되었습니다. {1}번만 더 부를게요.".format(customer, index-1))
    index -= 1
    if index == 0:
        print("커피는 폐기 처분 되었습니다.")




customer = "복길이"
person = "unknown"
# index 문에 대해서 사용방법을 잘 모르겠네...
while customer != person:
    print("{0}님, 커피나왔습니다.".format(customer))
    person = input("성함이 어떻게 되세요? ")
    if customer != person:
        print("그쪽거 아닙니다.")
    if customer == person:
        print("여기 있습니다.")
# 조건 충족시 while문을 빠져나가지만 아래 "여기 있습니다." 명령어까지 수행하고 함수를 나감