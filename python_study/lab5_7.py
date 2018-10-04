"""
챕터: day5
주제: 매개변수의 전달 방식 비교
문제:

작성자: 주동석
작성일: 2018. 10. 4
"""

def modify(n):
    n = n + 1
    return n

# 실행 시작 부분
k = 10 # 변수 정의
print("호출 전 k=", k) # 호출 전 변수 값 출력
re = modify(k) # modify 호출 후 결과 값을 re에 저장
print("호출 후 k=", k) # 호출 후 변수 값 출력
print("re=", re)