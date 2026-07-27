print("상속, super, 오버라이딩, 다형성")
# 부모클래스
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def work(self):
        print(self.name, "직원이 일합니다.")
    
    def print_info(self):
        print(f"이름 : {self.name}")
        print(f"급여 : {self.salary}원")

# 자식클래스
class Developer(Employee): # 상속
    def __init__(self, name, salary, language):
        # 부모 생성자 호출
        super().__init__(name, salary)

        self.language = language
    # 오버라이딩(재정의)
    def work(self):
        print(f"{self.name} 개발자가 {self.language} 프로그램을 작성합니다.")
    
    def print_info(self):
        super().print_info()
        print(f"개발 언어 : {self.language}")
# 자식클래스2
class Teacher(Employee):
    def __init__(self, name, salary, subject):
        super().__init__(name, salary)
        self.subject = subject
    
    def work(self):
        print(f"{self.name} 선생님이 {self.subject}과목을 가르칩니다")
    
    def print_info(self):
        super().print_info()
        print(f"과목 : {self.subject}")

dev = Developer("이성진", 100000000, "파이썬")
tea = Teacher("이썽진", 237498792, "국어")

print("개발자 정보")
dev.print_info

print("\n 교사 정보")
tea.print_info()

# -----------------------------------------------------
print("\n 직원들의 업무")
e_list = [dev,tea]

for i in e_list:
    i.work()
    print("="* 30)
# 자바 다형성 : 부모 타입 - 자식 객체
# 파이썬 다형성 : 객체가 같은 이름의 함수를 갖고 있음
# -> 실행할때마다 각각의 서로 다른 객체의 함수가 실행
# 개발자는 개발자의 work()
# 교사는 교사의 work()