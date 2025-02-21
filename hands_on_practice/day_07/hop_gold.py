def printMaze(arr):
    for i in range(ROW):
        for k in range(COL):
            print(f'{arr[i][k]:3d}', end=' ')  # 정수 변환 없이 그대로 출력
        print()
    print()

def growRich():
    memo = [[0 for _ in range(COL)] for _ in range(ROW)]
    memo[0][0] = goldMaze[0][0]

    # 첫 번째 행 초기화
    for i in range(1, COL):
        memo[0][i] = memo[0][i - 1] + goldMaze[0][i]

    # 첫 번째 열 초기화
    for i in range(1, ROW):
        memo[i][0] = memo[i - 1][0] + goldMaze[i][0]

    # DP 테이블 채우기
    for row in range(1, ROW):
        for col in range(1, COL):
            memo[row][col] = max(memo[row][col - 1], memo[row - 1][col]) + goldMaze[row][col]

    maxGold = memo[ROW - 1][COL - 1]

    print('## 메모이제이션 ##')
    printMaze(memo)

    # 경로 추적을 위한 별도 배열 생성 (원본 memo 보존)
    path = [[1 for _ in range(COL)] for _ in range(ROW)]  # 기본적으로 1로 설정

    row, col = ROW - 1, COL - 1
    while row != 0 or col != 0:
        path[row][col] = 0  # 최적의 경로를 0으로 마킹
        if row > 0 and col > 0:
            if memo[row - 1][col] > memo[row][col - 1]:
                row -= 1
            else:
                col -= 1
        elif col > 0:
            col -= 1
        else:
            row -= 1
    path[0][0] = 0  # 시작점도 경로로 설정

    print('## 황금 미로 길 (경로) ##')
    printMaze(path)

    return maxGold

# 전역변수 선언
ROW, COL = 5, 5
goldMaze = [[1, 4, 4, 2, 2],
            [1, 3, 3, 0, 5],
            [1, 2, 4, 3, 0],
            [3, 3, 0, 4, 2],
            [1, 3, 4, 5, 3]]

# 메인 코드
maxGold = growRich()
print(f'황금 미로에서 얻은 최대 황금 개수 --> {maxGold}')