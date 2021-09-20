class Unit:
    def  __init__(self, name, hp): # 생성자 역할, marine, tank같은 객체가 만들어질 때 자동으로 호출되는 함수
        self.name = name # 클래스 내에서 정의된 변수 = 맴버 변수
        self.hp = hp

class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp):
        self.damage = damage