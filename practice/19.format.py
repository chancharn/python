# 다양한 출력 포맷

# 빈 자리는 빈 공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))

# 오른쪽 정렬, 양수일 땐 +로, 음수일 땐 -로 부등호 표시, 10자리 확보
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

# 왼쪽 정렬하고, 빈칸을 _로 채움
print("{0:_<+10}".format(500))

# 3자리 마다 콤마 찍어주기
print("{0:,}".format(10000000000000))
# 3자리 마다 콤마 찍어주기, 부호도 붙이기
print("{0:+,}".format(10000000000000))
print("{0:+,}".format(-10000000000000))
# 3자리 마다 콤마 찍어주기, 부호도 붙이기, 자릿수 확보하기
# 빈자리는 ^로 채워주기
print("{0:^<+30}".format(10000000000))
# 소수점 출력
print("{0:f}".format(5/3)) # {0:f}
# 특정 자리수까지만 표시
print("{0:.2f}".format(5/3))