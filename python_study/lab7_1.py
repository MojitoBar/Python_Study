"""
    챕터: day7
    주제: os 모듈 사용
    문제: 1. 현재 디렉토리를 출력한 후, 사용자로부터 파일을 생성할 디렉토리를 입력받고,
    입력된 디렉토리로 이동한 후 해당 디렉토리가 존재하지 않는다면, "입력한 디렉토리는 존재하지 않습니다."를 출력한다.
    Exception으로 처리하라. 일부러 오류를 발생시켜 Exection의 이름을 파악하라.
    작성자: 주동석
    작성일: 2018. 12. 04
"""

import os

print("현재 디렉토리: ", os.getcwd())

try:
    target = input("이동할 디렉토리")
    ㅣ = os.listdir(os.chdir(target))
except FileNotFoundError:
    print("입력한 디렉토리는 존재하지 않습니다.")
    exit()
for f in ㅣ:
    print(f)