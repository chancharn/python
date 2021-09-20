# Quiz) 매주 1회 보고서 작성, 아래와 같은 형태로

# - x 주차 주간보고 -
# 부서 :
# 이름 :
# 업무 요약 :

# 1 ~ 50 주차까지 보고서 파일을 만드는 프로그램 작성

# 조건 : 파일명은 '1주차.txt' ... 와 같이 만들기

for i in range(1, 3):
    with open(str(i)+"주차.txt", "w", encoding="utf8") as report_file:
        # report_file.write(str(i)+"주차 주간보고")
        report_file.write("{0}주차 주간보고".format(i))
        report_file.write("""
        부서 : 
        이름 : 
        업무요약:
        """)
