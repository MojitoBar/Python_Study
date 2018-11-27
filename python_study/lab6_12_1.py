"""
    챕터: day6
    주제: exception
    문제: 사용자로부터 1과 10사이의 숫자를 입력받아, 1부터 해당 숫자까지의 합을 구하라.
    만약 숫자가 아닌 값이 입력되면, "숫자를 입력하세요"라는 문장을 출력한 후 다시 입력을 받는다.
    작성자: 주동석
    작성일: 2018. 11. 27
"""

# exception을 사용하여 프로그래밍
while(True):
    s = 0
    try:
        n = int(input("1과 10사이의 숫자를 입력해 주세요: "))
        for i in range(1, n+1):
            s += i
        print(s)
        break
    except ValueError:
        print("숫자를 입력하세요")
