# 파이썬 파일에서 필요한 클래스만 수입
import shape
# shape.py에 정의된 클래스, 함수 등을 수입해서 사용하겠다는 의미. .py 확장자는 붙이지 않는다.
from shape import Shape, Circle, Rectangle, Triangle

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