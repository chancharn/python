# continue & break

absent = [2 ,5] # 결석자들
no_book = [7]

for student in range(1, 11):
    if student in absent: # 결석자라면
        continue # student가 absent에 있다면 다시 5번째 줄 for문으로 올라가서 계속 하라
    elif student in no_book:
        print("{0}아, 교무실로 와라. 오늘 수업은 여기까지 한다.".format(student))
        break
    print("{0}아, 읽어라".format(student))