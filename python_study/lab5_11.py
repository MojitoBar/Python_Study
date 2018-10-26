"""
챕터: day5
주제: lambda 함수의 리스트
문제:

작성자: 주동석
작성일: 2018. 10. 11
"""
l = [lambda x: x**2,
     lambda x: x**3,
     lambda x: x**4]

for f in l:
    print(f(3))