# Quiz) 표준 체중을 구하는 프로그램 생성

# * 표준 체중 : 각 개인의 키에 적당한 체중

# (성별에 따른 공식)
# 남자 : 키(m) * 키(m) * 22
# 여자 : 키(m) * 키(m) * 21

# 조건1 : 표준 체중은 별도의 함수 내에서 계산
#         * 함수명 : std_weight
#         * 전달값 : 키(height), 성별(gender)
# 조건2 : 표준 체중은 소수점 둘째자리까지 표시

# (예제)
# 키 175cm 남자의 표준 체중은 67.38kg입니다.



# 내가 작성한 답(오류 뜸)
# gender = input("성별을 입력하시오 : (남자 or 여자) ")
# height = input("키를 입력하시오 : ")

# def std_weight(height, gender): # 키를 m단위로, 성별은 "남자 or 여자"
#     if gender == "남자":
#         weight = height * height * 22
#         return weight
#     else:
#         weight = height * height *21
#         return weight

# weight = round(std_weight(height / 100, gender), 2)

# print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))


# 강사용 정답
def std_weight(height, gender): # 키를 m단위로, 성별은 "남자 or 여자"
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21

height = 175
gender = "남자"
weight = round(std_weight(height / 100, gender), 2) # 소수점 둘째자리까지만 표현

print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))