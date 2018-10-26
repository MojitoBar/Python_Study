"""
챕터: day6
주제: class
문제:
숫자를 하나씩 발생시키는 Counter 클래스 정의
작성자: 주동석
작성일: 2018. 10. 18
"""

# Counter 클래스 정의
class Counter:
    def __init__(self, start = 0):
        """
        instance를 생성할 때 초기화하는 메소드, instance를 생성할 때 자동 호출됨.
        """
        self.count = start

    def reset(self):
        """
        self: method가 수행되는 instance 자신을 의미
        :return:
        """
        self.count = 0

    def increment(self):
        """
        카운터를 하나 증가시킴
        :return:
        """
        self.count += 1

    def get(self):
        """
        self에 있는 count값을 반환
        :return:
        """
        return self.count

# 실행 코드 시작
# class Counter의 instance를 생성해서 변수 a에 저장
a = Counter()
# class Counter의 instance를 생성해서 변수 b에 저장
b = Counter(10)

a.increment()
a.increment()
a.increment()

print("a=%d" %a.get())

print("b=%d" %b.get())