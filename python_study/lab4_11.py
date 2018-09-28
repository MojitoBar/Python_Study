"""
챕터: day4
주제: 반복문(for문)
문제:
사용자로부터 5개의 숫자를 입력받아, 이를 리스트에 저장한 후 합과 평균을 구하여 출력한다.
작성자: 주동석
작성일: 2018. 9. 27
"""

# sum 초기화
sum = 0
# list arr에 값 저장
arr = list(input().split())

# for 문을 5번 돌면서 sum에 더함
for i in range (5):
    sum += int(arr[i])

# 리스트의 합과 평균 출력
print("리스트의 합: " + str(sum))
print("리스트의 평균: " + str(float(sum / 5)))