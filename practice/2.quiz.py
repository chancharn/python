# 사이트 url에 따른 임의 비밀번호 생성

# 예 : http://naver.com

# 규칙1 : http:// 부분 제외
# 규칙2 : .이후 부분은 제외
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 "e" 갯수 + "!"로 구성

# 생성된 비밀번호 : nav51!

# url = "http://naver.com"
url = "http://google.com"
# url = "http://youtube.com"

# 규칙1
rule1 = url.replace("http://", "") # 슬라이스 말고 이런 방식으로도 가능
print(rule1)

# 규칙2
rule2 = rule1[0:5]
print(rule2)
# or
rule2_2 = rule1[0:rule1.index(".")]
print(rule2_2)

# 규칙3
rule3 = rule2[:3] + str(len(rule2)) + str(rule2.count("e")) + "!"
print(rule3)

print("{0}의 임의생성된 비밀번호는 {1}입니다.".format(url, rule3))





# 규칙 1, 2 해결 _ 내 방식
a = "http://naver.com"
a = a[7:12]
rule1 = a[:3]
rule2 = len(a)
rule3 = a.count("e")
rule4 = rule1 + str(rule2) + str(rule3) + "!"
print(rule4)