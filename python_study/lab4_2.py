"""
챕터: day4
주제: 조건문
문제: 사용자로부터 3개의 수를 입력 받아, 가장 작은 수를 출력하라.
작성자: 주동석
작성일: 2018. 9. 18
"""

a = int(input("첫 번째 수 입력: "))
b = int(input("두 번째 수 입력: "))
c = int(input("세 번째 수 입력: "))

min = ((a if a < c else c) if a < b else (b if b < c else c))

print(min)