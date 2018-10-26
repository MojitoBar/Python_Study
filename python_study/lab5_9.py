"""
챕터: day5
주제: 매개변수의 전달 방식 비교(call-by-reference)
문제:
A. list를 받아서, 마지막에 리스트의 요소의 개수를 요소로 추가하는 함수 addNum을 정의한다. 반환되는 값은 없다.
B. [5, 9, 4, 3]을 저장하는 list를 변수 l을 정의한다.
C. l을 인수로 addNum함수를 호출한 후 l을 출력한다.
작성자: 주동석
작성일: 2018. 10. 11
"""
global_v = 100

def addNum(list):
    global global_v
    global_v = 200
    list.append(len(list))

l = [5, 9, 4, 3]
addNum(l)
print(l)
print(global_v)
