# super

# class Unit:
#     def  __init__(self, name, hp, speed): 
#         self.name = name 
#         self.hp = hp
#         self.speed = speed

#     def move(self, location):
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         # Unit.__init__(self, name, hp, 0) # 위에서 사용하던 상속의 방법
#         super().__init__(name, hp, 0)
#         # 81번과 같은 기능을 super로 표현해도 똑같이 작동한다.
#         # 문제는 다중상속을 하는 경우에 발생한다.
#         self.location = location


class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit, Flyable): # super로 상속을 받을 경우 ()안의 상속받으려는 class중 맨 처음 class만 가져온다.
    def __init__(self):
        super().__init__()

dropship = FlyableUnit() # 결과값이 Unit 클래스의 값으로 나오게 된다.

# 그냥 super 기능을 쓰지말고, 상속을 받으면 될거 같다.