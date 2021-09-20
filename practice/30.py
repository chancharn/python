# 예외처리

try: # 예를 들어서 num1, num2에 정수라는 숫자형 값이 입력되어야 하는데, 문자로 '삼' 혹은 '사'라는 식으로 입력이 된다면, syntax error이 발생하는데 이를 막기 위해 예외처리를 해준다.
    print("나눗셈 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요. "))
    num2 = int(input("두 번째 숫자를 입력하세요. "))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError:
    print("에러! 잘못 입력하였습니다!")
# 그렇다면 num2에 '0'을 입력하게 되면? ZeroDivisionError이 발생
except ZeroDivisionError as err:
    print(err)
# 이와 같은 ValueError or ZeroDivisionError과 같은 유형을 따로 예외처리를 해줄 수 있다.

# except: # 위의 ValueError, ZeroDivisionError을 제외한 나머지 에러가 발생하면, 아래와 같은 문구를 보여주게 만드는 예외처리
#     print("알 수 없는 에러가 발생하였습니다.")

except Exception as err: 
    print("알 수 없는 에러가 발생하였습니다.")
    print(err)
# 15, 16라인과 같은 용도이지만 'as err'을 작성해주고, print(err)을 작성해 줌으로서, 어떤 에러코드가 발생하였는지 터미널 창에서 확인할 수 있다.


# 에러 발생시키기
try:
    print("한 자리 숫자 나누기 전용 계산기 입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise ValueError
    else:
        print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")

# 사용자 정의 예외처리
class BigNumberError(Exception): # Exception이라는 클래스를 상속한다는 의미
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기 입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2)) # BigNumberError의 괄호 안의 값을 입력하면 BigNumberError가 괄호 안의 값을 가지게 된다.
    else:
        print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
except BigNumberError as err:
    print("에러가 발생하였습니다. 한 자리 숫자만 입력해 주세요.")
    print(err) # print(err)의 의미가 BigNumberError가 발생했을 때 48에서 입력한 값이 출력되게 만드는 역할 / 48처럼 괄호안에 값을 넣은게 아니면 BigNumberError그대로 출력
finally: # 예외처리 부분에서 정상적으로 처리되거나 오류가 발생하건 상관없이 무조건 실행된다.
    print("계산기를 이용해 주셔서 감사합니다.")