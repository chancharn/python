# 패키지 : 모듈을 모아둔 것

import travel.thailand # import는 모듈이나 패키지는 불러올 수 있지만, class는 불러오지 못 한다.
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

from travel.thailand import ThailandPackage # 이런식으로는 class를 불러올 수 있다.
trip_to = ThailandPackage()
trip_to.detail()

from travel import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()

from travel import * 
# import *을 사용하면, travel폴더 내의 모든 모듈을 사용할 수 있을 것 같지만, 그렇지 않다.
# travel.__init__파일로 들어가서
# __all__ = ["vietnam"]이라고 작성을 해주어야 베트남 모듈 파일을 사용할 수 있다.
# thailand모듈도 사용하고 싶다면 __all__ = ["vietnam", "thailand"]라고 입력해주면 된다.
trip_to = vietnam.VietnamPackage()
trip_to.detail()

from travel import *
trip_to = thailand.ThailandPackage()
trip_to.detail()

# 모듈, 패키지의 위치를 확인할 수 있다.
import inspect
import random
print(inspect.getfile(random)) # 29번째 줄에서 호출된 random이라는 모듈이 어디에 있는지 위치를 알 수 있다.
from travel import thailand
print(inspect.getfile(travel.thailand))
