import turtle
import random

def drawTriangle(points, color):
    """주어진 세 꼭짓점(points)으로 삼각형을 채우는 함수"""
    turtle.fillcolor(color)
    turtle.penup()
    turtle.goto(points[0])  # 첫 번째 꼭짓점으로 이동
    turtle.pendown()
    
    turtle.begin_fill()
    for point in points[1:]:
        turtle.goto(point)
    turtle.goto(points[0])  # 마지막 선 연결
    turtle.end_fill()

def sierpinski(points, depth):
    """재귀적으로 시에르핀스키 삼각형을 그리는 함수"""
    if depth == 0:
        drawTriangle(points, random_color())
    else:
        mid1 = midpoint(points[0], points[1])
        mid2 = midpoint(points[1], points[2])
        mid3 = midpoint(points[2], points[0])
        
        sierpinski([points[0], mid1, mid3], depth - 1)
        sierpinski([mid1, points[1], mid2], depth - 1)
        sierpinski([mid3, mid2, points[2]], depth - 1)

def midpoint(p1, p2):
    """두 점의 중점을 계산하는 함수"""
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

def random_color():
    """랜덤한 색상을 반환하는 함수"""
    return (random.random(), random.random(), random.random())

def main():
    """메인 실행 함수"""
    turtle.speed(0)
    turtle.bgcolor("white")
    
    # 초기 삼각형 꼭짓점 설정
    size = 400  # 삼각형 크기
    points = [(-size, -size / 2), (size, -size / 2), (0, size * (3**0.5) / 2 - size / 2)]
    
    depth = 5  # 재귀 깊이 설정
    sierpinski(points, depth)
    
    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()
