"""
챕터: day5
주제: 재귀함수
문제:
A. 팩토리얼 계산 함수 fact를 재귀함수로 정의하여, fact(5)를 호출한 결과를 출력하라.
작성자: 주동석
작성일: 2018. 10. 11
"""

def fact(n):
    if n == 1:
        return n
    return n * fact(n - 1)

print(fact(5))