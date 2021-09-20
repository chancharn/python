cabinet = {1:"유재석", 2:"조세호", 3:"즐라탄"} # 키 값에 숫자형 뿐만 아니라 문자형도 가능

print(cabinet.get(1)) # key 값이 1인 value 출력 / 0, 1, 2와 같이 1번째 순서의 value값 출력하는 문장 아님
print(cabinet[1]) # key 값이 1인 value 출력

print(cabinet.get(4))
# print(cabinet[4])
# 두 방식 다 같은 결과 값을 도출하지만, 위의 경우 키 값이 없으면 none라고 출력이 되고, 아래는 없는 키 값을 입력하면 프로그램이 종료된다.

print(cabinet.get(4, "사용가능")) # none 대신 사용가능이라고 출력할 수도 있다.

print(3 in cabinet) # 3이라는 키 값이 있는지 확인 / boolean 형태로 출력됨
print(5 in cabinet) # 5라는 키 값이 있는지 확인

cabinet[1] = "정형돈" # 값 변경
cabinet["F2-1"] = "아드리아누" # 값 추가

del cabinet[2] # 값 삭제
# del(cabinet[2])

print(cabinet.keys()) # 키 값만 출력
print(cabinet.values()) # 벨류 값만 출력
print(cabinet.items()) # 모두 출력

cabinet.clear() # 캐비넷 안의 모든 값 삭제
print(cabinet)