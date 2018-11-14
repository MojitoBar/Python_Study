"""
챕터: day6
주제: class
문제:
fraction 클래스는 애트리뷰트로 numer(분자)와 denom(분모)를 가진다. 초기화하는 메쏘드를 정의하라.

작성자: 주동석
작성일: 2018. 10. 23
"""

# 분수 클래스 정의
def gcm(a, b):
    # 큰 수를 a에 저장
    if a < b:
        (a, b) = (b, a)
    # 유클리드 호제법
    while b != 0:
        (a, b) = (b, a % b)
    return a

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

    def __eq__(self, o):
        g1 = gcm(self.numer, self.denom)
        g2 = gcm(o.numer, o.denom)
        if(self.numer // g1 == o.numer // g2) and (self.denom // g1, o.denom // g2):
            return True
        else:
            return False

# half = Fraction(1, 2)
# half.print()

f1 = Fraction(1, 2)
f1.print()

f2 = Fraction(5, 4)
f2.print()

# f1과 f2를 더한 결과를 출력
f3 = f1.add(f2)

for i in range(2, f3.denom):
    if(f3.denom % i == 0 and f3.numer % i == 0):
        f3.denom = int(f3.denom / i)
        f3.numer = int(f3.numer / i)

f3.print()

if(f1 != f3):
    print("다릅니다.")
else:
    print("같습니다.")