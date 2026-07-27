import math # marh 모듈 수학 계산 함수
import random
num = 25

print("제곱근: ",math.sqrt(num))
print("2의 3제곱",math.pow(2,3))
print("원주율: ",math.pi)

student = ["강해린","설윤","유관순","세종"]

dice = random.randint(1,6)

print("발표학생 : ",random.choice(student))
print("주사위 값",dice)