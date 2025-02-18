import webbrowser
import time

SIZE = 100
stack = [None for _ in range(SIZE)] # 반복문에서 사용되지 않는 변수(i)는 '_'로 사용가능
top = -1

## 함수 선언
# 스택이 꽉 찾는지 확인하는 함수
#----------------------------------------------------------------------------------------    
def isStackFull():
    global SIZE, stack, top

    if (top >= SIZE - 1): # Full / 실무에서 쓰는 스택은 거의 무제한
        return True
    else: 
        return False
#----------------------------------------------------------------------------------------    
    
# 스택이 비었는지 확인
#----------------------------------------------------------------------------------------    
def isStackEmpty():
    global SIZE, stack, top

    if (top == SIZE - 1): # Empty
        return True
    else: 
        return False
#----------------------------------------------------------------------------------------    

# 스택에 데이터 추가
#----------------------------------------------------------------------------------------    
def push(data):
    global SIZE, stack, top

    if isStackFull() == True: # (isStackFull()):와 동일
        print('스택이 꽉 찼습니다.')
        return
    top += 1
    stack[top] = data
#----------------------------------------------------------------------------------------    

# 스택에서 데이터 추출
#----------------------------------------------------------------------------------------    
def pop(): 
    global SIZE, stack, top

    if (isStackEmpty()):
        print('스택이 비었습니다.')
        return None
    data = stack[top]
    stack[top] = None
    top -= 1
    return data
#----------------------------------------------------------------------------------------    

# 스택의 top위치의 데이터 확인(살짝보기)
#----------------------------------------------------------------------------------------    
def peek(): 
    global SIZE, stack, top

    if isStackEmpty():
        print('스택이 비었습니다.')
        return None
    return stack[top]
#----------------------------------------------------------------------------------------

## 메인모듈
#----------------------------------------------------------------------------------------    
if __name__ == '__main__':
    urls = ['naver.com', 'daum.net', 'google.com']

    for url in urls:
        push(url)
        webbrowser.open('http://' + url)
        print(url, end=' -> ')
        time.sleep(1)

    print('방문 종료!!!')
    time.sleep(5)

    while True:
        url = pop()
        if url == None:
            break
        webbrowser.open('http://' + url)
        print(url, end=' -> ')
        time.sleep(1)
    print('방문 종료!!!')
