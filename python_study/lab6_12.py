"""
    챕터: day6
    주제: exception
    문제: 사용자로부터 1과 10사이의 숫자를 입력받아, 1부터 해당 숫자까지의 합을 구하라.
    만약 숫자가 아닌 값이 입력되면, "숫자를 입력하세요"라는 문장을 출력한 후 다시 입력을 받는다.
    작성자: 주동석
    작성일: 2018. 11. 27
"""
import re
# exception을 사용하지 않고 프로그래밍
s = 0
while(True):
    n = input("1과 10사이의 숫자를 입력해 주세요: ")
    if re.search("\D", n):
        print("숫자를 입력하세요")
    else:
        n = int(n)
        break
for i in range(1, n+1):
    s += i
print(s)