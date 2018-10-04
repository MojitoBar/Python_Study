"""
챕터: day5
주제: 함수
문제:
두 개의 정수를 매개변수로  받아서, 두 수의 차를 반환하는 함수 substract를 정의한다.
4, 8을 매개변수로 substract를 호출한 후 결과를 출력한다.
작성자: 주동석
작성일: 2018. 10. 2
"""
# 두 수의 차를 반환하는 substract 함수 정의
def substract(a, b):
    return a - b

# 함수 호출
print(substract(4, 8))
# 키워드 인수(매개변수)
print(substract(b=4, a=8))

a = 10
b = True
c = "김치"
print(type(a))
print(type(b))
print(type(c))
