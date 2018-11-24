"""
    챕터: day6
    주제: 정규식
    문제: 정규식 기호 연습
    작성자: 주동석
    작성일: 2018. 11. 22
"""
import re
"""
1. apple에 a가 들어있는지 확인
2. apple에 b가 들어있는지 확인
3. 정규식을 이용하여, 사용자가 입력한 영어 문장에서 a, e, i, o, u가 포함되어 있는지 찾아서 출력하시오. 만족하는 첫번째만 출력한다.
<입력> This is a test.
"""
s1 = "apple"
if re.search("a", s1):
    print("a가 들어있습니다.")
else:
    print("b가 들어있지 않습니다.")

if re.search("b", s1):
    print("b가 들어있습니다.")
else:
    print("b가 들어있지 않습니다.")

s2 = input("영어 문장을 입력해 주세요: ")

print(re.search('[aeiou]', s2))

"""
4. 입력한 단어가 a로 시작하는지 확인
5. 입력한 단어가 e로 끝나는지 검사
"""
s3 = input("단어 하나를 입력해 주세요: ")

print(re.search('^a', s3))
print(re.search('e$', s3))

"""
7. 입력된 문장에서 숫자분분을 모두 출력하라.
A. 입력 예: 2017년 3월 8일 5000원
B. 출력 예:
2017
3
8
5000
"""

s4 = input("문장을 입력해 주세요: ")
l = re.findall("\d+", s4)
for i in l:
    print(i)
"""
10. 입력된 문장에서 <이후에 나오는 단어들을 출력하라.>
A. 입력 예: <2015> <김일수> <성공회대학교>
"""
s5 = input("문장을 입력해 주세요:")
l = re.findall("^<$\"", s5)
for i in l:
    print(i)