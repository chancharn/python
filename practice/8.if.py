weather = input("오늘 날씨는 어때요 ? ") # input는 사용자에게 변수 값을 직접 입력하게 하는 문장

if weather == "비" or weather== "눈": # and, or, <= 부등호도 사용 가능
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크 챙기세요")
else:
    print("준비물 필요없어요")