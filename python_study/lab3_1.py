"""
챕터: day3
주제: 데이터형 연습
작성자: 주동석
작성일: 2018. 9. 4
"""

# f의 데이터타입은 float. 왜냐하면, f에 실수인 3.4가 저장되었으므로.
f = 3.4
print(f)
# i의 데이터타입은 int. 왜냐하면, i에 정수인 3이 저장되었으므로.
i = 3
print(i)
# b의 데이터타입은 boolean. 왜냐하면, b에 True가 저장되었으므로. (boolean type은 True 또는 False를 저장한다.)
b = True
print(b)
# s의 데이터타입은 str. 왜냐하면, s에 문자열인 "안녕하세요"가 저장되었으므로. (문자열은 " " 또는 ' '로 묶는다.)
s = "안녕하세요"
print(s)
# s의 데이터타입은 str.
s = '1'
print(s)

# f와 i를 더해서 출력. i가 float로 자동 변화되어 계산됨.
print(f + i)

# s와 i를 더해서 출력.
# 오류 발생. 왜냐하면, 문자열이 int로 자동변환되지는 않는다.
# print(s + i)

# s를 int로 형 변환하여 i와 더하기.
# 문자열을 형 변환 하는 것은 가능하다.
print(int(s) + i)

# i를 str로 형 변환하여 s와 더하기.
# 문자열 이어주기 연산이 실행됨.
print(str(i) + s)

i = 57
j = 28

# i를 j로 나눈 값 출력
print(i / j)
# i를 j로 나눈 몫 출력
print(i // j)
# i를 j로 나누었을 때 나머지 출력
print(i % j)
# j의 제곱 출력
print(j ** 2)
# j의 세제곱 출력
print(j ** 3)

# or 연산자
print(b or False)
# and 연산자
print(b and False)

# 복소수 (실수부와 허수부로 구성된 숫자) 타입 변수 k
k = 5 + 7j
print(k)
# 복소수에서 실수부만 추출
print(k.real)
# 복소수에서 허수부만 추출
print(k.imag)
# 켤레 복소수를 가져오는 함수 호출
print(k.conjugate())

# 8진수 표현
o = 0o16
print(o)
# 8진수로 o를 출력하겠다.
print("%o" %o)
# 16진수로 o를 출력하겠다.
print("%x" %o)

# 16진수 표현
x = 0xa5
# 십진수 출력
print("%d" %x)
# 8진수 출력
print("%o" %x)
# 16진수 출력
print("%x" %x)

i = 57.0
j = 28.0

# i를 j로 나눈 값 출력
print(i / j)
# i를 j로 나눈 몫 출력
print(i // j)
# i를 j로 나누었을 때 나머지 출력
print(i % j)
# j의 제곱 출력
print(j ** 2)
# j의 세제곱 출력
print(j ** 3)