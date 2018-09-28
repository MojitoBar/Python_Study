"""
챕터: day3
주제: 문자열 연습
작성자: 주동석
작성일: 2018. 9. 6
"""

# p.70~

str11 = "가나다 참 쉽죠 생각해보니 그리 쉬운거 같진 않아요"
# 문장 자체를 변경하지는 않는다. 직접 print해야 바뀌는 것을 확인 가능.
str11.replace("가나다", "마바사")
print(str11)

# split 연습
# 앞 뒤 공백을 제거한 후 빈칸을 기준으로 단어를 모두 나누기
print(str11.strip().split(" "))
# 앞에서 두 개만 떼어 내기
print(str11.strip().split(" ", 2))
# str11의 길이 출력
print(len(str11))

s = "test"
s = "   kkk"
s = '''
kim
yee
hi
'''
print(s)

# i의 데이터 타입은 문자열 . input은 문자열을 반환하기 때문
i = input("문자열: ")
# i의 데이터 타입은 int . input은 문자열을 변환하기 떄문
i = int(input("문자열: "))


j = 100
#s1 는 str, j 는 int
s1 = str(j)