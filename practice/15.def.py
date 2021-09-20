# 함수의 기본값 정의

def profile(name, age, major):
    print("이름 : {0} \t 나이 : {1} \t 전공 : {2}".format(name, age, major))

profile("즐라탄", 40, "축구") # 즐라탄, 축구라는 매개변수는 문자가 아니므로 ""처리 반드시 해주어야 한다.
profile("아드리아누", 42, "축구")

# 축구선수니까 전공은 공통부분이므로 기본 값으로 처리
def profile(name, age, major="축구"):
    print("이름 : {0} \t 나이 : {1} \t 전공 : {2}".format(name, age, major))

profile("즐라탄", 40) # major는 함수를 정의할 때 미리 지정을 해줬기 때문에 생략 가능하다.
profile("아드리아누", 42)

# 키워드 값을 이용한 함수 정의
def profile(name, age, major="축구"):
    print("이름 : {0} \t 나이 : {1} \t 전공 : {2}".format(name, age, major))

profile(major = "축구", age = 40, name = "토레스") # 순서를 바꾸어도 키워드 값에 맞춰 순서 자동 정렬

# 가변인자를 활용한 함수 정의
def profile(name, age, lang1, lang2, lang3):
    print("이름 : {0}\t 나이 : {1}\t".format(name, age), end=" ") # 여기서 end를 저렇게 써주면 아래의 print문을 한 줄로 출력 가능하게 해준다.
    print(lang1, lang2, lang3)

profile("손흥민", 30, "java", "python", "c#")
profile("혼다", 37, "java", " ", " ")

# 혼다 같은 경우 언어를 하나 밖에 사용하지 못하기 때문에 lang2,3을 ""로 처리를 해주어야 하는 귀찮은 일이 생긴다, 또는 손흥민이 하나의 언어를 더 배우게 되면 함수자체를 수정해야 하는
# 복잡한 일이 생기게 되기 때문에, 가변인자를 활용해 함수를 작성한다
def profile(name, age, *language):
    print("이름 : {0}\t 나이 : {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print() # 이걸 넣어주어야 줄 바꿈이 됨

profile("손흥민", 30, "java", "python", "c#", "한국어", "영어", "중국어", "일본어")
profile("혼다", 37, "일본어")