# 클래스 상속

# 일반 유닛
class Unit:
    def  __init__(self, name, hp): # 생성자 역할, marine, tank같은 객체가 만들어질 때 자동으로 호출되는 함수
        self.name = name # 클래스 내에서 정의된 변수 = 맴버 변수
        self.hp = hp
    
# 공격 유닛
# 일반 유닛에 있는 name, hp와 같은 것을 공격 유닛에서 재활용할 수 있는데, 이걸 상속이라고 한다.
class Attackunit(Unit): # 위의 일반 유닛 클래스를 상속하려면 '()'안에 Unit를 입력
    def  __init__(self, name, hp, damage): 
        Unit.__init__(self, name, hp) # 일반 유닛을 상속받아 name, hp를 재활용하기 때문에 Unit.__init__(self, name, hp)로 작성
        self.damage = damage # 일반 유닛에는 damage가 없으므로 따로 추가

    def attack(self, location): 
        print("{0} : {1} 방향으로 적군이 공격합니다. [공격력 {2}]".format(self.name, location, self.damage)) 

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage)) 
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))


# 다중 상속 - 부모가 2 이상
# 위의 일반 유닛 클래스인 Unit가 부모 클래스, Attackunit클래스가 자식 클래스라고 한다.

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아간다. [속도 {2}]".format(name, location, self.flying_speed))

# 아래의 클래스는 Attackunit와 Flyable 두 개의 클래스를 상속받는다
class FlyableAttackunit(Attackunit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        Attackunit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)

valkyrie = FlyableAttackunit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시") # Flyable 함수의 경우 별도로 이름 정보가 없기 때문에, valkyrie.name이라고 지정해주어야 한다..?????
