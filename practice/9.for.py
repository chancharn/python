# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")
# 위와 같은 것을 두줄로 표현이 가능하다

for waiting_no in range(0,5): # or for waiting_no in range(5): or for waiting_no in [0, 1, 2, 3, 4]:
    print("대기번호 : {0}".format(waiting_no))


starbucks = ["아이언맨", "토르", "그루트"]

for waiting_man in starbucks:
    print("{0}, 커피 나왔습니다.".format(waiting_man))