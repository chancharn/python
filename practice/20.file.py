# 파일 입출력

# 변수 생성 / score.txt파일에, 쓰기, utf8형식으로
# "w"는 덮어쓰기, "a"를 쓴다면 이어서 작성
score_file = open("score.txt", "w", encoding="utf8")
print("수학 : 0", file=score_file)
print("영어 : 0", file=score_file)
score_file.close() # score_file함수 닫기

score_file = open("score.txt", "a", encoding="utf8")
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100") 
score_file.close()
# score_file.write로 작성하면 따로 줄 구분이 안되기 때문에 \n을 넣어줘서 줄 구분해주어야 한다

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read())
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline()) # 한 줄씩 읽기
print(score_file.readline(), end="")
print(score_file.readline(), end="")
score_file.close()

# 상대에게 받은 파일을 읽을 경우, 몇 줄이 있는지 모를 떄
score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    print(line)
    if not line:
        break
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # 파일 내 모든 line 가지고 와서,리스트 형태로 저장
for line in lines:
    print(line, end="")
score_file.close()
