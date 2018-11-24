"""
    챕터: day6
    주제: 정규식
    문제: 정규식 기호 연습
    작성자: 주동석
    작성일: 2018. 11. 20
"""
import re

s7='href =      "C:\Python34\Kim.jpg"'
s8='href="C:\Python34\kim.jpg"'

# 공백(\t와 같은 것도 포함)이 나타나는 곳 찾기
print(re.search("\s", s7))

# 공백(\t와 같은 것도 포함)이 아닌 것이 나타나는 곳 찾기
print(re.search("\S", s7))

# s7, s8에서 'href='가 있는 곳 찾기
# 하나의 패턴을 여러 문자열에서 찾고 있으므로 compile 후 search 이용
r = re.compile("href=")
print(r.search(s7))
print(r.search(s8))

# s7에서  'href='가 있는 곳 찾기. =의 좌우에 빈 칸이 있든 없든 상관 없이 찾기
r = re.compile("href\s*=\s*")
print(r.search(s7))
print(r.search(s8))

r = re.compile("href\s*=\s*\"")
result = r.search(s7)
print(result.group())

print(re.split("=", s8))

print(re.sub("e+", "i", s7))

print(re.findall("\d", s7))

r = re.compile("(href\s*=\s*)(\".*\")")
result = r.search(s8)
print(result.group(0))
print(result.group(1))
print(result.group(2))
print(result.groups())