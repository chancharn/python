# 난수를 사용하기 위해 random 모듈을 사용해야한다
from random import *

num1 = randint(1, 10) # 1 ~ 10사이의 임의의 정수(int)
print(num1)

num2 = random() # 0 ~ 1사이의 임의의 유리수(float)
print(num2)
num3 = uniform(1.0, 10.0) # 0 ~ 10사이의 임의의 유리수(float)
print(num3)

num4 = randrange(1, 101) # 1 ~ 100사이의 임의의 정수
num4 = randrange(1, 101, 2) # 1 ~ 100사이의 임의의 짝수??? 아닌데
print(num4)



# sample
# 램덤 모듈에서 sample기능을 이용하면 list, set, tuple 등의 자료로부터 일부를 추출할 수 있는 기능이다.

import random
numlist = range(1, 10)
numlist = list(numlist) # list형태로 변경
a = random.sample(numlist, 3) # 샘플로 3개를 추출한다.
print(a)