# quiz) 당신의 학교에서는 파이
# 댓글 작성자들 중 추첨을 통해 1명은 치킨, 3명은 쿠폰을 받게 됩니다.
# 추첨 프로그램을 작성하시오.

# 조건1 : 댓글은 20명이 작성하였고, 아이디는 1~20이라고 가정
# 조건2 : 무작위로 추첨하되, 중복 불가
# 조건3 : ramdom 모듈의 shuffle과 sample

# (출력 예시)
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
# -- 축하합니다 --

# (활용 예제)
# from random import *
# lst = [1, 2, 3, 4, 5]
# print(lst)
# shuffle(lst)
# print(lst)
# print(sample(lst, 1))

from random import *
# [1, 2, 3, 4... ] 다 적어주기 보단
users = range(1, 21) # 이렇게 간편하게 할 수 있지만, 우리가 원하는 리스트가 아닌 range라는 타입이기 때문에 타입을 변경해 주어야 한다.
print(type(users)) 
users = list(users) # range 타입을 list형으로 변경
print(type(users))

print(users)
shuffle(users) # 배열되어 있는 users를 섞어주는 역할
print(users)

winners = sample(users, 4)
print(winners)

print(" -- 당첨자 발표 -- ")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:4]))
print("치킨 당첨자 : {0}, {1}, {2}".format(winners[1], winners[2], winners[3]))
print(" -- 축하합니다 -- ")