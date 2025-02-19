# 그래프 - 깊이우선탐색


# 전역변수
#----------------------------------------------------------------------------------------    
G1 = None
stack = []          # 스택
visitedAry = []     # 방문기록
#----------------------------------------------------------------------------------------    

# 그래프 클래스
#----------------------------------------------------------------------------------------    
class Graph:
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]
#----------------------------------------------------------------------------------------    

## 메인코드
#----------------------------------------------------------------------------------------
SIZE = 4
G1 = Graph(SIZE)
# 0:A, 1:B, 2:C, 3:D
# A의 간선
G1.graph[0][2] = 1
G1.graph[0][3] = 1
# B의 간선
G1.graph[1][2] = 1
# C의 간선
G1.graph[2][0] = 1
G1.graph[2][1] = 1
G1.graph[2][3] = 1
# D의 간선
G1.graph[3][0] = 1
G1.graph[3][2] = 1

print('## G1 무방향 그래프 ##')
for row in range(G1.SIZE):
    for col in range(G1.SIZE):
        print(G1.graph[row][col], end=' ')
    print()
#----------------------------------------------------------------------------------------    

## DFS시작
#----------------------------------------------------------------------------------------  
print('\n## DFS 시작! ##')
current = 0 # A를 뜻하는 0
stack.append(current) # Stack push(A)
visitedAry.append(current) # 방문기록 A

while(len(stack) !=0): # Stack 길이가 0이 되면 모든 정점을 방문했다는 뜻
    next = None    
    for vertex in range(SIZE):
        if G1.graph[current][vertex] == 1: # [현재][도착점] == 1 # 간선이 있다
            if vertex in visitedAry: # 도착점이 방문한 적이 있는 정점이면 탈락
                continue # pass를 써도 되지만 컨티뉴가 맞음
            else: # 방문한 적이 없으면 다음 정점으로 지정
                next = vertex # 다음 번 방문할 정점
                break

    if next != None: # 다음에 방문할 정점이 있으면
        current = next # 넥스트가 커런트로
        stack.append(current)
        visitedAry.append(current)
    else:
        current = stack.pop() # 다시 돌기

print('방문순서', end=' --> ')
for i in visitedAry:
    print(chr(ord('A')+i), end=' ') # 문자A에 대한 ASCII 코드값 출력
print()
#----------------------------------------------------------------------------------------  