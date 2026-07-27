print("다중 상속과 mro")
class Login:
    def run(self):
        print("run() 실행")
    def Login(self):
        print("Login() 실행")

class Printer:
    def run(self):
        print("Printer 클래스의 run() 실행")
    def print_info(self):
        print("프린터 합니다")
# 다중 상속
class Study(Login,Printer):
    def study(self):
        print("수업중입니다.")

s = Study() # 객체 생성
s.Login()
s.print_info()
s.study()
s.run() # 상속 우선순위(왼쪽) 부모의 함수 호출
Printer.run(s)
# 상속 우선순위가 낮은 부모의 함수 호출
print("함수 탐색 순서:")
print(Study.mro())
# 클래스.mro() : 클래스 찾는 순서를 리스트로 보여줌 