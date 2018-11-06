# coding=utf-8
"""
챕터: day6
주제: class, class variable
문제: 정수집합 클래스

작성자: 주동석
작성일: 2018. 11. 6.
"""
"""
Student 클래스를 정의한다. 다음 학생에게 줄 학번을 클래스 변수(class variable) tag로 정의한다.
(메쏘드와 같은 레벨에서 변수를 정의하면 클래스 변수가 된다. self가 필요 없다)
"""

class Student:
    tag = 1 # 다음 학생에게 줄 학번, 모든 instance가 공유하여 사용, class variable(member)
    def __init__(self, name, grade):
        """
        이름, 학년을 매개변수로 받는다.
        :return: 없음
        """
        # 매개변수 값을 self 맴버(instance variable)에 배정한다.
        self.name = name
        self.grade = grade
        # 클래스 변수인 tag의 값을 학번으로 배정
        self.snum = Student.tag
        Student.tag += 1

    def __str__(self):
        return "학번: " + str(self.snum) + "이름: " + self.name