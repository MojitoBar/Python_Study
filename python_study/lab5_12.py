"""
챕터: day5
주제: 재귀함수(recursion)
자기 자신을 호출하는 함수
문제:
A. 곱하기를 더하기 반복문으로 구현한 함수 prod를 정의하여 prod(3,6)을 계산하여 출력

작성자: 주동석
작성일: 2018. 10. 11
"""

# 곱셈을 더하기로 구현한 함수
def prod(x, y):
    sum = 0;
    for i in range(y):
        sum += x
    return sum

print(prod(3, 6))

def r_prod(x, y):
    if y == 1:
        return x;
    else:
        return x + r_prod(x, y - 1)

print(r_prod(3, 6))