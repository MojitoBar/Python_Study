"""
    챕터: day7
    주제: os 모듈 사용
    문제:
    사용자가 입력한 디렉토리로 이동한 후, 사용자가 입력한 이름의 새 디렉토리를 생성하라.
    사용자가 입력한 디렉토리 아래에 test 디렉토리를 생성하라.
    사용자가 입력한 디렉토리를 포함하여 해당 디렉토리와 test 디렉토리를 삭제하라.
    삭제가 끝난 후, 사용자가 입력한 디렉토리(2)의 부모 디렉토리의 파일 목록을 출력하라.
    작성자: 주동석
    작성일: 2018. 12. 04
"""
import os

target = input("이동할 디렉토리: ")
l = os.chdir(target)
name = input("생성할 디렉토리 이름은: ")
os.mkdir(target+'/'+name+'/')
target1 = l + "\"" + name
os.mkdir(target1, "test")
os.rmdir(target1)

l = os.listdir(os.chdir(target))

for f in l:
    print(f)