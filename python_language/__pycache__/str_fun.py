# str_fun.py
class SimpleBook:
    def __init__(self, title, price):
        self.title = title
        self.price = price
    def __str__(self):
        return f"도서명: {self.title},가격: {self.price}원"

s = SimpleBook("파이썬기초",20000)
print(s)
# s라는 객체를 출력하려고 하면 자동으로 __str__메서드를 호출한다
# __str__()메서드 : 원하는 포맷으로 출력을 원할때 사용
# __str__()메서드 : 문자열으로 return 함