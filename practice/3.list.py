# 리스트 : 각각의 값들을 하나로 묶어주는 역할을 하는 것

subway = ["유재석", "조세호", "박명수"]
print(subway)
print(subway[1]) # 리스트 값을 index
# subway = ["유재석", "조세호", ["유재석", ["유재석", "조세호", "박명수"], "박명수"]]
# 리스트 안에 리스트가 존재하는 경우 subway[2][1][0] 이런식으로도 표현 가능

print(subway.index("조세호")) # index : 리스트 내에 조세호가 몇 번째에 위치하고 있는지

subway.append("하하") # append : 맨뒤에 추가
print(subway)

subway.insert(1, "즐라탄") # insert : 원하는 위치에 삽입하고 싶을 때 / 위치는 0, 1, 2, 3, 4, 이런식으로 나아간다.
print(subway)

subway.pop() # pop : 뒤부터 한명씩 꺼낼 때
print(subway)

subway.append("즐라탄")
print(subway.count("즐라탄")) # count : "즐라탄"이라는 요소가 몇 개인지

subway.remove("유재석") # 유재석이라는 인자를 직접 찾아서 삭제하여준다.
print(subway)

del(subway[0]) # 0번째 위치한 인자를 삭제해준다
print(subway)

num_list = [2, 3, 1, 5, 4]
num_list.sort() # sort : 순서대로 정렬
print(num_list)

num_list.reverse() # reverse : 역순으로 정렬
print(num_list)

num_list.clear() # clear : 모든 내용 삭제
print(num_list)

# 문자, 숫자 등 다양한 자료형으로 사용 가능
mix_list = ["조세호", 20, True]
num_list = [2 ,1 ,5]
mix_list.extend(num_list) # append는 요소 값을 추가한다면, extend는 리스트를 추가
print(mix_list)
num_list.extend(mix_list)
print(num_list)