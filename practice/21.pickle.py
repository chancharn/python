# pickle란 데이터를 파일 형태로 저장

import pickle
profile_file = open("profile.pickle", "wb") # pickle의 경우 바이너리형태로 작성해야해서, w가 아닌 Wb라고 적어야 한다.
profile = {"이름":"박명수", "나이":30, "취미":["축구","골프","코딩"]}
print(profile)
pickle.dump(profile, profile_file) # profile에 있는 정보를 profile_file에 저장
profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # profile_file에 있는 데이터를 profile에 불러오기
print(profile)
profile_file.close()


# pickle 간편 작업

with open("profile.pickle", "rb") as profile_file:
# profile.pickle 파일을 읽기형태로 불러와서, profile_file라는 변수에 저장
    print(pickle.load(profile_file))
# file를 불러와서 프린트 / 따로 close해줄 필요 없음


# pickle를 사용하지 않고 with문으로 파일 다루는 방법
with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부했다.")
# "r"로 study_file에 있는 데이터를 불러옴
with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())