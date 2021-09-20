print(abs(-10)) # abs : 절대값
print(pow(4, 3)) # pow : 앞의 변수에 뒤에 변수 횟수만큼 제곱 4*4*4
print(max(5, 12)) # max : 최대값, min : 최소값
print(round(3.14)) # round :반올림

from math import * # math로부터 * 임포트를 해주어야 버림, 올림, 제곱근 사용 가능
print(floor(4.99)) # floor : 버림
print(ceil(3.001)) # ceil : 올림
print(sqrt(16)) # sqrt : 제곱근

# 랜덤함수
from random import *
print(random()) # 0.0 ~ 1.0 미만의 임의의 값 (디폴트)
print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값
print(int(random() * 10)) # 0.0 ~ 10.0 미만의 임의의 값 중 정수 형태로
print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값

x = randrange(4, 29) # 4 ~ 28중 임의의 값
print("오프라인 스터디 모임 날짜는 매월 " + str(x) + "일로 선정되었습니다.") # 18번 줄에서 x값이 숫자형으로 정의되었기 때문에, str(문자열로) 치환해주어야 한다.
print("오프라인 스터디 모임 날짜는 매월 ", x, "일로 선정되었습니다.") # 이렇게 표현하면 str로 감싸지 않아도 된다.

# 문자열 슬라이스는 pass

python = "Python is Amazing"
print(python.lower()) # python 내의 문자를 소문자로 치환
print(python.upper()) # python 내의 문자를 대문자로 치환
print(len(python)) # 길이 / 만약 list형에서 len을 사용하면, 리스트 내 값들의 갯수
print(python.replace("Python", "Java")) # "Python"을 "Java"로 바꾸기
print(python[0].isupper()) # python문자의 0번째 문자가 대문자인지 확인 (boolean형식)

python = "Python is Amazing"
index = python.index("n")
print(index) # n이 있는 위치 색인
index = python.index("n", index + 1) # 첫번째 n이 나온 위치가 5, 'index + 1'은 다음 n이 나오는 위치(첫번째 n나온 위치 그 다음 위치부터 0으로 시작)
print(index) # n이 있는 위치 색인
# index와 find의 차이 : 거의 유사하지만 기능, but find는 없으면 -1을, index는 없으면 오류를 낸다
print(python.find("Java"))
# print(python.index("Java"))

print(python.count("y"))
# python 문장 중  y갯수를 나타냄

# 문자열 포맷팅
a = ("나는 {0}살이고, {1}입니다.").format(20, "남자")
print(a)
age = 31
sex = "male"
b = ("나는 {0}살이고, {1}입니다.").format(age, sex)
print(b)
c = ("나는 {1}살이고, {0}입니다.").format(age, sex)
print(c)
d = ("나는 {country}살고, {job}입니다.").format(country="서울", job="백수")
print(d)







# 추가
print("ㅋ" * 9)

age = 31
# print("난" + age + "살이다.") # 오류 / 즉, +를 사용하려면, 자료의 형태가 같아야지 사용 가능하다. (문자열은 문자열끼리)
print("난", age, "살이다.") # 잘 실행됨

# 연산자
print(2**3) # 거듭제곱
print(5/3) # 나누기
print(5//3) # 몫
print(5%3) # 나머지