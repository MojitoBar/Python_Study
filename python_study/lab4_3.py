"""
챕터: day4
주제: 조건문
문제: 사용자로부터 정수를 입력받는다.
      0보다 크면 "양수" 0이면 "0" 0보다 작으면 "음수"를 출력한다.
작성자: 주동석
작성일: 2018. 9. 18
"""

a = int(input("정수 입력: "))
print("양수") if a > 0 else (print("0") if a == 0 else print("음수"))