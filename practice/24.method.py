class Attackunit:
    def  __init__(self, name, hp, damage): # 생성자 역할, marine, tank같은 객체가 만들어질 때 자동으로 호출되는 함수
        self.name = name # 클래스 내에서 정의된 변수 = 맴버 변수
        self.hp = hp
        self.damage = damage
        # print("{0} 유닛이 생성 되었습니다.".format(self.name))
        # print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

    def attack(self, location): # 클래스를 쓸 땐 그냥 맨 앞에 self를 적어준다고 생각하면 된다.
        print("{0} : {1} 방향으로 적군이 공격합니다. [공격력 {2}]".format(self.name, location, self.damage)) 
        # 10번 줄의 self.name, self.damage는 3과 5줄의 변수를 쓴다는 것을 의미하고, location은 9번 줄에서 정의한 location을 그대로 사용한다는 의미

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage)) # self.damage와 다른 변수이다
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))
            

firebat1 = Attackunit("파이어뱃", 50, 16)
firebat1.attack("5시")
# 21번 줄에서 이미 Attackunit라는 클래스로 name, hp, damage라는 값이 생성이 되었으므로, firebat1은 Attackunit를 품고 있다, 그렇기 때문에 firebat1.damage만 입력해주면 된다.
firebat1.damaged(25)
firebat1.damaged(25)