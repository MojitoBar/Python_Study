"""
챕터: day6
주제: class
문제:
과제 19

작성자: 주동석
작성일: 2018. 11. 13
"""
#  도형 클래스 정의
class Shape:
    def area(self):
        return 0
    def perimeter(self):
        return 0
    def __str__(self):
        return("도형")

# Shape를 상속 받는 Circle 클래스 정의
class Circle(Shape):
    # 메쏘드 변수 PI 선언
    PI = 3.1415
    def __init__(self, n):
        self.r = n
    def getRadius(self):
        return self.r
    def area(self):
        return self.r * self.r * self.PI
    def perimeter(self):
        return 2 * self.PI * self.r
    def __str__(self):
        return ("<원> " + "반지름:" + str(self.r))

# Shape를 상속 받는 Rectangle 클래스 정의
class Rectangle(Shape):
    def __init__(self, a, h):
        self.a = a
        self.h = h
    def getHeight(self):
        return self.h
    def getWidth(self):
        return self.a
    def getSides(self):
        l=[]
        l.append(self.a)
        l.append(self.h)
        l.append(self.a)
        l.append(self.h)
        return l
    def area(self):
        return self.a * self.h
    def perimeter(self):
        return 2 * (self.a + self.h)
    def __str__(self):
        return ("<직사각형> "+"밑변:"+str(self.a)+" 높이:"+str(self.h))

# Shape를 상속 받는 Triangle 클래스 정의
class Triangle(Shape):
    def __init__(self, a, b, c, h):
        self.first = a
        self.second = b
        self.third = c
        self.hight = h
    def getHeight(self):
        return self.hight
    def getWidth(self):
        return self.first
    def getSides(self):
        l=[]
        l.append(self.first)
        l.append(self.second)
        l.append(self.third)
        return l
    def area(self):
        return self.first * self.hight * 1/2
    def perimeter(self):
        return 2 * (self.first + self.second + self.third)
    def __str__(self):
        return ("<삼각형> "+"밑변:"+str(self.first)+" 높이:"+str(self.hight))


s = Shape() # s에 Shape()를 저장
c = Circle(5) # c에 반지름이 5인 Circle 저장
r = Rectangle(5, 10) # r에 밑변이 5이고 높이가 10인 Rectangle 저장
t = Triangle(3, 4, 5, 4) # t에 밑변이 3이고 두 변이 각각 4, 5, 높이가 4인 Triangle 저장

# c, r, t의 면적과 둘레 출력
print("c면적:"+str(c.area())+" c둘레"+str(c.perimeter()))
print("r면적:"+str(r.area())+" r둘레"+str(r.perimeter()))
print("t면적:"+str(t.area())+" t둘레"+str(t.perimeter()))

# t의 변들을 출력
st=""
for i in t.getSides():
    st = st + str(i) + " "
print(st)

# l 리스트를 생성해 s, c, r을 추가
l =[]
l.append(s)
l.append(c)
l.append(r)

# for문을 돌며 넓이와 둘레를 출력
for i in l:
    print(i)
    print("넓이:"+str(i.area()))
    print("둘레:"+str(i.perimeter()))
    print(i.getRadius()) # getRadius()는 Circle()클래스에만 있기 때문에 오류 발생