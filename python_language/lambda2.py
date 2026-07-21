print("sort()와 람다함수")
# 리스트 안에 튜플
# 순서 있음 : 리스트 [], 튜플() => 불변
# 순서 없음 : 집합

students = [
    ("홍길동",60),
    ("권율",92),
    ("이순신",88),
    ("유관순",74)
]
# sorted(정렬할 자료, key=정렬기준)
result = sorted(students,key=lambda x: x[1])
# sorted는 리스트 안에 요소들을 하나씩 꺼내면서 비교한다
# students 리스트의 요소들은
# ("홍길동",60),("권율",92),("이순신",88),("유관순",74)이 있다
# 하지만 이 튜플로는 비교가 애매하기 때문에 
# 함수를 받는 key를 이용해 각각의 요소의 첫번째 인덱스인 정수들로
# 비교를 해야 한다

print("오름차순")
print(result)
for a in result: # result의 요소를 꺼내서 a라는 변수에 넣는다
    print(a)

result = sorted(students,key=lambda x: x[1], reverse = True)
print("내림차순")
print(result)

print("=" * 50)

print("딕셔너리 -> 리스트의 정렬")
stu=[
    {"name":"홍길동", "score" : 70},
    {"name":"이성진", "score" : 99},
    {"name":"설윤", "score" : 100},
    {"name":"아이유", "score" : 64},
]

stu_result = sorted(stu,key=lambda x : x["score"], reverse = True)

print("점수가 높은 순서부터 출력")
for ss in stu_result:
    print(ss["name"],ss["score"])