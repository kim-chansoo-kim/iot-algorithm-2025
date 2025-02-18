# 전역변수
memory = []
head, prev, curr = None, None, None
dataArray = [['지민', '010-1111-1111'], ['정국', '010-2222-2222'], ['뷔', '010-3333-3333'], 
             ['슈가', '010-4444-4444'], ['진', '010-5555-5555']]

# ----------------------------------------------------------------------------------------    
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
        return str(self.__data)
# ----------------------------------------------------------------------------------------

# 데이터 출력 함수
# ----------------------------------------------------------------------------------------
def printNodes(start):
    curr = start
    if curr == None:
        return
    print(curr.getData(), end=' -> ')

    while curr.getLink() != None:
        curr = curr.getLink()
        if curr.getLink() == None:
            print(curr.getData(), end=' ')
        else:
            print(curr.getData(), end=' -> ')
    print()
# ----------------------------------------------------------------------------------------

# 데이터 삽입 함수
# ----------------------------------------------------------------------------------------
def insertNode(namePhone, insertData):
    global memory, head, prev, curr

    node = Node(insertData)
    memory.append(node)

    if head == None:
        head = node
        return

    # 삽입할 위치 찾기
    if head.getData()[0] > namePhone[0]:
        node.setLink(head)
        head = node
        return
    
    curr = head
    while curr.getLink() != None:
        prev = curr
        curr = curr.getLink()
        if curr.getData()[0] > namePhone[0]:
            node.setLink(curr)
            prev.setLink(node)
            return
    
    curr.setLink(node)
# ----------------------------------------------------------------------------------------

# 연결 리스트 생성
# ----------------------------------------------------------------------------------------
if __name__ == '__main__':
    if not dataArray:
        print("데이터가 없습니다.")
    else:
        head = Node(dataArray[0])
        memory.append(head)

        prev = head
        for name in dataArray[1:]:
            node = Node(name)
            if prev:
                prev.setLink(node)
            prev = node
            memory.append(node)

        printNodes(head)

        insertNode(['지민', '010-1111-1111'], ['퐁당', '010-6666-6666'])
        printNodes(head)