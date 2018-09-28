"""
챕터: day4
주제: 조건문
문제: 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.
작성자: 주동석
작성일: 2018. 9. 18
"""

# 시험 점수를 입력 받는다.
score = int(input())

# 90 ~ 100점은 A를 출력
if (score <= 100 and score >= 90):
    print("A")
# 80 ~ 89점은 B를 출력
elif (score <= 89 and score >= 80):
    print("B")
# 70 ~ 79점은 C를 출력
elif (score <= 79 and score >= 70):
    print("C")
# 60 ~ 69점은 D를 출력
elif (score <= 69 and score >= 60):
    print("D")
# 나머지 점수는 F를 출력
else:
    print("F")