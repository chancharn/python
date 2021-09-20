class Unit:
    def  __init__(self, name, hp, damage): # 생성자 역할, marine, tank같은 객체가 만들어질 때 '자동'으로 호출되는 함수
        self.name = name # 클래스 내에서 정의된 변수 = 맴버 변수
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5) # Unit라는 클래스에 입력하는 변수랑 똑같은 갯수의 변수가 입력이 되어야 한다. (self는 제외)
# marine2 = Unit("마린") -> X
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

print("유닛이름 : {0}, 공격력 : {1}".format(tank.name, tank.damage))
# tank.name, tank.damage와 같은 표기 방법으로 클래스 내부에 있는 값들을 활용할 수 있다.

wraith1 = Unit("레이스", 80, 5) 
# wraith 변수에 '= Unit'를 입력하여 클래스를 불러오면, 안의 변수 값들이 wraith.name, wraith.hp, wraith.damage로 사용 가능
wraith1.clocking = True

if wraith1.clocking == True:
    print("{0}은 현재 클로킹 상태입니다.".format(wraith1.name))

# if wraith2.clocking == True:
#     print("{0}은 현재 클로킹 상태입니다.".format(wraith2.name))
# # wraith2는 clocking라고 지정해주지 않았기 때문에 오류가 발생
