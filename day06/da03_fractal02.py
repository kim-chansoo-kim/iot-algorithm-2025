# 시에르핀스키 삼각형 그리기

from tkinter import *

# 전역변수 선언
#----------------------------------------------------------------------------------------
wSIZE = 1000
radius = 400
#----------------------------------------------------------------------------------------

# 함수 선언
#----------------------------------------------------------------------------------------
def drawTriangle(x, y, size):
    if size >= 10: # 숫자 조정으로 삼각형 갯수 변화
        drawTriangle(x, y, size/2)
        drawTriangle(x+size/2, y, size/2)
        drawTriangle(x+size/4, int(y-size*(3**0.5)/4), size/2)
    else:
        canvas.create_polygon(x, y, x+size, y, x+size/2, y-size*(3**0.5)/2, fill='#00FA9A', outline='#00FA9A')
#----------------------------------------------------------------------------------------

# 메인모듈
#----------------------------------------------------------------------------------------
root = Tk()
root.title('삼각형 모양의 프랙탈')
canvas = Canvas(root, height=wSIZE, width=wSIZE, bg='#FFFACD')
canvas.pack()

drawTriangle(wSIZE/5, wSIZE/5*4, wSIZE*2/3)
root.mainloop()
#----------------------------------------------------------------------------------------

# 터틀
import turtle
import time

def draw_sierpinski_debug(t, length, depth):
    if depth == 0:
        for _ in range(3):
            t.forward(length)
            t.left(120)
        return
    
    print(f"Depth: {depth}, Position: ({t.xcor()}, {t.ycor()}), Heading: {t.heading()}")
    
    draw_sierpinski_debug(t, length / 2, depth - 1)
    turtle.update()
    time.sleep(0.1)  # 딜레이 추가
    t.forward(length / 2)
    draw_sierpinski_debug(t, length / 2, depth - 1)
    turtle.update()
    time.sleep(0.1)  # 딜레이 추가
    t.backward(length / 2)
    t.left(60)
    t.forward(length / 2)
    t.right(60)
    turtle.update()
    draw_sierpinski_debug(t, length / 2, depth - 1)
    turtle.update()
    time.sleep(0.1)  # 딜레이 추가
    t.left(60)
    t.backward(length / 2)
    t.right(60)
    turtle.update()

# 설정
turtle.tracer(0)  # 애니메이션 속도 향상
t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(-200, -100)
t.pendown()

draw_sierpinski_debug(t, 400, 5)

turtle.update()
turtle.done()
