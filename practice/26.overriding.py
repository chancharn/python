# 오버라이딩
# 부모 클래스를 받아서 하는게 아닌 자식 클래스에서 정의한 메소드를 사용하는 것을 오버라이딩이라고 한다.

class Unit:
    def  __init__(self, name, hp, speed): 
        self.name = name 
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))
    

class Attackunit(Unit): 
    def  __init__(self, name, hp, speed, damage): 
        Unit.__init__(self, name, hp, speed) # 세개는 Unit에 있는 값을 가져온다.
        self.damage = damage 

    def attack(self, location): 
        print("{0} : {1} 방향으로 적군이 공격합니다. [공격력 {2}]".format(self.name, location, self.damage)) 

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage)) 
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

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
        print("[공중 유닛 이동]")
        self.fly(self.name, location)


vulture = Attackunit("벌쳐", 80, 10, 20)
battlecruiser = FlyableAttackunit("배틀크루저", 500, 25, 3)

vulture.move("11시")
# battlecruiser.fly(battlecruiser.name, "9시")
# 매번 지상 공중 구분을 하기가 번거롭다
battlecruiser.move("9시")


# ------------------------------
# pass

class BuildingUnit():
    def __init__(self, name, hp, location):
        pass # 아무것도 안하고 일단 넘어간다는 의미

building1 = BuildingUnit("건물", 200, "7시") # run해도 터미널창에 뜨지 않음을 확인할 수 있다.

def game_start():
        print("[알림] 새로운 게임을 시작한다.")

def game_over():
        pass


game_start()
game_over()