# set = 집합과 같은 개념
# 중복 x, 순서 x

set = {1,2,3,3,3,3,3,3,}
print(set) # 중복이 허용되지 않기 때문에 {1, 2, 3}으로만 표현된다.

java = {"즐라탄", "메시", "루니"}
python = {"즐라탄", "손흥민"}
# python = set(["즐라탄", "손흥민"]) - set 명령어인데 사용이 안되고 있음...

# 교집합 (java & python 모두 활용 가능자)
print(java & python)
print(java.intersection(python))

# 합집합 (둘 중 하나라도 사용 가능한 자)
print(java | python)
print(java.union(python))

# 차집합 (java는 할 줄 알고 python 할 줄 모르는 사람)
print(java - python)
print(java.difference(python))

# python을 할 줄 아는 사람 추가
python.add("호날두")
print(python)

# python을 까먹어 버림
python.remove("손흥민")
print(python)

# 자료구조 변경
# 집합의 자료구조
menu = {"아메리카노", "라떼", "모카"}
print(menu, type(menu))

# 집합 -> 리스트로 변경
menu = list(menu)
print(menu, type(menu)) 

# 리스트 -> 튜플로 변경
menu = tuple(menu)
print(menu, type(menu)) 