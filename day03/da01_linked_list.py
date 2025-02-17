# 단순 연결 리스트

## 전역변수
memory = [] # 컴퓨터 메모리처럼 보이게 만든 변수
head, prev, curr = None, None, None # 항상 첫번째 노드, curr바로 앞의 노드, 현재 선택한 노드
dataArray = ['다현', '정연', '쯔위', '사나', '지효',] # 연결리스트를 만들 데이터

# 노드 클래스
#----------------------------------------------------------------------------------------    
class Node:
    def __init__(self, data):
        self.__data = data
        self.__link = None

    def setLink(self, link):
        self.__link = link
        
    def getData(self):
        return self.__data
    
    def getLink(self):
        return self.__link
    
    def __str__(self):
        return self.__data
#----------------------------------------------------------------------------------------    

# 데이터 생성함수
#----------------------------------------------------------------------------------------    
def printNodes(start):
    curr = start
    if curr == None: return

    print(curr.getData(), end=' -> ')

    while curr.getLink() != None: # 현재링크의 다음링크가 있는동안
        curr = curr.getLink() # 다음 노드를 가리킴
        if curr.getLink() == None: # 더 이상 다음 노드가 없어 화살표 삭제
            print(curr.getData(), end=' ')
        else:           
            print(curr.getData(), end=' -> ')

    print() # 그냥 한줄 내려줌
#----------------------------------------------------------------------------------------    

# 데이터 삽입함수
#----------------------------------------------------------------------------------------    
def insertNode(findData, insertData):
    global memory, head, prev, curr # 전역변수를 가져와서 insertNode함수안에서 쓰겠다는 선언  
#----------------------------------------------------------------------------------------    
    # 맨 처음에 데이터 삽입
    if head.getData() == findData:
        node = Node(insertData)
        node.setLink(head) # 현재 head가 가리키는 node를 새노드의 링크로 연결
        head = node # head는 새node로 설정
        return # 더 이상 밑으로 실행 안되도록 함수 탈출
#----------------------------------------------------------------------------------------    
    # 중간에 데이터 삽입
    curr = head
    while curr.getLink() !=None:
            prev = curr
            curr = curr.getLink()
            if curr.getData() == findData:
                node = Node(insertData)
                node.setLink(curr)
                prev.setLink(node)
                return # 더 이상 밑의 로직이 실행안되도록 함수 탈출
#----------------------------------------------------------------------------------------    
    # 마지막에 데이터 삽입
    node = Node(insertData)
    curr.setLink(node)
#----------------------------------------------------------------------------------------    

# 데이터 삭제함수
#----------------------------------------------------------------------------------------    
def deleteNode(deleteData):
    global memory, head, curr, prev
    # 첫번째 노드 삭제
    if head.getData() == deleteData: 
        curr = head
        head = head.getLink()
        del(curr)
        return
#----------------------------------------------------------------------------------------   

#----------------------------------------------------------------------------------------   
    # 중간, 마지막 노드 삭제
    curr = head
    while curr.getLink != None:
        prev = curr
        curr = curr.getLink()
        if curr is None: return # 단순로직으로 예외처리
        if curr.getData() == deleteData:
            prev.setLink(curr.getLink()) # 지우려는 노드의 링크를 prev에서 가리키도록
            del(curr)
            return
#----------------------------------------------------------------------------------------   

# 데이터 검색함수
#----------------------------------------------------------------------------------------   
def findNode(findData):
    global memory, head, curr, prev

    curr = head
    if curr.getData() == findData:
        return curr
    
    while curr.getLink != None:
        curr = curr.getLink()
        if curr is None: return
        if curr.getData() == findData:
            return curr
    return None # 찾는 데이터가 없음
#----------------------------------------------------------------------------------------

# 연결리스트 생성, 삽입, 삭제 구현
#----------------------------------------------------------------------------------------    
if __name__ == '__main__': # 시작모듈일때

    node = Node(dataArray[0]) # '다현' 사용
    head = node
    memory.append(node)

    for name in dataArray[1:]: # '정연'부터 사용
        prev = node # '다현'이 들어있는 노드를 prev에 할당
        node = Node(name) # 0/정연, 1/쯔위, 2/사나, 3/지효
        prev.setLink(node) # 이전 노드에 현재노드를 연결
        memory.append(node)

    printNodes(head)
    # 5개의 데이터를 가지는 연결리스트 생성 끝

#----------------------------------------------------------------------------------------    
    # 데이터 삽입
    insertNode('다현', '화사')
    printNodes(head)

    insertNode('사나', '솔라')
    printNodes(head)

    insertNode('재남', '문별')
    printNodes(head)
#----------------------------------------------------------------------------------------    

#----------------------------------------------------------------------------------------
    # 데이터 검색
    fNode = findNode('화사')
    print(fNode)

    fNode = findNode('퐁당')
    print(fNode)
#----------------------------------------------------------------------------------------   

#----------------------------------------------------------------------------------------
    # 데이터 삭제
    deleteNode('화사')
    printNodes(head)
    
    deleteNode('쯔위')
    printNodes(head)

    deleteNode('')
    printNodes(head)
#----------------------------------------------------------------------------------------