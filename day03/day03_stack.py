# 스택 동작확인 구현
SIZE = int(input('스택크기를 결정하세요 --> '))
stack = [None for _ in range(SIZE)] # 반복문에서 사용되지 않는 변수(i)는 '_'로 사용가능
top = -1

## 함수 선언
# 스택이 꽉 찾는지 확인하는 함수
#----------------------------------------------------------------------------------------    
def isStackFull():
    global SIZE, stack, top

    if (top == SIZE - 1): # Full / 실무에서 쓰는 스택은 거의 무제한
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
def Push(data):
    global SIZE, stack, top

    if isStackFull() == True: # isStackFull() == True와 동일
        print('Stack is Full!')
        # return 생략
    else:
        top += 1
        stack[top] = data
#----------------------------------------------------------------------------------------    

# 스택에서 데이터 추출
#----------------------------------------------------------------------------------------    
def pop(): 
    global SIZE, stack, top

    if isStackEmpty():
        print('Stack is Empty.')
        return None
    else:
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
        print('Stack is Empty.')
        return None
    else:
        return stack[top]
#----------------------------------------------------------------------------------------

## 메인모듈
#----------------------------------------------------------------------------------------    
if __name__ == '__main__':
    while True:
        select = input('삽입[I]/추출[E]/확인[V]/종료[Q] > ').upper()

        if select == 'Q':
            break
        elif select == 'I':
            data = input('입력 데이터 > ')
            Push(data)
            print(f'스택상태\n{stack}')
        elif select == 'E':
            data = pop()
            print(f'추출 데이터 > {data}')
            print(f'스택상태\n{stack}')
        elif select == 'V':
            data = peek()
            print(f'확인 데이터 > {data}')
            print(f'스택상태\n{stack}')
        else:
            print('입력오류~!')
print('스택 종료!!!')