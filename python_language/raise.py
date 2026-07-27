# throw : 오류를 일부로 발생
# throws : 호출한 곳으로 오류 처리하게 던지기
age = -5
# if age <=0:
#     raise ValueError("나이가 0보다 작거나 같을수는 없다")
# print("나이는: ",age)

try:
    age = int(input("나이를 입력하세요"))
    if age <=0:
        raise ValueError("나이가 0보다 작거나 같을수는 없다")
except ValueError as e:
    print("오류 발생",e)
else:
    print("나이는:",age)
finally:
    print("끝")
