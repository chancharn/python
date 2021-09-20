# 표준 입출력

# print("java", "python")
# print("java", "python", sep= ", ")
# print("java", "python", sep= " vs ")
# print("java", "python", "javascript", sep=" vs ")

# print("java", "python", end= "? ") # 아래 구문을 이어서 출력
# print("뭐가 더 어려울까요?")


# 뭔지 찾아보기
# import sys
# print("python", "java", file=sys.stdout)
# print("python", "java", file=sys.stderr)

# 문자 정렬
scores = {"수학" : 0, "영어" : 50, "코딩" : 100}
for subject, score in scores.items(): # 키, 밸류 모두 받을 때 item
    #print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=" : ") # ljust(8)은 8칸 공간을 확보하고 왼쪽 정렬

# 은행 대기 순번표
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(4)) # zfill : 4개의 공간 확보 후 빈공간은 '0'을 채우는 것

# a = input("뭐라도 말해봐") # input로 값을 입력받으면 무조건 str(문자)형태로 받는다