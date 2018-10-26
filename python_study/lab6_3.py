"""
챕터: day6
주제: class
문제:
fraction 클래스는 애트리뷰트로 numer(분자)와 denom(분모)를 가진다. 초기화하는 메쏘드를 정의하라.

작성자: 주동석
작성일: 2018. 10. 23
"""

# 분수 클래스 정의
class Fraction:
    def __init__(self,n ,d):
        """
        분수를 초기화하는 메쏘드
        :param n: 분자에 해당하는 값
        :param d: 분모에 해당하는 값
        """
        self.numer = n
        self.denom = d

    def print(self):
        print("%d/%d" %(self.numer, self.denom))

    # 분자를 반환하는 메쏘드 getNumer 정의
    def getNumer(self):
        return self.numer

    # 분모를 반환하는 메쏘드 getdenom 정의
    def getDenom(self):
        return self.denom

    def setNumer(self, n):
        self.numer = n

    def setDenom(self, n):
        self.denom = n

    def add(self, o):
        r1 = self.denom * o.denom
        r2 = self.numer * o.denom + o.numer * self.denom
        r = Fraction(r2, r1)
        return r

# half = Fraction(1, 2)
# half.print()

f1 = Fraction(2, 7)
f1.print()

f2 = Fraction(1, 8)
f2.print()

# f1과 f2를 더한 결과를 출력
f1.add(f2).print()