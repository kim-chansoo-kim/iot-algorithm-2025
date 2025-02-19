# 허니버터칩이 가장 많이 남은 편의점 찾기

## 전역변수
#----------------------------------------------------------------------------------------    
G = None
storeAry = [['GS25', 30], ['CU', 60], ['Seven11', 10], ['Ministop', 90], ['Emart24', 40]] # 편의점 배열 정의[이름, 허니버티칩개수]
GS25, CU, Seven11, Ministop, Emart24 = 0, 1, 2, 3, 4
#----------------------------------------------------------------------------------------    

## 그래프 클래스(인접 행렬 생성)
#----------------------------------------------------------------------------------------    
class Graph:
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]
#----------------------------------------------------------------------------------------

# 그래프 출력 함수
#----------------------------------------------------------------------------------------
def printGraph(g):
    print(' ', end='  ')
    for v in range(g.SIZE):
        print(f"{storeAry[v][0]:>10}", end='  ')
    print()
    
    for row in range(g.SIZE):
        print(f"{storeAry[row][0]:>10}", end='  ')
        for col in range(g.SIZE):
            print(f"{g.graph[row][col]:>8}", end='  ')  # 가운데 정렬
        print()
    print()
#----------------------------------------------------------------------------------------

## 메인 모듈
#----------------------------------------------------------------------------------------
gSize = 5
G = Graph(gSize)
G.graph[GS25][CU] = 1; G.graph[GS25][Seven11] = 1
G.graph[CU][GS25] = 1; G.graph[CU][Seven11] = 1; G.graph[CU][Ministop] = 1
G.graph[Seven11][GS25] = 1; G.graph[Seven11][CU] = 1; G.graph[Seven11][Ministop] = 1
G.graph[Ministop][Seven11] = 1; G.graph[Ministop][CU] = 1; G.graph[Ministop][Emart24] = 1
G.graph[Emart24][Ministop] = 1

print('## 편의점 그래프 ##')
printGraph(G)

stack = []
visitedAry = []

current = 0 # 시작 편의점을 GS25로 한다
maxStore = current
maxCount = storeAry[current][1]
stack.append(current)
visitedAry.append(current)

# 깊이 우선 탑색 방식으로 순회
#----------------------------------------------------------------------------------------
while(len(stack) !=0):
    next = None    
    for vertex in range(gSize):
        if G.graph[current][vertex] == 1:
            if vertex in visitedAry:
                continue
            else:
                next = vertex
                break
# 방문 편의점이 허버칩이 최대개수보다 많으면, 방문한 편의점을 최대보유 편의점으로 지정
    if next != None:
        current = next
        stack.append(current)
        visitedAry.append(current)
        if storeAry[current][1] > maxCount:
            maxCount = storeAry[current][1]
            maxStore = current
    else:
        current = stack.pop()
#----------------------------------------------------------------------------------------
print(f"허니버티칩 최대 보유 편의점(개수) --> {storeAry[maxStore][0]} ({storeAry[maxStore][1]})")
#----------------------------------------------------------------------------------------

from collections import deque

# 편의점 데이터
storeAry = [['GS25', 30], ['CU', 60], ['Seven11', 10], ['Ministop', 90], ['Emart24', 40]]
GS25, CU, Seven11, Ministop, Emart24 = 0, 1, 2, 3, 4

# 그래프 클래스
class Graph:
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

# 그래프 생성
gSize = 5
G = Graph(gSize)
G.graph[GS25][CU] = 1; G.graph[GS25][Seven11] = 1
G.graph[CU][GS25] = 1; G.graph[CU][Seven11] = 1; G.graph[CU][Ministop] = 1
G.graph[Seven11][GS25] = 1; G.graph[Seven11][CU] = 1; G.graph[Seven11][Ministop] = 1
G.graph[Ministop][Seven11] = 1; G.graph[Ministop][CU] = 1; G.graph[Ministop][Emart24] = 1
G.graph[Emart24][Ministop] = 1


### BFS(너비 우선 탐색)로 허니버터칩이 가장 많은 편의점 찾기
#----------------------------------------------------------------------------------------
def bfs_max_honey_chips(start):
    queue = deque([start])
    visited = set([start])
    
    max_store = start
    max_count = storeAry[start][1]

    while queue:
        current = queue.popleft()

        for neighbor in range(gSize):
            if G.graph[current][neighbor] == 1 and neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

                # 허니버터칩 개수 비교하여 최대값 업데이트
                if storeAry[neighbor][1] > max_count:
                    max_count = storeAry[neighbor][1]
                    max_store = neighbor

    return max_store, max_count

# BFS 탐색 시작 (GS25 기준)
maxStore, maxCount = bfs_max_honey_chips(GS25)

# 결과 출력
print(f"허니버터칩 최대 보유 편의점(개수) --> {storeAry[maxStore][0]} ({storeAry[maxStore][1]})")
#----------------------------------------------------------------------------------------