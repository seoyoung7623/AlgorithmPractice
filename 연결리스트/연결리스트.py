# 연결리스트 : 링크를 이용해 다음 순서의 자료를 탐색
'''
1. 싱글 연결리스트
2. 더블 연결리스트
3. 원형 연결리스트
'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __str__(self):
        return str(self.data)

# 싱글 연결리스트
class SingleLinkedList:
    def __init__(self,data):
        new_node = Node(data)
        self.head = new_node
        self.list_size = 1

    def __str__(self):
        print_list = '[ '
        node = self.head
        while True:
            print_list += str(node)
            if node.next == None:
                break
            node = node.next
            print_list += ', '
        print_list += ' ]'
        return print_list

    # 첫번째 노드 삽입 (헤더가 교체됨)
    def insertFirst(self,data):
        new_node = Node(data)
        temp_node = self.head
        self.head = new_node
        self.head.next = temp_node # 새로 생성된 헤더의 링크를 기존의 헤드의 링크로 변경

        self.list_size += 1

    # 노드 선택(인덱스 번호로 노드 선택)
    def selectNode(self,num):
        if self.list_size < num:
            return
        node = self.head
        count = 0
        while count < num:
            node = node.next
            count += 1
        return node
    
    # 마지막 노드 삽입
    def insertLast(self,data):
        node = self.head
        while True:
            if node.next == None:
                break
            node = node.next
        
        new_node = Node(data)
        node.next = new_node
        self.list_size += 1
    
    # 중간 노드 삽입
    def insertMiddle(self,num,data):
        if self.head.next == None: #헤더가 만들어진 직후에 메서드를 사용하는 경우
            self.insertLast(data)
            return
        node = self.selectNode(num)
        new_node = Node(data)
        temp_next = node.next
        node.next = new_node
        new_node.next = temp_next
        self.list_size += 1

    # 노드삭제
    def deleteNode(self,num):
        if self.list_size < 1:
            return
        elif self.list_size < num:
            return
        if num == 0:
            self.deleteHead()
            return
        node = self.selectNode(num-1)
        # 이전 노드의 링크를 다다음 노드와 연결하기 위해 이전 노트 선택
        node.next = node.next.next
        del_node = node.next
        del del_node

    # 헤더 노드삭제
    def deleteHead(self):
        node = self.head
        self.head = node.next
        del node

    def size(self):
        return str(self.list_size)

if __name__ == "__main__":
    m_list = SingleLinkedList(1)
    m_list.insertLast(5)
    m_list.insertLast(6)
    print('LinkedList :', m_list)
    print('LinkedList Size() :', m_list.size())
    print('LinkedList SelectNode(1) :', m_list.selectNode(1))

    m_list.insertMiddle(1, 15)
    print('LinkedList Insert Middle(1, 15) :', m_list)

    m_list.insertFirst(100)
    print('LinkedList Insert First(100) : ', m_list)
    print('LinkedList SelectNode(0) :', m_list.selectNode(0))

    m_list.deleteNode(0)
    print('LinkedList Delete Node(0) : ', m_list)
    m_list.deleteNode(1)
    print('LinkedList Delete Node(1) : ', m_list)