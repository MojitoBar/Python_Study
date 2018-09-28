"""
챕터: day4
주제: 반복문(for문)
문제:
사용자가 입력한 영문자를 아래와 같이 출력
(예)
BINGO
 INGO
  NGO
   GO
    O
작성자: 주동석
작성일: 2018. 9. 27
"""
str1 = input("영문자 입력: ")
for i in range(0, len(str1)):

    print(" " * i + str1[i:len(str1)])

str1 = input("영문자 입력: ")
i = 0
for i in range(0, len(str1)):
    str2 = ""
    for j in range(0, i):
        str2 = str2 + " "
    for j in range(i, len(str1)):
        str2 = str2 + str1[j]
    print(str2)