"""
과제제출양식을 반드시 맞추어서 제출하고, 종이 출력도 제출한다.

추가 내용

- 음수가 작동됨을 보장하라

- +, -, *, /, ==, !=, <, <=, >, >= 을 재정의하라.

- __str__ 함수를 정의하라.

작성자: 주동석
작성일: 2018. 11. 01
"""

# 분수 클래스 정의
class Fraction:
    # 초기화 함수
    def __init__(self, n, d):
        # 분자 초기화
        self.numer = n;
        # 분모 초기화
        self.denom = d;

    # 더하기 함수 재정의
    def __add__(self, other):
        new = Fraction(0, 0)
        new.denom = self.denom * other.denom
        new.numer = self.numer * other.denom + other.numer * self.denom
        return new.abbreviation()

    # 빼기 함수 재정의
    def __sub__(self, other):
        new = Fraction(0, 0)
        new.denom = self.denom * other.denom
        new.numer = self.numer * other.denom - other.numer * self.denom
        return new.abbreviation()

    # 곱하기 함수 재정의
    def __mul__(self, other):
        new = Fraction(0, 0)
        new.denom = self.denom * other.denom
        new.numer = self.numer * other.numer
        return new.abbreviation()

    # 나누기 함수 재정의
    def __truediv__(self, other):
        new = Fraction(0, 0)
        new.denom = self.denom * other.numer
        new.numer = self.numer * other.denom
        return new.abbreviation()

    # 약분 함수 정의
    def abbreviation(self):
        for i in range(2, self.denom):
            if (self.denom % i == 0 and self.numer % i == 0):
                self.denom = int(self.denom / i)
                self.numer = int(self.numer / i)
        return self

    # 분수를 보기 좋게 출력하는 함수
    def __str__(self):
        s = ""
        s = "(" + s + str(self.numer) + "/" + str(self.denom) + ")"
        return s

    # 두 분수 비교 (<)
    def __lt__(self, other):
        s = self.numer / self.denom
        o = other.numer / other.denom
        return s < o

    # 두 분수 비교 (<=)
    def __le__(self, other):
        s = self.numer / self.denom
        o = other.numer / other.denom
        return s <= o

    # 두 분수 비교 (>)
    def __gt__(self, other):
        s = self.numer / self.denom
        o = other.numer / other.denom
        return s > o

    # 두 분수 비교 (>=)
    def __ge__(self, other):
        s = self.numer / self.denom
        o = other.numer / other.denom
        return s >= o

    # 두 분수 비교 (==)
    def __eq__(self, other):
        s = self.numer / self.denom
        o = other.numer / other.denom
        return s == o


# case1
f1 = Fraction(-4, 5)
f2 = Fraction(3, 2)

print(f1*(f2))

# case2
f3 = Fraction(8, 31)
f4 = Fraction(2, 3)

print(f3.__sub__(f4))

# case3
f5 = Fraction(3, 5)
f6 = Fraction(3, 7)

print(f5.__add__(f6))

# case4
f7 = Fraction(4, 8)
f8 = Fraction(1, 2)

print(f7.__eq__(f8))

# case5
f9 = Fraction(2, 81)
f10 = Fraction(3, 9)

print(f9.__ge__(f10))