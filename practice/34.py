# 내장함수
# 따로 import를 써줄 필요가 없는 함수이다.
# 예 : input

# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 갖고 있는지 표시
print(dir())
import random # 외장함수
print(dir()) # 목록에 random이 추가가 됨을 알 수 있다.
import pickle
print(dir())

print(dir(random)) # random 모듈로 사용할 수 있는 기능 열거

lst = [1, 2, 3]
print(dir(lst)) # list에 사용할 수 있는 함수 기능 열거

name = "Jim"
print(dir(name)) # name변수에 쓸 수 있는 함수 기능 열거

# list of python builtins라고 구글에 검색하면 내장함수가 어떤게 있는지 볼 수 있다.


# 외장함수 : 직접 import로 갖고 와야 함
# list of python modules라고 검색하면 외장함수를 볼 수 있다.
