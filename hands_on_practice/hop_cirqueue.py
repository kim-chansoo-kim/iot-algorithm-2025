# 원형 큐 구현

## 함수선언
#----------------------------------------------------------------------------------------
def isQueueFull():
    global SIZE, queue, front, rear

    if ((rear+1) % SIZE == front):
        return True
    else:
        return False
#----------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------
def isQueueEmpty():
    global SIZE, queue, front, rear
    if (front == rear):
        return True
    else:
        return False
#----------------------------------------------------------------------------------------

# enQueue함수
#----------------------------------------------------------------------------------------
def enQueue(data):
    global SIZE, queue, front, rear
    if isQueueFull():
        print('Queue is full')
        return
    rear = (rear+1) % SIZE
    queue[rear] = data
#----------------------------------------------------------------------------------------

# deQueue함수
#----------------------------------------------------------------------------------------
def deQueue():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print('Queue is empty')
        return None
    
    front = (front+1) % SIZE
    data = queue[front]
    queue[front] = None
    return data
#----------------------------------------------------------------------------------------

# peek함수
#----------------------------------------------------------------------------------------
def peek():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print('Queue is empty')
        return None
    return queue[(front+1) % SIZE]
#----------------------------------------------------------------------------------------

# 초기화
#----------------------------------------------------------------------------------------
SIZE = int(input('큐크기 입력 > '))
queue = [None for _ in range(SIZE)]
front = rear = 0
#----------------------------------------------------------------------------------------

## 메인 모듈
#----------------------------------------------------------------------------------------
if __name__ == '__main__':
    while True:
        select = input('삽입[I]/추출[E]/확인[V]/종료[Q] --> ').upper()

        if select == 'Q':
            break
        elif select == 'I':
            data = input('데이터 입력 > ')
            enQueue(data)
            print(f'큐상태 : {queue}')
        elif select == 'E':
            data = deQueue()
            print(f'데이터 추출 : {data}')
            print(f'큐상태 : {queue}')
        elif select == 'V':
            data = peek()
            print(f'데이터 확인 : {data}')
            print(f'큐상태 : {queue}')
        else:
            print('입력오류')
print('큐 종료!!!')
#----------------------------------------------------------------------------------------