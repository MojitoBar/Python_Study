"""
챕터: day4
주제: 조건문
문제: 사용자로부터 2개의 수를 입력 받아, 큰 수를 출력하라.
작성자: 주동석
작성일: 2018. 9. 18
"""

# 첫 번째 정수 입력 받기
a = int(input("첫 번째 정수: "))
# 두 번째 정수 입력 받기
b = int(input("두 번째 정수: "))

# 첫 번째 정수가 두 번째 정수보다 크거나 같으면
if(a >= b):
# 첫 번째 정수 출력
    print(a)
# 두 번째 정수가 첫 번째 정수보다 크면
else:
# 두 번째 정수 출력
    print(b)