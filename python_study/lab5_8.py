"""
챕터: day5
주제: 매개변수의 전달 방식 비교
문제:

작성자: 주동석
작성일: 2018. 10. 4
"""

def modify1(s):
    s += " To you"
    return s

msg = "Happy Birthday"
print("호출 전 msg", msg)
re = modify1(msg)
print("호출 후 msg=", msg)
print("re=", re)
