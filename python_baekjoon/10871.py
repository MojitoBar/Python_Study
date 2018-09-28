"""
챕터: day4
주제: 반복문 for
문제: 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.
작성자: 주동석
작성일: 2018. 9. 20
"""
n, x = input().split()
n = int(n)
x = int(x)

arr = list(input().split())
arr2 = list()

for i in range(n):
     arr[i] = int(arr[i])
     if x > arr[i]:
          arr2.append(arr[i])

c = ""
for i in range(len(arr2)):
     c += str(arr2[i])
     if i < len(arr2) - 1:
          c += " "

print(c)