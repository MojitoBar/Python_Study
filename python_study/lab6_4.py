# coding=utf-8
"""
챕터: day6
주제: class, class variable, 디폴트 매개변수, operator overloading 복습
문제: 정수집합 클래스

작성자: 주동석
작성일: 2018. 11. 6.
"""
"""
Student 클래스를 정의한다. 다음 학생에게 줄 학번을 클래스 변수(class variable) tag로 정의한다.
(메쏘드와 같은 레벨에서 변수를 정의하면 클래스 변수가 된다. self가 필요 없다)
"""

class Student:
    tag = 1 # 다음 학생에게 줄 학번, 모든 instance가 공유하여 사용, class variable(member)
    def __init__(self, name, grade=1):
        """
        이름, 학년을 매개변수로 받는다.
        :return: 없음
        """
        # 매개변수 값을 self 맴버(instance variable)에 배정한다.
        self.name = name
        self.grade = grade
        # 클래스 변수인 tag의 값을 학번으로 배정
        self.snum = Student.tag
        Student.tag += 1

    """
        Student 클래스에 학년을 올리는 upgrade()라는 메쏘드를 정의한다.
        self를 매개변수로 받는다. 몇 학년을 올릴지를 매개변수로 받는다. 1년 올리는 것이 디폴트이다.
    """
    def upgrade(self, n = 1):
        """
        4학년인 경우, 진급시키지 말고, "%s는 졸업 예정 학생 입니다."를 출력(%s에는 학생 이름)
        :param n:
        :return:
        """
        if self.grade == 4:
            print("%s는 졸업 예정 학생 입니다."%self.name)
        else:
            self.grade += n

    """
        Student 클래스에 __eq__ 메쏘드를 정의한다. 학번을 비교하여 같은 학생이면 True, 아니면 False를 반환한다.
    """
    def __eq__(self, o):
        if(self.snum == o.snum):
            return True
        else:
            return False

    def __str__(self):
        return "학번:" + str(self.snum) + " 이름:" + self.name + " 학년:" + str(self.grade)



# 실행부 시작
# 학생 인스턴스 3개 생성
s1 = Student("김일수", 4)
s2 = Student("김이수", 2)
s3 = Student("김삼수", 1)

print(s1)
print(s2)
print(s3)

# s2의 학년을 한 학년 높인다. (매개변수 안 보내기)
s2.upgrade()

# s3의 학년을 2학년 높인다. (매개변수 보내기)
s3.upgrade(2)

# 진급 후의 학생 정보 출력
print(s1)
print(s2)
print(s3)

# list에 3학생 정보 저장하기
l = []
l.append(s1)
l.append(s2)
l.append(s3)
l.append(Student("김사수"))

print("====리스트에 있는 요소 출력====")
for s in l:
    s.upgrade()
    print(s)

