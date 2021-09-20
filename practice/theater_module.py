# 일반 영화 가격
def price(people): # 굳이 함수 정의 안하고 price = 10000으로 할랬는데, people라는 파라미터를 받아야 해서..? 
    print("{0}명의 가격은 {1}원 입니다.".format(people, 10000 * people))

# 조조 영화 가격
def price_morning(people):
    print("{0}명의 조조 할인 가격은 {1}원입니다.".format(people, 6000 * people))

# 군인 할인 가격
def price_soldier(people):
    print("{0}명 군인 할인 가격은 {1}원입니다.".format(people, 4000 * people))