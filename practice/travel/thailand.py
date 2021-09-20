class ThailandPackage:
    def detail(self):
        print("[태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원")

if __name__ == "__main__": # 모듈 내에서 실행하는 경우에 대한 함수
    print("Thailand 모듈을 직접 실행")
    print("이 문장은 모듈을 직접 실행할 때만 실행이된다.")
    trip_to = ThailandPackage()
    trip_to.detail()
else:
    print("Thailand 외부에서 모듈 호출")
# 5 ~ 11의 코드를 확인해보려면, thailand.py에서 직접 run을 실행해보면, 6,7번과 같은 문장이 생성되고,
# package.py에서 run을 실행해보면, 11번과 같은 문장이 생성된다.
# 만약 다른 프로젝트를 할 때에도 사용하던 모듈이 필요하다면 복사해서 사용하면 된다.

# pypi.org라는 사이트에 들어가면 다른 이들이 사용하던 package를 다운받을 수 있다.
# pip install beautifulsoup - 패키지 설치
# pip install --upgrade beautifulsoup
# pip uninstall beautifulsoup