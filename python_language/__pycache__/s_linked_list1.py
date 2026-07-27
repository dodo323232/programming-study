# s_linked_list1.py
# 단일 연결 리스트 : 노드가 data와 ilink 로 구성

class Node : 
    def __init__(self,data):
        self.data=data
        self.next = None

node1 = Node(10)
print("저장 값",node1.data)
print("다음 노드:", node1.next)

# 노드 세개 연결하여 출력
class Node2:
    def __init__(self,data):
        self.data=data
        self.next=None

head = Node2(10)
head.next = Node2(20)
head.next.next= Node2(30)

cur = head # 첫위치를 현재 위치로 정함

while cur is not None: # None이 아닐떄가지 반복
    print(cur.data) # 노드의 값 출력
    cur=cur.next # 다음 노드로 현재 위치를 변경

# --------------------------------------
class Node3:
    def __init__(self,data):
        self.data=data
        self.next=None

class S_list:
    def __init__(self):
        self.head=None
        # head는 첫위치를 기억하는 변수
    def append(self,data):
        new_node = Node3(data) # 새 노드 등장

        if self.head is None: # 노드가 전혀 없으면
            self.head= new_node # 새로운 노드부터 시작
            return

        curr=self.head # 첫위치를 현재위치로도 정함

        while curr.next is not None: # 끝까지 이동(None 일때까지)
            curr = curr.next # 뒤로 하나씩 이동

        curr.next = new_node # 마지막 노드 뒤에 새 노드 연결

    def print_list(self):
        curr=self.head  
        if curr is None: 
            print("연결리스트가 비어있습니다")
            return 
        while curr is not None:
            print(curr.data, end="-> ")
            curr=curr.next
        print("None")

        print("노드 개수",self.length())

    def Sort(self):
        if(self.head == None):
            print("head값이 없습니다")
            return

        swap = True
        while swap:
            swap = False
            current = self.head
            while(current.next is not None):
                if(current.data > current.next.data):
                    current.data, current.next.data = current.next.data, current.data
                    swap = True
                current = current.next
        # 맨 앞에 새 노드를 삽입
    def insert_first(self,data):
        new_node = Node3(data) # 새 노드 생성

        new_node.next = self.head
        # 처음 위치를 새 노드의 다음 위치로 변경
        self.head = new_node
        # 새 노드를 가장 앞으로 삽입한다
    
    def length(self):
        count = 0
        curr = self.head
        while(curr is not None):
            count+=1
            curr = curr.next
        return count
    def delete(self,target):
        if self.head is None:
            print("노드가 존재하지 않습니당")
            return

        # 첫번째 위치에 있을 경우 삭제
        if(self.head.data == target):
            self.head = self.head.next
            # 2번째 위치를 첫번째 위치로 이동
            print(target,"삭제 완료")
            return

        curr = self.head
        while(curr.next is not None):
            if(curr.next.data == target):
                curr.next = curr.next.next
                print(target,"삭제 완료")
                return
            curr = curr.next
        print("값을 찾지 못함")


s = S_list()
s.append(200)
s.append(100)
s.append(400)
s.insert_first(30)
s.print_list()
s.Sort()
s.print_list()
s.delete(100)
s.print_list()