# 지금까지 해온 클래스 상속의 개념으로 스타크래프트 실행해보겠다.
from random import *

class Unit:
    def  __init__(self, name, hp, speed): # --> 파라미터
        self.name = name # --> 매개변수
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name)) # 매개변수인 self.name을 사용해도 파라미터인 name을 써도 상관없다.

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))
    
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage)) 
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

class Attackunit(Unit): 
    def  __init__(self, name, hp, speed, damage): 
        Unit.__init__(self, name, hp, speed) # 세개는 Unit에 있는 값을 가져온다.
        self.damage = damage 

    def attack(self, location): 
        print("{0} : {1} 방향으로 적군이 공격합니다. [공격력 {2}]".format(self.name, location, self.damage)) 

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아간다. [속도 {2}]".format(name, location, self.flying_speed))

class FlyableAttackunit(Attackunit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        Attackunit.__init__(self, name, hp, 0, damage) # 지상 speed는 0으로 설정
        Flyable.__init__(self, flying_speed)
    
    def move(self, location):
        self.fly(self.name, location)

class Marine(Attackunit):
    def __init__(self):
        Attackunit.__init__(self, "마린", 40, 1, 5)

    # 스팀팩 : 일정 시간 동안 공격, 이동 속도 증가, 체력 10 감소
    def steampack(self):
        if self.hp >= 10:
            self.hp -= 10
            print("{0} 유닛이 스팀팩을 사용하였습니다.".format(self.name))
        else:
            print("{0} 체력이 부족하여 스팀팩을 사용할 수 없습니다.".format(self.name))

class Tank(Attackunit):
    # 시즈모드 : 공격력 상승, 이동 불가
    sieze_developed = False # 시즈모드 개발여부

    def __init__(self):
        Attackunit.__init__(self, "탱크", 150, 1, 35)
        self.sieze_mode = False

    def set_sieze_mode(self):
        if Tank.sieze_developed == False:
            return

        # 시즈모드로 변환
        if self.sieze_mode == False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.sieze_mode = True
        
        # 시즈모드 해제
        else:
            print("{0} : 시즈모드를 해제합니다.".format(self.name))
            self.damage /= 2
            self.sieze_mode = False

class Wraith(FlyableAttackunit):
    def __init__(self):
        FlyableAttackunit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False # 개발이 되어 있다고 가정 / 클로킹 모드 해제 상태

    def clocking(self):
        if self.clocked == True: # 클로킹 모드일 시 해제
            print("{0} : 클로킹 모드를 해제합니다.".format(self.name))
            self.clocked = False
        
        else:
            print("{0} : 클로킹 모드를 설정합니다.".format(self.name))
            self.clocked = True

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    print("player : GG")
    print("[player]님이 퇴장하였습니다.")




# 게임 시작
game_start()

# 마린 3기, 탱크 2기, 레이스 1기 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()
t1 = Tank()
t2 = Tank()
w1 = Wraith()

# 위에서 생성한 유닛을 일괄적으로 관리하기 위해 리스트화 한다.
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# 전군 이동
for unit in attack_units:
    unit.move("1시")

# 탱크 시즈모드 개발
Tank.sieze_developed = True
print("[알림] 탱크 시즈모드 개발이 왼료되었습니다.")

# 공격 모드 준비 (탱크 : 시즈모드, 마린 : 스팀팩, 레이스 : 클로킹)
for unit in attack_units:
    if isinstance(unit, Marine): # isinstance는 이 유닛이 마린이 맞는지 확인할 때 / 여러 클래스의 객체가 리스트에 있기 때문에, 이 특정 유닛이 Marine클래스가 맞는지 확인할 때
        unit.steampack()
    elif isinstance(unit, Tank):
        unit.set_sieze_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

# 전군 공격
for unit in attack_units:
    unit.attack("1시")

# 전군 피해
for unit in attack_units:
    unit.damaged(randint(5, 20))
# 특정 데미지가 아닌 난수로 데미지를 입는다 가정. / random 모듈 불러오기 from random import *

# 게임 종료
game_over()