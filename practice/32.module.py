# 필요한 함수 정의나 클래스만 따로 모아 두는 것을 모듈
# 32-2에 정의한 함수 중 필요한 것 들만 불러와서 사용 가능.

import theater_module
theater_module.price(3) # 3명이서 일반 가격으로 영화를 예매 시
theater_module.price_morning(4) # 조조 가격으로 영화를 예매 시
theater_module.price_soldier(5) # 군인 가격으로 영화를 예매 시

import theater_module as mv # theater_module라는 모듈 파일의 이름이 길어서 줄여서 표현할 수 있다.
mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)

from theater_module import * # theater_module내 모든 것을 불러오기 때문에, mv를 붙일 필요가 없다.
price(3)
price_morning(4)
price_soldier(5)

from theater_module import price, price_morning
price(5)
price_morning(4)
# price_soldier(3) # 오류 발생

from theater_module import price_soldier as ps
ps(3)
