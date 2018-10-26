"""
챕터: day6
주제: class
문제:
좌표를 표현하는 클래스 Cordinate를 정의한다.
1. __init__는 x, y 좌표를 받아서 self의 x, y에 배정
2. 거리를 구하는 distance 메소드를 정의한다. self와 다른 좌표 other를 매개 변수로 받는다.
거리는 (x좌표 사이의 차의 제곱과 y좌표 사이의 차의 제곱의 합의 제곱근이다.)

작성자: 주동석
작성일: 2018. 10. 18
"""

class Cordinate:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

"""
실행 코드 부분
(3, 4) 좌표의 점 c를 정의
원점 origin 정의
(3, 4)와 원점과의 거리 출력
"""

c = Cordinate(3, 4)
origin = Cordinate()

print("거리: %.2f" %c.distance(origin))
print("거리: %.2f" %Cordinate.distance(c, origin))